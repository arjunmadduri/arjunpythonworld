import time
# current_time = time.time()
# print(current_time)
starting_time = time.time()
for i in range(1000):
    print("something")

ending_time = time.time()
total_time = ending_time-starting_time
result = total_time
print(result)