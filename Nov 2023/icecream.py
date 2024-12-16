
# Imagine you and your friends had a fantastic day at an ice cream parlor, trying out different flavors. You want to create a program that helps you analyze your ice cream adventure!
#  Can you write a Python program that takes input on how many scoops of each flavor you all had,
#  and then calculates the total number of scoops, the average number of scoops per flavor, and identifies the most popular flavor(s)?
#  You can use the statistics module to help you calculate the mean, median, and mode!

# HINT:

# ﻿import statistics is used to import the statistics module, which provides functions for calculating mathematical statistics of numeric (real-valued) data.
# The calculate_mean function calculates the mean (average) of a list of numbers using the statistics.mean function.
# The calculate_median function calculates the median (middle value) of a list of numbers using the statistics.median function.
# The calculate_mode function calculates the mode (most common value) of a list of numbers using the statistics.mode function.
# The main function is the main entry point of the script. 
# It prints a welcome message and instructions for the user to enter the number of scoops of each ice cream flavor they had, separated by spaces.
# It then reads the input, converts it to a list of integers, calculates the total number of scoops, 
# and calculates the mean, median, and mode of the scoops using the defined functions. Finally, it prints the results.

import statistics

friend_flavors = {}

amount_people = int(input("Enter the amount of people going to the ice cream store including yourself::: "))

for i in range(amount_people):
    names = []
    friend_name = str(input(f"Enter the friend {i+1}'s name::: "))
    names.append(friend_name)

while True:
    flavor = {}
    flavors = str(input("Enter the flavor this friend has and when done type in 'done'::: "))
    if flavors.lower() == "done":
        break
    scoops = int(input(f"Enter the amount of scoops this person has of the {flavors} flavor::: "))
    flavor[flavors] = scoops
    
flavor[flavors] = scoops
friend_flavors[friend_name] = flavors


all_scoops = []
total_scoops = 0

print("\n-----Summary-----")
for friend, flavors in friend_flavors.items():
    friend_total = sum(flavor.values())
    all_scoops.extend(flavor.values())
    total_scoops += friend_total
    average_scoops = statistics.mean(flavor.values())
    print(f"{friend} - Total scoops: {friend_total}, Average scoops per flavor: {average_scoops:.2f}")

overall_average = statistics.mean(all_scoops)
max_scoops = max(all_scoops)

most_popular = [flavor for flavors in friend_flavors.values() for flavor, scoops in flavors.items() if scoops == max_scoops]

print(f"\nOverall total scoops: {total_scoops}")
print(f"Overall average scoops per flavor: {overall_average:.2f}")
print("Most popular flavor(s): " + ", ".join(most_popular))