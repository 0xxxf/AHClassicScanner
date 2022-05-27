import apihandler

class Classic(apihandler.APICaller):
    def __init__(self, headers, token=None):
        super().__init__(headers, token)

    def auctionHouseItems(self, region, realm, faction):
        request_url = "https://{region}.api.blizzard.com/data/wow/connected-realm/{realm}/auctions/{faction}".format(
            region=region, realm=realm, faction=faction)
        return super().requestJSON(request_url)

    def auctionHouseIndex(self, region, realm):
        request_url = "https://{region}.api.blizzard.com/data/wow/connected-realm/{connectedRealmId}/auctions/index".format(
            region=region, realm=realm)
        return super().requestJSON(request_url)

    def realmList(self, regionj):
        request_url = "https://{region}.api.blizzard.com/data/wow/realm/index".format(
            region=region)
        return super().requestJSON(request_url)


