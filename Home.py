import streamlit as st
import qrcode

# Define the title and description
st.title("Advent Calendar")
st.write("Countdown to Christmas!")

# Define the date and current day
today = 1  # Change this value to the current day
total_days = 25  # Total number of days in December

# Create a loop for each day of the advent calendar
for i in range(1, total_days + 1):
    if i < today:
        st.write(f"🎄 Day {i}: You missed this one!")
    elif i == today:
        st.write(f"🎁 Day {i}: It's today! Click to open your surprise!")
        day_number = i
        url = "https://youtu.be/mcUza_wWCfA?si=VmzTHzDU5eVuQa5E"
        message = f"Day {day_number} of the month: {url}"
        img = qrcode.make(message)
        st.image(img.get_image(), caption=f"QR Code for {url}", use_column_width=True)
    else:
        st.write(f"🗓️ Day {i}: Coming soon...")

# Display a festive message
st.write("Merry Christmas and Happy Holidays!")
