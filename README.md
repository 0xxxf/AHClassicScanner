# AH CLASSIC SCANNER
# WIP: Writing a Library to access Data, updating to this repo for now (BlizzAPIHandler) but I will probably move it once it's done.
## A python script that finds buyout prices for WoW Classic AH items

The scripts works by making calls to Blizzard's API, in order to make those calls you will need an API Client to generate an authentication token.

You can check how to create a new client [here](https://develop.battle.net/documentation/guides/getting-started)

The script will look for a token in access_token.json, here's a simple way to get a token via curl:

```sh
curl -u {client_id}:{client_secret} -d grant_type=client_credentials https://us.battle.net/oauth/token >> access_token.json
```

Now you can run the script without issues.

## Running
* Update data from Blizzard's API
```sh
python3 main.py -u
``` 

* Retrieve item by name
```sh
python3 main.py -i {item_name} {region} {realm_id} 
```

* Get all realms IDs
```sh
python3 main.py -r 
```
