import streamlit as st
from datetime import datetime
import pytz

# Title of the web app
st.title('World Clock Application')

# Dropdown menu for selecting locations
locations = {
    'New York': 'America/New_York',
    'Taipei': 'Asia/Taipei',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney',
    'Moscow': 'Europe/Moscow',
    'London': 'Europe/London',
}

# User can initially select locations, with a limit up to 4
if 'selected_locations' not in st.session_state:
    st.session_state.selected_locations = ['New York', 'Taipei']

# Render multiselect widget without directly limiting selections but track via session state
user_selection = st.multiselect('Select up to 4 locations', options=list(locations.keys()), default=st.session_state.selected_locations)

# Update session state and enforce limit if necessary
if len(user_selection) <= 4:
    st.session_state.selected_locations = user_selection
else:
    st.error('You can select up to 4 locations only.')
    # Automatically trim the selection to 4 if more are chosen
    st.session_state.selected_locations = user_selection[:4]

# Use columns to display the selected locations and their current times
col1, col2 = st.columns(2)

# Display the current time in the selected locations using columns for a cleaner look
for i, location in enumerate(st.session_state.selected_locations):
    timezone = pytz.timezone(locations[location])
    now = datetime.now(timezone)
    
    # Alternate between columns
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"**{location}**")
        st.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
