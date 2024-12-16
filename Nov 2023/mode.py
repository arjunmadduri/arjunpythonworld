import statistics
number = []
number_amount = int(input("Enter how many number do you want to enter::: "))
for i in range(number_amount):
    numbers = int(input("Enter a number::: "))
    number.append(numbers)
print(number)
mode = statistics.mode(number)
print(mode)
multimode = statistics.multimode(number)
print(multimode)





import statistics

friends_flavors = {}

friends_amount = int(input("How many people are going to the ice cream store::: "))

for i in range(friends_amount):
    friend_name = input(f"\nEnter the name of your friend or yourself {i+1}::: ")
    flavor = {}
    print(f"{friend_name} what flavor of ice cream did you eat::: ")

while True:
    flavors = str(input("Please enter the flavor you ate or type in 'done' to finish::: "))
    if flavors.lower == "done":
        break
    scoops = int(input("How many scoops did you have of thise flavor"))
    
    flavor[flavors] = scoops
    friends_flavors[friend_name] = flavors

total_scoops = 0
all_scoops = []

print("\n--- Summary ---")
for friend, flavors in friends_flavors.items():
    friend_total = sum(flavors.values())
    all_scoops.extend(flavors.values())
    total_scoops += friend_total
    average_scoops = statistics.mean(flavors.values())
    print(f"{friend} - Total scoops: {friend_total}, Average scoops per flavor: {average_scoops}")
