import streamlit as st
import pytz
from datetime import datetime
import time

# Function to get current time in a specific timezone
def get_time_in_timezone(timezone):
    tz = pytz.timezone(timezone)
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

# List of timezones to display
timezones = ['UTC', 'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']

st.title('World Clock')

# Display the current time in each timezone
for tz in timezones:
    st.write(f"{tz}: {get_time_in_timezone(tz)}")

# Update the time every 30 seconds
st_autorefresh = st.empty()
while True:
    st_autorefresh.write(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    time.sleep(30)
    st.experimental_rerun()
