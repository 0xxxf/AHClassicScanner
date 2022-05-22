import requests
import json
import csv
import json
import bisect
import sys

def get_data_from_request():
    f = open("access_token.json")
    data = json.load(f)
    access_token = str(data['access_token'])

    custom_params = {"namespace": "dynamic-classic-us",
                     "locale": "en_US", "access_token": access_token}

    res = requests.get(
        'https://us.api.blizzard.com/data/wow/connected-realm/4372/auctions/2', params=custom_params)

    data = res.json()
    with open("auction_data.json", 'w') as f:
        json.dump(data, f)
    return res.status_code


def get_data_from_file():
    f = open("auction_data.json")
    return json.load(f)


def get_item_by_name(find_id):
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

    return "Not found"

def copper_to_gsc(value):
    g = value / 10000
    s = (value%10000) / 100
    c = (value%10000) % 100
    return int(g), int(s), int(c)


opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-u" in opts:
    # call blizz api and update our auction file
    data = get_data_from_request()
    print("Request returned code: " + str(data))
    if int(data) == 200:
        print("Data updated and dumped into auction_data_json succesfully ")
    else:
        print("Data could not be updated")
elif "-i" or "--item" in opts:
    print("Last buyout price listed (Gold,Silver,Copper):")
    price = get_buyout_price(str(args[0]))
    print(copper_to_gsc(int(price)))
else:
    raise SystemExit()
