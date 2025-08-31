import phonenumbers
import opencage
import folium




from test import number
from  phonenumbers import geocoder
ch_number =  phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key='188ba05efcc54efd99a5f38043232906'
geocoder = OpenCageGeocode(key)
query = location="me"
results= geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

mymap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat ,lng] ,popup=location).add_to(mymap)
mymap.save("mylocation2.html")