#import library

import math

#function for calculating bills and how long electricity was turned on 
def energy_usage(appliances_usage):
    power_ratings = {
        "light": 4,
        "tv": 25,
        "fridge": 45,
        "fan": 15,
        "computer": 75
    }
#formula for calculating how long used
    daily_usage = sum(appliance['quantity']*appliance['time']*power_ratings[appliance['appliance']] / 1000 for appliance in appliances_usage)
    monthly_usage = daily_usage * 30
    
#if condition for calculating bills for electricity
    if monthly_usage <= 100:
        bill = monthly_usage*0.7
    if monthly_usage > 100:
        bill = monthly_usage * 1.6
    return monthly_usage, bill
#array for storing different appliances usage
appliances_usage = []
appliances=['light', 'tv', 'fridge', 'fan', 'computer']
#for loop to go through and capture each appliance usage
for appliance in appliances:
    quantity = int(input(f"Enter what quantitiy of the {appliance} you have:::"))
    time_length = float(input(f"Enter how many hours you use {appliance} :::"))
#if condition for saying if the user says anything over 24 for the time_length it will turn into 24 because a day has 24 hours
    if time_length > 24:
        time_length = 24
#filling the array with the values from the input in the variables
    appliances_usage.append({"appliance": appliance, "quantity":quantity,"time":time_length})

#printing final result by calling the function that we used earlier
print(f"Your Monthly Energy usage is", energy_usage(appliances_usage))  