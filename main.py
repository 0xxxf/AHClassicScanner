import requests
import json
import csv, json
import bisect
class Auction:
	def __init__(self, id, item, bid, buyout, quantity, time_left):
		self.id = id;
		self.item = item;
		self.bid = bid;
		self.buyout = buyout;
		self.quantity = quantity;
		self.time_left = time_left;

	def get_item_name(self):
		return get_item_by_id(self.item['id'])

def get_data_from_request():
	f = open("access_token.json")
	data = json.load(f)
	access_token = str(data['access_token'])

	custom_params = {"namespace":"dynamic-classic-us", "locale":"en_US", "access_token": access_token}

	res = requests.get('https://us.api.blizzard.com/data/wow/connected-realm/4372/auctions/2',params=custom_params)
	data = res.json()

	with open("auction_data.json", 'w') as f:
		json.dump(data,f)
	return data

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

auction_list = []
data = get_data_from_file()

for auction in data['auctions']:
	id = auction['id']
	item = auction['item']
	bid = auction['bid']
	buyout = auction['buyout']
	quantity = auction['quantity']
	time_left = auction['time_left']
	auction_list.append(Auction(id,item,bid,buyout,quantity,time_left))

item_buyout = {}

for auction in data['auctions']:
	item = auction['item']['id']
	buyout = auction['buyout']
	item_buyout[item] = buyout

sorted_list = sorted(item_buyout.items(), key=lambda x: x[0])
id_to_find =  get_item_by_name("Recipe: Hot Lion Chops")

for i in sorted_list:
	if str(i[0]) == str(id_to_find):
		print("BUYOUT PRICE: " + str(i[1]))
