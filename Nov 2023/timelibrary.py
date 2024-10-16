# import time
# # current_time = time.time()
# # print(current_time)
# starting_time = time.time()
# for i in range(345000):
#     print("ola amigos")

# ending_time = time.time()
# total_time = ending_time-starting_time
# result = total_time
# print(result)

#pytz library
#from pytz import all_timezones
#print(all_timezones)
#'US/Pacific'
from pytz import timezone
from datetime import datetime
current_time = datetime.now(timezone('US/Pacific'))
print(current_time)