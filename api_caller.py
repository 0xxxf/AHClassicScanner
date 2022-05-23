import requests,json

#TODO: change return type and standarize it across call functions, doesn't make much sense like this
def get_auctionhouse_data(access_token, region, realm, faction, write_to_file = False):
    """ Call Blizzard's API at us.api.blizzard.com/data/wow/connected-realm/{realm}/auctions/{auction}

    Args:
        access_token: 
        region:
        realm: Id of desired realm
        faction:
    Returns:
        [0]json data [1]status code of the request
    """
    custom_params = {"namespace": "dynamic-classic-us",
                     "locale": "en_US", "access_token": access_token}
    request_url = "https://{region}.api.blizzard.com/data/wow/connected-realm/{realm}/auctions/{faction}".format(region=region, realm=realm, faction=faction)

    res = requests.get(request_url, params=custom_params)
    data = res.json()
    if write_to_file:
      with open("auction_data.json", 'w') as f:
          json.dump(data, f)
    return res.json(), res.status_code

def get_realm_list(access_token):
    """ Call Blizzard's API at us.api.blizzard.com/data/wow/realm/index retrieving a list of realms and it's respective IDs

    Args:
        access_token:
    Returns:
        [0]json data [1]status code of the request
    """
    custom_params = {"namespace": "dynamic-classic-us", "locale": "en_US", "access_token": access_token}

    res = requests.get("https://us.api.blizzard.com/data/wow/realm/index", params=custom_params)
    for item in res.json()['realms']:
      print(item['name'],item['id'])
    return res.json(), res.status_code
