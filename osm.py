import folium
from zones import MarkerCoordinates, markers


omsk = MarkerCoordinates("omsk", "omsk", 54.991416, 73.364253)

m = folium.Map(location=[omsk.lat, omsk.long], zoom_start=10)

for marker in markers:
    folium.Marker(location=[marker.lat, marker.long], tooltip=marker.name, popup="{}".format(marker.descriptions) ).add_to(m)

m.save("map.html")