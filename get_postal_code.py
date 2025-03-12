import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from the .env file
load_dotenv()

def get_coord_from_pc(pc):
    url = "https://www.onemap.gov.sg/api/common/elastic/search?searchVal={}&returnGeom=Y&getAddrDetails=Y&pageNum=1".format(pc)

    bearer = "Bearer {}".format(os.getenv('OPENAPI_TOKEN'))
        
    headers = {"Authorization": bearer}
        
    response = requests.get(url, headers=headers)
        
    print(response.text)
    data = json.loads(response.text)
    lat = data['results'][0]['LATITUDE']
    lon = data['results'][0]['LONGITUDE']

    # return lat and lon
    return (lat, lon)

# start with a postal code 
postal_code = 544186

# convert it to lat/long using OneMap API
coordinates = get_coord_from_pc(postal_code)
print(coordinates)

# then we have to create the polygons for each constituency under the geojson dataset

# then we compare this lat,lon against all polygons to see which one it sits in 

# finally, we return the constituency 

