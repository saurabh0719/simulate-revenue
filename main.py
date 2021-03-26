from simulation import Simulation

def main():
    subscription_cost = int(input("Enter the per month user subscription cost : "))
    total_users = int(input("Enter the total number of users on the platform : "))
    total_artists = int(input("Enter the total number of artists on the platform : "))
    commission_cost = int(input("Enter platform commission eg. 40 for 40% :"))
    views_limit = int(input("Enter the views upper limit p/a :"))

    simulation = Simulation(subscription_cost, total_users, total_artists, commission_cost, views_limit)
    simulation.runSimulation()
    # summary_toggle = int(input("Enter 1 for detailed report and 0 for summary only :"))

    # simulation = Simulation(subscription_cost, total_users, total_artists, commission_cost)

    # if summary_toggle == 1 or summary_toggle == 0:
    #     simulation.runSimulation(summary_toggle)
    # else:
    #     print("Please enter a valid input for report/summary.")

if __name__ =="__main__":
    main()
