import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Your OpenWeatherMap API key
API_KEY = "416f71adf93c0805f149e088bef914e9"   # <-- Replace with your actual key
CITY = "India"  # You can change to any city you like

# URL to fetch forecast data
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Extract temperature and time
times = []
temperatures = []

for forecast in data['list']:
    time = datetime.datetime.fromtimestamp(forecast['dt'])
    temp = forecast['main']['temp']
    times.append(time)
    temperatures.append(temp)

# Plotting the data
plt.figure(figsize=(12, 6))
sns.lineplot(x=times, y=temperatures, marker="o")
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
