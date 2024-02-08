import streamlit as st
import datetime
import pytz
from streamlit_autorefresh import st_autorefresh

# Use streamlit_autorefresh for updating the time every second
st_autorefresh(interval=1000, key="time_refresher")

# Title of the application
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