# AH CLASSIC SCANNER
## A python script that finds buyout prices for WoW Classic AH items

The scripts works by making calls to Blizzard' API, in order to make those calls you will need an API Client.

You can check how to create a new client [here](https://develop.battle.net/documentation/guides/getting-started)

Once you have your client, you need to generate a token, the python scripts retrieve this token from access_token.json, here's a simple way to make this via curl:
```sh
curl -u {client_id}:{client_secret} -d grant_type=client_credentials https://us.battle.net/oauth/token >> access_token.json
```

Now that you have a token you can run the script.

## Running
* Update data from Blizzard's API
```sh
python3 main.py -u
``` 

* Retrieve item by name
```sh
python3 main.py -i {item_name}
```
