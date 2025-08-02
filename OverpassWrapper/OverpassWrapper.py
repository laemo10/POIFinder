import requests
import json

class OverpassWrapper(object):
    def __init__(self):
        self._OverpassURL = "https://overpass-api.de/api/interpreter"
        return

    def Request(self, lat : float, lon : float, radius : int, amenity : list[str] , nbPoints : int) -> dict:
        amenities = "|".join(amenity)

        # Overpass QL query
        query = f"""
            [out:json][timeout:25];
            (
              node["amenity"~"{amenities}"](around:{radius},{lat},{lon});
              way["amenity"~"{amenities}"](around:{radius},{lat},{lon});
              relation["amenity"~"{amenities}"](around:{radius},{lat},{lon});
            );
            out center {nbPoints};
            """

        response = requests.post(self._OverpassURL, data={"data": query})
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    o = OverpassWrapper()
    returnedDict = o.Request(46.8139, -71.2082, 2000, ["restaurant", "cafe"] ,10)
    print(returnedDict)
