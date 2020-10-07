import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename1 = 'stations.json.gz'
filename2 = 'city_data.csv'

stations = pd.read_json(filename1, lines=True)
city_data = pd.read_csv(filename2)

stations['avg_tmax'] = stations['avg_tmax'].div(10)
city_data['area'] = city_data['area'].div(1000000)
city_data['density'] = city_data['population'].div(city_data['area'])
city_data = city_data.dropna()
city_data = city_data[city_data['area'] < 10000 ]

def distance(city, stations):
   
    lat2 = city['latitude']
    lon2 = city['longitude']
    # taken from https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206
    p = np.pi/180
    a = 0.5 - np.cos((lat2-stations['latitude'])*p)/2 + np.cos(stations['latitude']*p) * np.cos(lat2*p) * (1-np.cos((lon2-stations['longitude'])*p))/2
    return 12742 * np.arcsin(np.sqrt(a))

def best_tmax(city, stations):
    return stations.loc[np.argmin(distance(city,stations))]['avg_tmax']

best_tmax(city_data.iloc[0],stations)

city_data['tavg'] = city_data.apply(best_tmax,stations=stations,axis=1)

plt.plot(city_data['tavg'], city_data['density'], 'b.')
plt.xlabel('Avg Max Temperature (\u00b0C)')
plt.ylabel('Population Density (people/km\u00b2)')
plt.title('Temperature vs Population Density')
plt.savefig('output.png')