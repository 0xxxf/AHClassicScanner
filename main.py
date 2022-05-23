from os import access
import requests
import json
import csv
import sys
from os.path import exists
import api_caller

def get_access_token():
    f = open("access_token.json")
    data = json.load(f)
    access_token = str(data["access_token"])
    f.close()
    return access_token

def get_data_from_file():
    f = open("auction_data.json")
    return json.load(f)


def get_item_by_name(find_id):
    """ Finds an item id by its name using items.csv

    Returns:
        Id of item
    """  
    csv_file = "items.csv"
    data = {}
    with open(csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            entry = rows['entry']
            name = rows['name']
            data[name] = entry
    if str(find_id) in data:
        return data.get(str(find_id))
    return 0


def get_buyout_price(item_name):
    """ Gets the buyout price of an item.

    Args:
        item_name: Name of the item
    Returns:
        Buyout price in str format
    """
    data = get_data_from_file()
    item_buyout = {}
    for auction in data['auctions']:
        item = auction['item']['id']
        buyout = auction['buyout']
        item_buyout[item] = buyout

    sorted_list = sorted(item_buyout.items(), key=lambda x: x[0])
    id_to_find = get_item_by_name(str(item_name))

    for i in sorted_list:
        if str(i[0]) == str(id_to_find):
            return str(i[1])
    return 0

def copper_to_gsc(value):
    """ Converts copper into Gold,Silver,Copper format

    Args:
        value: Cooper value to transform
    Returns:
        Gold, Silver, Copper in Int format
    """
    g = value / 10000
    s = (value%10000) / 100
    c = (value%10000) % 100
    return int(g), int(s), int(c)

# Get options and args
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]


# If auction_data.json doesnt exist, update data 
if not exists("auction_data.json"):
    print("Auction data not found, updating Data...")
    data = get_auctionhouse_data("us",4408,2, True)
    if int(data) == 200:
        print("Data updated correctly")
    else:
        print("Data could not be updated, make sure you are using a correct token")

if "-u" in opts:
    # call blizz api and update our auction file
    data = api_caller.get_auctionhouse_data(get_access_token(),"us",4408,2,True)
    print("Request returned code: " + str(data[1]))
    if int(data[1]) == 200:
        print("Data updated and dumped into auction_data_json succesfully ")
    else:
        print("Data could not be updated")
elif "-r" or "--realms" in opts:
    api_caller.get_realm_list(get_access_token())
elif "-i" or "--item" in opts:
    price = get_buyout_price(str(args[0]))
    if price == 0:
        print("Item not found in AH")
    else:
        print("Last buyout price listed (Gold,Silver,Copper):")
        print(copper_to_gsc(int(price)))

else:
    raise SystemExit()
