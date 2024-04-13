#importing libraries of functions to make this code easier with built in functions with out having to create formulas with math
import math
import time
#function that stores all the dictonaries and outputs 
def calorie_counter(excercise,terrain,duration):
    #dictonary for holding possible excercise and terrain
    calorie_chart = {
        "running": {"flat": 10, "hilly": 15, "mountain":20},
        "biking": {"flat": 15, "hilly": 20, "mountain":25},
        "cycling": {"flat": 20, "hilly": 25, "mountain":30}
    }
    #if condition for saying excercise or terrain is not in dictonary
    if excercise not in calorie_chart or terrain not in calorie_chart[excercise]:
        print ("Invlaid input please retry and add a valid input:::")
        return
    #variables for giving output of how many calories burned
    calorie_per_minute = calorie_chart[excercise][terrain]
    calories_burned = calorie_per_minute*duration
    return calories_burned
#inputs for user
excercise = str(input("Enter what excercise you are doing, [ running, biking, cycling] :::")).lower()
terrain = str(input("Enter what terrain you are going to do your excercise in, [ flat, hilly, mountain] :::")).lower()
duration = int(input("Enter what the duration will be for the excercise:::"))
#output of how many calories burned by using print and calling the function to give the final result
print("The Amount of Calories Burned in this Session",calorie_counter(excercise,terrain,duration))