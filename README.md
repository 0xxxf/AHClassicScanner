# AH CLASSIC SCANNER
## A python script that finds buyout prices for WoW Classic AH items

Currently working on it, right now the only function is finding a select item, you need to hardcode the API call
In order to work, you need a blizzard API Client (you need an access token in order to make api calls), refer to: https://develop.battle.net/documentation/guides/getting-started 


* Update data from Blizzard's API
```console
python3 main.py -u
``` 

* Retrieve item by name
```console
python3 main.py -i {item_name}
```
