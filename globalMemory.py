# Contains all global variables

class GlobalMemory:
    def __init__(self):
        self.SUBSCRIPTION_COST = 30
        self.TOTAL_USERS = 80
        self.TOTAL_ARTISTS = 20
        self.COMMISSION_COST = 40
        self.VIEWS_LIMIT = 30
        self.TOTAL_VIEWS_PER_ARTIST = []
        self.ARTIST_USERS_LIST = []

    def initMemory(self, subscription_cost, total_users, total_artists, commission_cost, views_limit):
        self.SUBSCRIPTION_COST = subscription_cost
        self.TOTAL_USERS = total_users
        self.TOTAL_ARTISTS = total_artists
        self.COMMISSION_COST = commission_cost
        self.VIEWS_LIMIT = views_limit

    def printGlobalMemory(self):
        print("Subscription cost :", self.SUBSCRIPTION_COST)
        print("Total Users :", self.TOTAL_USERS)
        print("Total Artists :", self.TOTAL_ARTISTS)
        print("Commission cost :", self.COMMISSION_COST)
        print("Views Limit :", self.VIEWS_LIMIT)

gmemory = GlobalMemory()

