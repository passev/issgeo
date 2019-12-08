from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import pprint
import geocoder


geolocator = Nominatim(user_agent="issgeo")
pp = pprint.PrettyPrinter(width=41, compact=True)

#api = requests.post("http://api.open-notify.org/iss-now.json")
#cevap = api.json()
#print (cevap['longitude'])

# ISS Koordinatlari

api = requests.get("http://api.open-notify.org/iss-now.json")
kisiler = requests.get("http://api.open-notify.org/astros.json")

cevap = api.json()
cevapkisi = kisiler.json()

pos = cevap['iss_position']
ad = cevapkisi['people']
lat = pos['latitude']
lon = pos['longitude']
sayi = cevapkisi['number']


# ISS Koordinatlari

iss = lat + ','+ ' ' + lon
location = geolocator.reverse(iss)
konum = geocoder.ip('me')
ev = (konum.latlng)
den = geolocator.reverse(ev)
uzak = (geodesic(ev, iss).kilometers)

print()
print("=========== ISS NEREDE (Eger None Yaziyorsa Okyanus Uzerindedir) ===========")
print()
print(location.address)
print()
print("=========== KONUMUMA OLAN UZAKLIK ===========")
print()
print(den, "'den", uzak, "km uzakta.")
print()
print("=========== ISS'de KAC KISI VAR ===========")
print()
print("ISS'de", sayi, "kisi var.")
print()
