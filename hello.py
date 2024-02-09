import requests
from bs4 import BeautifulSoup
import time
import warnings
from urllib3.exceptions import InsecureRequestWarning
import psycopg2

import os
password = os.getenv('POSTGRE_PASSWORD')



# Suppress SSL warnings
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

# Database connection parameters
db_config = {
    "host": "techin510-lab5.postgres.database.azure.com",
    "dbname": "postgres",
    "user": "chelsey",
    "password": password
}

def get_lat_lon(location):
    base_url = "https://nominatim.openstreetmap.org/search.php"
    query_params = {"q": location, "format": "jsonv2"}
    response = requests.get(base_url, params=query_params)
    data = response.json()
    if data and isinstance(data, list) and len(data) > 0:
        return data[0].get('lat'), data[0].get('lon')
    else:
        return None, None

def get_weather_data(lat, lon):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json',
    }
    point_url = f"https://api.weather.gov/points/{lat},{lon}"
    try:
        point_res = requests.get(point_url, headers=headers)
        point_res.raise_for_status()
        point_data = point_res.json()
        forecast_url = point_data['properties']['forecast']
        forecast_res = requests.get(forecast_url, headers=headers)
        forecast_res.raise_for_status()
        forecast_data = forecast_res.json()
        periods = forecast_data['properties']['periods']
        if periods:
            first_period = periods[0]
            forecast_summary = f"{first_period['name']}: {first_period['temperature']}°{first_period['temperatureUnit']}, {first_period['shortForecast']}"
            return forecast_summary
        else:
            return "Forecast data not available"
    except Exception as e:
        return f"Error fetching weather data: {e}"

def scrape_event_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'Not Available'
    date = soup.find('time').get_text(strip=True) if soup.find('time') else 'Not Available'
    location = soup.find('address').get_text(strip=True) if soup.find('address') else 'Not Available'
    lat, lon = get_lat_lon(location)
    weather = get_weather_data(lat, lon) if lat and lon else 'Weather data not available'
    return {'Name': name, 'Date': date, 'Location': location, 'Latitude': lat, 'Longitude': lon, 'Weather': weather}

def connect_postgres(config):
    try:
        conn = psycopg2.connect(**config)
        return conn
    except Exception as e:
        print(f"Database connection failed due to {e}")

def insert_event_details(conn, event_details):
    with conn.cursor() as cur:
        for event in event_details:
            sql = """INSERT INTO events (name, date, location, latitude, longitude, weather)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cur.execute(sql, (event['Name'], event['Date'], event['Location'], event['Latitude'], event['Longitude'], event['Weather']))
        conn.commit()

# Main scraping logic
event_links_set = set()
for page in range(1, 42):
    time.sleep(1)
    url = f"https://visitseattle.org/events/page/{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for a in soup.find_all('a', href=True):
        if '/events/' in a['href']:
            event_links_set.add(a['href'])
event_links = list(event_links_set)
print(f"Total unique links collected: {len(event_links)}")

# Scrape details for each event
event_details = [scrape_event_details(url) for url in event_links]

# Insert data into PostgreSQL
conn = connect_postgres(db_config)
if conn:
    insert_event_details(conn, event_details)
    conn.close()
    print("Data inserted into PostgreSQL database successfully.")
