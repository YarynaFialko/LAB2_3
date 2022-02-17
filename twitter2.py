import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def user_info(user_name):
    """
    Returns a dictionary with user's information
    user_name - string
    user_dict - dictionary
    """
    #acct = input('Enter Twitter Account:')
    if (len(user_name) < 1):
        return
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': user_name})
    #print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    user_dict = json.loads(data)
    #print(json.dumps(js, indent=2))

    #with open("data.json", 'w', encoding="utf-8") as file:
    #    json.dump(js, file, indent=2)
    return user_dict



