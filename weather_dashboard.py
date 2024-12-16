import streamlit as st
import requests

# Title
st.title("Real-Time Weather Dashboard")

# Input Section
city = st.text_input("Enter a city name:", "Mumbai")

# Fetch Weather Data
if st.button("Get Weather"):
    api_key = "148a0ab0c277fc08c6088fd408de009a"  # Replace with your OpenWeatherMap API Key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # API Call
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        # Display Weather Data
        st.subheader(f"Weather in {city.capitalize()}:")
        st.write(f"**Temperature:** {data['main']['temp']}°C")
        st.write(f"**Feels Like:** {data['main']['feels_like']}°C")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Weather:** {data['weather'][0]['description'].capitalize()}")
    else:
        st.error(f"City '{city}' not found!")

# Footer
st.markdown("Made with ❤️ using Streamlit")

