import apihandler


class Retail(apihandler.APICaller):
    def __init__(self, headers, token=None):
        super().__init__(headers, token)

    def auctionHouseItems(self, region, connectedRealmId):
        """ 
        This response may be > 10 MB
        """
        request_url = "https://{region}.api.blizzard.com/data/wow/connected-realm/{connectedRealmId}/auctions/".format(
            region=region, connectedRealmId=connectedRealmId)
        return super().requestJSON(request_url)
