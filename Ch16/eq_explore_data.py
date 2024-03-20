import json
import plotly.express as px

# json load - file
# json loads - str -> dic, dic, -> str

mag, lat, lon = [],[],[]



with open('c.geojson','r', encoding = 'utf-8' ) as f:
    data = json.load(f)
    # print(type(data['features']), type((data['features'][0])), len(data['features']))
    # print(data['features'][0]['properties']['mag'])
    # print(data['features'][0]['geometry']['coordinates'])
    for feature in data['features']:
        print(feature['properties']['mag'])
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])
        # print (mag, lon, lat)

fig=px.scatter_geo(lat=lat, lon=lon, size = mag)
fig.show()
