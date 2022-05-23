import requests,json

def get_auctionhouse_data(access_token, region, realm, faction):
    """ Call Blizzard's API at us.api.blizzard.com/data/wow/connected-realm/{realm}/auctions/{auction}

    Args:
        realm: Id of desired realm
        auction: Id of AH
    Returns:
        status code of the request
    """
    custom_params = {"namespace": "dynamic-classic-us",
                     "locale": "en_US", "access_token": access_token}
    request_url = "https://{region}.api.blizzard.com/data/wow/connected-realm/{realm}/auctions/{faction}".format(region=region, realm=realm, faction=faction)

    res = requests.get(request_url, params=custom_params)
    data = res.json()
    with open("auction_data.json", 'w') as f:
        json.dump(data, f)
    return res.status_code

def get_realm_list(access_token):
    custom_params = {"namespace": "dynamic-classic-us", "locale": "en_US", "access_token": access_token}

    res = requests.get("https://us.api.blizzard.com/data/wow/realm/index", params=custom_params)
    for item in res.json()['realms']:
      print(item['name'],item['id'])
    return res.json()