import random
import numpy
import matplotlib.pyplot as plt

class Simulation:

    def __init__(self, subscription_cost, total_users, total_artists, commission_cost):
        self.subscription_cost = subscription_cost
        self.total_users = total_users
        self.total_artists = total_artists
        self.commission_cost = commission_cost
        self.total_commission = 0
        self.computation_matrix = []
        self.artist_revenue_list = []
        self.artist_users_list = []
        self.users_following_list = []

    def returnUserShare(self):
        #print("calculating user row\n")
        total_artists_followed = random.randint(1, self.total_artists)
        self.users_following_list.append(total_artists_followed)
        commission = self.commission_cost/100
        self.total_commission += (commission*self.subscription_cost)
        share_per_artist = ((self.subscription_cost*(1-commission))/total_artists_followed)
        artists_list = []
        artists_skip_list = []

        for i in range(self.total_artists):
            artists_list.append(share_per_artist)

        total_artists_to_be_skipped = self.total_artists - total_artists_followed

        print("Total artists followed :", total_artists_followed)
        print("Total artists not followed :", total_artists_to_be_skipped)

        if total_artists_to_be_skipped>0:
            i = 1
            rand_var = random.randint(1, self.total_artists)
            artists_skip_list.append(rand_var)
            print("Skip list appended :", rand_var)
            # print("first skip val appended\n")
            while i <= (total_artists_to_be_skipped-1):
                # print("While loop running iteration : ", i)
                temp_rand = random.randint(1, self.total_artists)
                if(temp_rand in artists_skip_list):
                    continue
                else:
                    artists_skip_list.append(temp_rand)
                    # print(artists_skip_list)
                    print("Skip list appended :", temp_rand)
                    i += 1

        print("Artist skip list calculated :", artists_skip_list)

        for i in artists_skip_list:
            artists_list[i-1] = 0

        # print("Final List calculated :", artists_list)
        return artists_list

    def populateComputationMatrix(self):
        print("-------------------------------------- Populating Computation Matrix -----------------------------------------------")
        i = 0
        while i <self.total_users:
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
        print("Total number of users :", self.total_users)
        print("Total number of artists :", self.total_artists)
        print("\n")
        #print(self.computation_matrix)
        list_as_matrix = numpy.array(self.computation_matrix)
        print(list_as_matrix)
        print("\n")
        print("Total company commission based on", self.commission_cost, "percent commission is :", self.total_commission)
        print("------------------------------------------------------------------------------------------------------------------\n")

    def printArtistResults(self):
        print("-------------------------------------- ARTIST ANALYSIS -------------------------------------- \n")
        for i in range(self.total_artists):
            user_count = 0
            total_revenue = 0
            for j in range(self.total_users):
                if self.computation_matrix[j][i] != 0:
                    user_count += 1
                    total_revenue += self.computation_matrix[j][i]
            print("Artist", (i+1))
            self.artist_revenue_list.append(total_revenue)
            self.artist_users_list.append(user_count)
            print("Total Revenue :", total_revenue, "\t Total Users :", user_count)
            # print("\n")
        print("------------------------------------------------------------------------------------------------------------------\n")

    def printUserResults(self):
        print("-------------------------------------- USER ANALYSIS --------------------------------------\n")
        for i in range(self.total_users):
            artist_count = 0
            for j in range(self.total_artists):
                if self.computation_matrix[i][j] != 0:
                    artist_count += 1
            fees_per_artist = self.subscription_cost/artist_count
            print("User", (i+1))
            print("Total artists followed :", artist_count, "\t fees per artist :", fees_per_artist)
            # print("\n")
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
        base_axis_plot = list(range(1,self.total_artists+1))
        #print(base_axis_plot)
        plt.bar(base_axis_plot, self.artist_revenue_list, tick_label = base_axis_plot, width = 0.2, color = 'blue')
        # plt.xlabel("Artists")
        # plt.ylabel("Revenue")
        # plt.title("Revenue Bar Graph")

        for i in range(len(base_axis_plot)):
            base_axis_plot[i] += 0.2

        #print(base_axis_plot)
        plt.bar(base_axis_plot, self.artist_users_list, tick_label = base_axis_plot, width = 0.2, color = 'yellow')

        plt.xlabel("Artists")
        plt.ylabel("Users (y) / Revenue (b)")
        plt.title("Revenue (blue) X Users (yellow)")

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
