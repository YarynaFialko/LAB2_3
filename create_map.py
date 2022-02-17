"""
This module creates a map with friends' marks.
"""
import sys
import folium
from geopy.geocoders import ArcGIS, Nominatim
import twitter2

arcgis = ArcGIS(timeout=10)
nominatim = Nominatim(timeout=10, user_agent="htrtrrfr")
geocoders = [arcgis, nominatim]

def receive_data(data):
    """
    Filters the data.
    """
    users = data['users']

    friends = {}
    for user in users:
        name = user.get('screen_name')
        location = user.get('location')
        if location:
            friends[name] = location
    return friends


def geocode(address):
    """
    Returns coordinates using the address.
    >>> geocode("Chicago, Illinois, USA")
    (41.884250000000065, -87.63244999999995)
    """
    i = 0
    try:
        while i < len(geocoders):
            location = geocoders[i].geocode(address)
            if location is not None:
                return location.latitude, location.longitude
            else:
                i += 1
    except TypeError:
        print(sys.exc_info()[0])
        return ['null', 'null']
    return ['null', 'null']



def create_html(data):
    """
    Creates a HTML map file.
    data -> dict
    """
    my_map = folium.Map(location=[0, 0], zoom_start=2)
    fg_1 = folium.FeatureGroup(name="Friends locations")
    for name, val in zip(data.keys(), data.values()):
        mark = f"Name: {name}\nLocation: {val[0]}\n"
        coord = f"Latitude: {str(round(val[1][0],4))}\nLongitude: {str(round(val[1][1], 4))}"
        fg_1.add_child(folium.Marker(
            location=[val[1][0], val[1][1]], popup=mark+coord, icon=folium.Icon()))
    my_map.add_child(fg_1)
    my_map.save('lab2_3/templates/map.html')


def main(user_name):
    """
    Operates fuctions
    """
    data = twitter2.user_info(user_name)
    friends = receive_data(data)
    friends_data = {}
    for user in friends.items():
        address = geocode(user[1])
        if address != ['null', 'null']:
            friends_data[user[0]] = [user[1], address]
    create_html(friends_data)
