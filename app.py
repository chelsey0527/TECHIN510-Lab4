import streamlit as st
import datetime
import pytz
from streamlit_autorefresh import st_autorefresh

# Initialize 'page' in session state if it's not already present
if 'page' not in st.session_state:
    st.session_state['page'] = 'World Clock'

# Page Selector
page = st.radio('Choose a page:', ['World Clock', 'Unix Timestamp'])

# Update the session state based on the page selection
st.session_state['page'] = page

# Use streamlit_autorefresh for updating the time every second
st_autorefresh(interval=1000, key="time_refresher")

if page == 'World Clock':
    st.title('World Clock')

   

    # List of available time zones
    time_zones = list(pytz.all_timezones)

    # Dropdown menu for selecting locations
    selected_zones = st.multiselect('Select up to 4 locations:', time_zones, default=["UTC"], help="You can select up to 4 locations.")

    # Limit selection to 4 locations
    if len(selected_zones) > 4:
        st.error("Please select up to 4 locations only.")
    else:
        # Display the current time for the selected locations
        for zone in selected_zones:
            tz = pytz.timezone(zone)
            current_time = datetime.datetime.now(tz)
            st.write(f"Current time in {zone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

elif page == 'Unix Timestamp':
    st.title('Current Time in Unix Timestamp')

    # List of available time zones
    time_zones = list(pytz.all_timezones)

    # Dropdown menu for selecting locations
    selected_zones = st.multiselect('Select locations:', time_zones, default=["UTC"], help="You can select up to 4 locations.")

    # Limit selection to 4 locations
    if len(selected_zones) > 4:
        st.error("Please select up to 4 locations only.")
    else:
        # Display the current Unix timestamp for the selected locations
        for zone in selected_zones:
            tz = pytz.timezone(zone)
            current_time = datetime.datetime.now(tz)
            unix_timestamp = int(current_time.timestamp())  # Convert to Unix timestamp
            st.write(f"Unix timestamp for {zone}: {unix_timestamp}")
