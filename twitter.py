import urllib.request, urllib.parse, urllib.error
import json
import ssl
import twurl


def get_twitter_info(account):
    """
    (str) -> list
    This function forms a list of
    username's friends' locations.
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Setting context
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Getting the information for the username.
    try:
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': account, 'count': '25'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        f = json.loads(data)
    except:
        return []
    friends_locs_lst = []
    for u in f['users']:
        friends_locs_lst.append((u['screen_name'], u['location']))
    return friends_locs_lst

