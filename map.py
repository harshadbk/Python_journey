import geocoder
import folium
g= geocoder.ip("me")
myaddress=g.latlng
print(myaddress)

my_map1=folium.Map(location=myaddress,
                   zoom_start=1)
folium.CircleMarker(location=myaddress,
                    radius=50,popup="Yorkshire").add_to(my_map1)
folium.Marker(myaddress,popup="Yorkshire").add_to(my_map1)
my_map1.save("my_map.html")