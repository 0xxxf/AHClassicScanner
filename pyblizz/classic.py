import apihandler
import definitions


class Classic(apihandler.APICaller):
    def __init__(self, headers, region, token=None):
        super().__init__(headers, token)
        if region == "eu":
            super().namespace = "dynamic-classic-eu"
            super().locale = "eu"
        else:
            super().namespace = "dynamic-classic-us"
            super().locale = "us"

    def auctionHouseItems(self, region, realm, faction):
        namespace = definitions.getNameSpaceDynamic(0)

        request_url = "https://{region}.api.blizzard.com/data/wow/connected-realm/{realm}/auctions/{faction}".format(
            region=region, realm=realm, faction=faction)
        return super().requestJSON(request_url)

    def auctionHouseIndex(self, region, realm):
        request_url = "https://{region}.api.blizzard.com/data/wow/connected-realm/{connectedRealmId}/auctions/index".format(
            region=region, realm=realm)
        return super().requestJSON(request_url)

    def realmList(self, region):
        request_url = "https://{region}.api.blizzard.com/data/wow/realm/index".format(
            region=region)
        return super().requestJSON(request_url)
