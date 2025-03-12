import requests
import os
from dotenv import load_dotenv
import json
import geopandas as gpd

### SETUP ###
# Load environment variables from the .env file
load_dotenv()

# Load GeoJSON data into a GeoDataFrame
geojson_file = 'data/2025.geojson'  # Replace with the path to your GeoJSON file
gdf = gpd.read_file(geojson_file)

### EXECUTION ###

# def get_coord_from_pc(pc):
#     url = "https://www.onemap.gov.sg/api/common/elastic/search?searchVal={}&returnGeom=Y&getAddrDetails=Y&pageNum=1".format(pc)

#     bearer = "Bearer {}".format(os.getenv('OPENAPI_TOKEN'))
        
#     headers = {"Authorization": bearer}
        
#     response = requests.get(url, headers=headers)
        
#     print(response.text)
#     data = json.loads(response.text)
#     lat = data['results'][0]['LATITUDE']
#     lon = data['results'][0]['LONGITUDE']

#     # return lat and lon
#     return [lat, lon]

# # start with a postal code 
# postal_code = 544186

# convert it to lat/long using OneMap API
# coordinates = get_coord_from_pc(postal_code)
coordinates=['1.3934293161425', '103.905442121703']
lat = '1.3934293161425'
lon = '103.905442121703'
# print(coordinates)

# then we have to create the polygons for each constituency under the geojson dataset

def create_polygons():
    polygons = gpd.GeoDataFrame(geometry=gdf.geometry)
    print(gdf)

    return polygons

polygons = create_polygons()
print(polygons)


def inside(lat, lon, vs):
    """
    Check if a point is inside a polygon using the ray-casting algorithm.
    
    :param point: Tuple (x, y) representing the point.
    :param vs: List of tuples [(x1, y1), (x2, y2), ...] representing the polygon vertices.
    :return: True if the point is inside the polygon, False otherwise.
    """
    x = lat
    y = lon
    inside = False
    n = len(vs)

    for i in range(n):
        j = (i - 1) % n  # Ensure j wraps around
        xi, yi = vs[i]
        xj, yj = vs[j]

        intersect = ((yi > y) != (yj > y)) and \
                    (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        
        if intersect:
            inside = not inside

    return inside

for polygon in polygons:
    if inside(lat, lon, polygon): 
        print("found it")
        print("The Constituency is {}")
        print(polygon)
        break



# then we compare this lat,lon against all polygons to see which one it sits in 

# finally, we return the constituency 

