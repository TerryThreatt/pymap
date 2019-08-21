import folium
import pandas

# data
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# marker color function
def color_producer(elevation): 
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else: 
        return 'red'

# map 
map = folium.Map(location=[29.744814, -95.5873537], zoom_start=6, titles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

# location marker loop
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=color_producer(el))))

# adding child elements
map.add_child(fg)

map.save("Map1.html")

