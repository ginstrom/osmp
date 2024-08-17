import requests
import json

def get_tokyo_stations():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area["name"="東京都"]->.tokyo;
    (
      node["railway"="station"](area.tokyo);
    );
    out body;
    """

    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()

    stations = []
    for element in data['elements']:
        if 'tags' in element:
            station = {
                'id': element['id'],
                'lat': element['lat'],
                'lon': element['lon'],
                'name': element['tags'].get('name', 'Unknown'),
                'name:en': element['tags'].get('name:en', 'Unknown'),
                'operator': element['tags'].get('operator', 'Unknown'),
                'wikipedia': element['tags'].get('wikipedia', 'Unknown'),
            }
            stations.append(station)

    return stations

# Fetch and print the stations
tokyo_stations = get_tokyo_stations()
print(json.dumps(tokyo_stations[:5], indent=2, ensure_ascii=False))
