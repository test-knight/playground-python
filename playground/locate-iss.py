#  https://www.openstreetmap.org/?mlat=33.8891&mlon=-84.4533#map=16/33.8891/-84.4533
# iss location: http://api.open-notify.org/iss-now.json

from urllib import request
import json
import webbrowser

iss_api_url = 'http://api.open-notify.org/iss-now.json'
iss_location = request.urlopen(iss_api_url)

json_obj = json.loads(iss_location.read())
print(json_obj)
lat = json_obj['iss_position']['latitude']
long = json_obj['iss_position']['longitude']
zoom_level = 4


iss_location_mapped = f"https://www.openstreetmap.org/?mlat={lat}&mlon={long}#map={zoom_level}/{lat}/{long}"
print(iss_location_mapped)

# shows location of ISS in a (default) webbrowser
webbrowser.open(iss_location_mapped)
