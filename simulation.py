import random
import numpy
import matplotlib.pyplot as plt
from globalMemory import gmemory

class Simulation:

    def __init__(self):
        self.total_commission = 0
        self.computation_matrix = []
        self.artist_revenue_list = []
        self.artist_users_list = []
        self.users_following_list = []
        self.total_views_per_artist = [0]*gmemory.TOTAL_ARTISTS
        self.total_views_per_user = []

    
    def modifyRevenuePerView(self, artists_list, artists_skip_list): # update total_views_per_artist and total_views_per_user 
        # pass
        final_artists_views_list = [0]*gmemory.TOTAL_ARTISTS
        total_user_views = 0
        for i in range(gmemory.TOTAL_ARTISTS):
            if i in artists_skip_list: 
                final_artists_views_list[i] = 0
            else :
                rand_views = random.randint(1, gmemory.TOTAL_ARTISTS)
                final_artists_views_list[i] = rand_views
                total_user_views += rand_views
                self.total_views_per_artist[i] += rand_views

        print("Views of the user per artist :", final_artists_views_list)
        self.total_views_per_user.append(total_user_views)
        print("Total views for the user :", total_user_views)
        cost_share = 1-(gmemory.COMMISSION_COST/100)
        cost_per_view = (gmemory.SUBSCRIPTION_COST*cost_share)/total_user_views

        for i in range(gmemory.TOTAL_ARTISTS):
            final_artists_views_list[i] *= cost_per_view

        return final_artists_views_list


    def returnUserShare(self):
        #print("calculating user row\n")
        total_artists_followed = random.randint(1, gmemory.TOTAL_ARTISTS)
        self.users_following_list.append(total_artists_followed)
        commission = gmemory.COMMISSION_COST/100
        self.total_commission += (commission*gmemory.SUBSCRIPTION_COST)
        share_per_artist = ((gmemory.SUBSCRIPTION_COST*(1-commission))/total_artists_followed)
        artists_list = []
        artists_skip_list = []

        for i in range(gmemory.TOTAL_ARTISTS):
            artists_list.append(share_per_artist)

        total_artists_to_be_skipped = gmemory.TOTAL_ARTISTS - total_artists_followed

        print("Total artists followed :", total_artists_followed)
        print("Total artists not followed :", total_artists_to_be_skipped)

        if total_artists_to_be_skipped>0:
            i = 1
            rand_var = random.randint(1, gmemory.TOTAL_ARTISTS)
            artists_skip_list.append(rand_var)
            print("Skip list appended :", rand_var)
            # print("first skip val appended\n")
            while i <= (total_artists_to_be_skipped-1):
                # print("While loop running iteration : ", i)
                temp_rand = random.randint(1, gmemory.TOTAL_ARTISTS)
                if(temp_rand in artists_skip_list):
                    continue
                else:
                    artists_skip_list.append(temp_rand)
                    # print(artists_skip_list)
                    print("Skip list appended :", temp_rand)
                    i += 1

        print("Artist skip list calculated :", artists_skip_list)

        for i in artists_skip_list:
            artists_list[i-1] = 0 #artist list contains initial list of revenue each artist makes, prior to modifying for view p/a

        print("Initial Artist List :", artists_list)

        final_list = self.modifyRevenuePerView(artists_list, artists_skip_list)

        print("Final List calculated :", final_list)
        return final_list

    
    def populateComputationMatrix(self):
        print("-------------------------------------- Populating Computation Matrix -----------------------------------------------")
        i = 0
        while i < gmemory.TOTAL_USERS:
            print("Loop", (i+1), "in process...")
            rand_list = self.returnUserShare()
            print(rand_list)
            print('\n')
            self.computation_matrix.append(rand_list)
            #print("Row returned", i+1)
            i += 1
        print("\n-------------------------------------- Matrix population complete --------------------------------------\n")

    
    def printComputationMatrix(self):
        print("-------------------------------------- Computation Matrix : Rows -> Users, Columns -> Artists -------------------------------------- \n")
        print("Total number of users :", gmemory.TOTAL_USERS)
        print("Total number of artists :", gmemory.TOTAL_ARTISTS)
        print("\n")
        #print(self.computation_matrix)
        list_as_matrix = numpy.array(self.computation_matrix)
        print(list_as_matrix)
        print("\n")
        print("Total company commission based on", gmemory.COMMISSION_COST, "percent commission is :", self.total_commission)
        print("------------------------------------------------------------------------------------------------------------------\n")

    
    def printArtistResults(self):
        print("-------------------------------------- ARTIST ANALYSIS -------------------------------------- \n")
        for i in range(gmemory.TOTAL_ARTISTS):
            user_count = 0
            total_revenue = 0
            for j in range(gmemory.TOTAL_USERS):
                if self.computation_matrix[j][i] != 0:
                    user_count += 1
                    total_revenue += self.computation_matrix[j][i]
            print("Artist", (i+1))
            self.artist_revenue_list.append(total_revenue)
            self.artist_users_list.append(user_count)
            print("Total Revenue :", total_revenue, "\t Total Users :", user_count, "\t Total User Views :", self.total_views_per_artist[i])
            # print("\n")
        print("------------------------------------------------------------------------------------------------------------------\n")

    
    def printUserResults(self):
        print("-------------------------------------- USER ANALYSIS --------------------------------------\n")
        for i in range(gmemory.TOTAL_USERS):
            artist_count = 0
            for j in range(gmemory.TOTAL_ARTISTS):
                if self.computation_matrix[i][j] != 0:
                    artist_count += 1
            # fees_per_artist = self.subscription_cost/artist_count
            print("User", (i+1))
            # print("Total artists followed :", artist_count, "\t fees per artist :", fees_per_artist)
            # print("\n")
            print("Total artists followed :", artist_count, "\t Total Views :", self.total_views_per_user[i])
        print("------------------------------------------------------------------------------------------------------------------\n")

    
    def printArtistStatistics(self):
        print("-------------------------------------- ARTIST STATISTICS --------------------------------------\n")
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

        print("Artists followed by each user :", self.users_following_list)

        # min_revenue = self.artist_revenue_list.index(min(self.artist_revenue_list))
        # print("Artist with minimum revenue is Artist", (min_revenue+1), "with a revenue of", (self.artist_revenue_list[min_revenue], "and", (self.artist_users_list[min_revenue]), "users.\n")
        
        # max_revenue = self.artist_revenue_list.index(max(self.artist_revenue_list))
        # print("Artist with maximum revenue is Artist", (max_revenue+1), "with a revenue of", (self.artist_revenue_list[max_revenue], "and", (self.artist_users_list[max_revenue]), "users.\n")

        # min_users = self.artist_users_list.index(min(self.artist_users_list))
        # print("Artist with minimum users is Artist", (min_users+1), "with a revenue of", (self.artist_revenue_list[min_users], "and", (self.artist_users_list[min_users]), "users.\n")

        # max_users = self.artist_users_list.index(max(self.artist_users_list))
        # print("Artist with maximum users is Artist", (max_users+1), "with a revenue of", (self.artist_revenue_list[max_users], "and", (self.artist_users_list[max_users]), "users.\n")

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
        plt.title("Revenue (blue) X Users Following (green) X Total Views (red)")

        plt.show()


    def runSimulation(self):
        print("\n-------------------------------------- SIMULATION RUNNING --------------------------------------\n")
        self.populateComputationMatrix()
        self.printComputationMatrix()
        self.printArtistResults()
        self.printUserResults()
        self.printArtistStatistics()
        # self.printRevenueBarGraph()
        # self.printUsersBarGraph()
        self.printBarGraphs()
