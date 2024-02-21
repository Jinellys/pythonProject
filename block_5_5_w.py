import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

# weather_2012_final = pd.read_csv('data/weather_2012.csv', index_col='Date/Time')
# weather_2012_final['Temp (C)'].plot(figsize=(18, 6))
url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3, year=2012)
weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1')
weather_mar2012
weather_mar2012["Temp (Â°C)"].plot(figsize=(15, 5))