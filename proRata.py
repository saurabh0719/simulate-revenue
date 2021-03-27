import random
import numpy
import matplotlib.pyplot as plt
from globalMemory import gmemory

# This simulation runs on the assumption that UserCentricSimulation has already been computed for gmemory.TOTAL_VIEWS_PER_ARTIST and gmemory.ARTIST_USERS_LIST
class ProRataSimulation:

    def __init__(self):
        self.total_commission = 0
        self.total_views_per_artist = gmemory.TOTAL_VIEWS_PER_ARTIST
        self.artist_revenue_list = [0]*gmemory.TOTAL_ARTISTS
        self.artist_users_list = gmemory.ARTIST_USERS_LIST

    
    def computeArtistRevenue(self, total_money, total_views):
        for i in range(gmemory.TOTAL_ARTISTS):
            self.artist_revenue_list[i] = (self.total_views_per_artist[i]/total_views)*total_money


    def compute(self):
        total_money = gmemory.TOTAL_USERS*gmemory.SUBSCRIPTION_COST
        self.total_commission = (gmemory.COMMISSION_COST/100)*total_money
        total_money -= self.total_commission
        total_views = sum(self.total_views_per_artist)
        self.computeArtistRevenue(total_money, total_views)

    
    def printArtistResults(self):
        print("-------------------------------------- PRO RATA ARTIST ANALYSIS -------------------------------------- \n")
        for i in range(gmemory.TOTAL_ARTISTS):
            print("Artist", (i+1))
            print("Total Revenue :", self.artist_revenue_list[i], "\t Total Users :", self.artist_users_list[i], "\t Total User Views :", self.total_views_per_artist[i])
            # print("\n")
             
        print("------------------------------------------------------------------------------------------------------------------\n")


    def printArtistStatistics(self):
        print("-------------------------------------- PRO RATA ARTIST STATISTICS --------------------------------------\n")
        artists_mean_revenue = numpy.mean(self.artist_revenue_list)
        artists_mean_users = numpy.mean(self.artist_users_list)

        artists_median_revenue = numpy.median(self.artist_revenue_list)
        artists_median_users = numpy.median(self.artist_users_list)

        print("Mean revenue per artist :", artists_mean_revenue, "\nMean no. of users per artist :", artists_mean_users)
        #print("\n")
        print("Median revenue per artist :", artists_median_revenue, "\nMedian no. of users per artist :", artists_median_users)
        print("\n")

        print("Artists revenue list :", self.artist_revenue_list)
        print("Artists user following :", self.artist_users_list)

        print("\n------------------------------------------------------------------------------------------------------------------\n")


    def printBarGraphs(self):
        initial_base_axis_plot = list(range(1,gmemory.TOTAL_ARTISTS+1))
        base_axis_plot = list(range(1,gmemory.TOTAL_ARTISTS+1))
        #print(base_axis_plot)
        plt.bar(base_axis_plot, self.artist_revenue_list, tick_label = initial_base_axis_plot, width = 0.2, color = 'blue')
        # plt.xlabel("Artists")
        # plt.ylabel("Revenue")
        # plt.title("Revenue Bar Graph")

        for i in range(len(base_axis_plot)):
            base_axis_plot[i] += 0.2

        #print(base_axis_plot)
        plt.bar(base_axis_plot, self.artist_users_list, tick_label = initial_base_axis_plot, width = 0.2, color = 'green')

        for i in range(len(base_axis_plot)):
            base_axis_plot[i] += 0.2

        plt.bar(base_axis_plot, self.total_views_per_artist, tick_label = initial_base_axis_plot, width = 0.2, color = 'red')

        plt.xlabel("Artists")
        plt.ylabel("Revenue/Users/Views")
        plt.title("PRO RATA Revenue (blue) X Users Following (green) X Total Views (red)")

        plt.show()

    
    def runSimulation(self):
        print("\n-------------------------------------- PRO RATA SIMULATION RUNNING --------------------------------------\n")
        self.compute()
        self.printArtistResults()
        self.printArtistStatistics()
        self.printBarGraphs()


    