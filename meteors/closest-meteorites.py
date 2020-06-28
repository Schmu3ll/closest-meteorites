import requests
import math

koti_lng = 60.273060
koti_lat = 25.02134
json_data = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
meteor_data = json_data.json()

def calc_dist(lat1, lng1, lat2, lng2):
	lat1 = math.radians(lat1)
	lng1 = math.radians(lng1)
	lat2 = math.radians(lat2)
	lng2 = math.radians(lng2)

	h = math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin((lng2-lng1)/2)**2

	return 6372.8 * 2 *math.asin(math.sqrt(h))

def dataloop():
	for spot in meteor_data:
		if not ('reclat' in spot and 'reclong' in spot): continue
		spot_lat = float(spot['reclat'])
		spot_lng = float(spot['reclong'])

		spot_dist = calc_dist(koti_lat,koti_lng,spot_lat,spot_lng)
		spot['distance_from_home'] = spot_dist

def get_dist(spot):
	return spot.get('distance', math.inf)

dataloop()

meteor_data.sort(key=get_dist)
print(meteor_data[0:10])
