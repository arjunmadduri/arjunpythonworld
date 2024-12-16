#Library statistics for mean, median, and mode
import statistics

#This is where all the flavors and the friends eating those flavors and howmany scoops those friends ate for that flavor
friends_flavors = {}

#variable for asking the number of friends
num_friends = int(input("Enter the amount of people including yourself::: "))

#welcoming the user to the analyzer
print("---Welcome to the Ice Cream Analyzer---")

#for loop for the friend name and what flavor by the number of friends that went to the ice cream store in the first place
for i in  range(num_friends):
    friend_name = input(f"\nEnter the name of Friend {i + 1}: ")
#flavors is where we store our flavors and friend that ate it then being appended to (friends_flavors)
    flavors = {}
    print(f"{friend_name}, please enter you flavor of ice cream::: ")

#an infinite loop that goes until all friends are done inputing their flavors and scoops of flavors, when done with one person press "done" to go to the next part of the code
while True:
    flavor = input("Enter a flavor (or type 'done' to finish): ")
    if flavor.lower() == 'done':
        break
    scoops = int(input("How many scoops did you have of this flavor::: "))

#representing the scoops and flavors of what they should be
    flavors[flavor] = scoops
    friends_flavors[friend_name] = flavors

#the total scoops which will be modified throughout the ending part of the code
total_scoops = 0

#all the scoops in total which will also be modified throughout the ending part of the code
all_scoops = []

#this part is the summary or basically the recipt for each person that went including yourself to the ice cream store
print("\n--- Summary ---")
for friend, flavors in friends_flavors.items():
    friend_total = sum(flavors.values())
    all_scoops.extend(flavors.values())
    total_scoops += friend_total
    average_scoops = statistics.mean(flavors.values())
    print(f"{friend} - Total scoops: {friend_total}, Average scoops per flavor: {average_scoops:.2f}")



#This is where all the overall calculations for the average amoun of scoops and all the scoops that everyone had in total is
overall_average = statistics.mean(all_scoops)
max_scoops = max(all_scoops)

#here is where we show the most popular flavor and other values
most_popular = [flavor for flavors in friends_flavors.values() for flavor, scoops in flavors.items() if scoops == max_scoops]

#here is the final recipt for in total how many scoops everyone had, the average scoops per flavor, and the most popular flavor out of all the people
print(f"\nOverall total scoops: {total_scoops}")
print(f"Overall average scoops per flavor: {overall_average:.2f}")
print("Most popular flavor(s): " + ", ".join(most_popular))