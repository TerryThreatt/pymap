import folium 


map = folium.Map(location=[29.744814, -95.5873537], zoom_start=6, titles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")


for coordinates in [[38.2, -99.1], [30.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I'm a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")