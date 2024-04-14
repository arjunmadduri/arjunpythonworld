#dictionary for appliance and rating
#dictionary for slab rates

import math

def energy_usage(appliances_usage):
    power_ratings = {
        "light": 4,
        "tv": 25,
        "fridge": 45,
        "fan": 15,
        "computer": 75
    }
   
    daily_usage = sum(appliance['quantity']*appliance['time']*power_ratings[appliance['appliance']] / 1000 for appliance in appliances_usage)
    monthly_usage = daily_usage * 30
    #return monthly_usage

    if monthly_usage <= 100:
        bill = monthly_usage*0.7
    if monthly_usage > 100:
        bill = monthly_usage * 1.6
    return monthly_usage, bill

appliances_usage = []
appliances=['light', 'tv', 'fridge', 'fan', 'computer']
for appliance in appliances:
    quantity = int(input(f"Enter what quantitiy of the {appliance} you have:::"))
    time_length = float(input(f"Enter how many hours you use {appliance} :::"))
    appliances_usage.append({"appliance": appliance, "quantity":quantity,"time":time_length})

#print(appliances_usage)
print(f"Your Monthly Energy usage is", energy_usage(appliances_usage)) 