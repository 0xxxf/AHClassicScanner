class Definitions:
    # Classic
    D_NAMESPACE_CLASSIC_EU = "dynamic-classic-eu"
    D_NAMESPACE_CLASSIC_US = "dynamic-classic-us"
    S_NAMESPACE_CLASSIC_EU = "static-classic-eu"
    S_NAMESPACE_CLASSIC_US = "static-classic-us"

    # Retail
    D_NAMESPACE_EU = "dynamic-eu"
    D_NAMESPACE_US = "dynamic-us"
    S_NAMESPACE_EU = "static-eu"
    S_NAMESPACE_US = "static-us"
    P_NAMESPACE_EU = "profile-eu"
    P_NAMESPACE_US = "profile-us"

    @staticmethod
    def getNamespaceDynamic(region, call_type):
        # call_type = static = 0 /dynamic = 1
        if region == 1:
            if call_type == 0:
                return S_NAMESPACE_CLASSIC_EU
            if call_type == 1:
                return D_NAMESPACE_CLASSIC_EU
        if region == 2:
            if call_type == 0:
                return S_NAMESPACE_CLASSIC_US
            if call_type == 1:
                return D_NAMESPACE_CLASSIC_US

        return None
