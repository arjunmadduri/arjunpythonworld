# Ask for the State Code .  If OR, WA=10%, CA-6%, TX, 6%
# Ask for the Type Standard, Semi Luxury, Luxury

#Give Car Options

#Once the User Choose Car Option

#@Give the Price
# 3 inputs
# variab;es for prices

import math

car_prices = {
          "camry":29000,
          "sentra":25000,
          "elantra":31000,
          "rav4":40000,
          "sorento":50000,
          "paliside":55000,
          "corvette":65000,
          "mustang":75000,
          "modelx":90000
}             

TaxCode = {
     "TX":6,
     "OR":0,
     "WA":10,
     "CA":6
}


def Cartype(Type):
    ST = ['Camry','Sentra', 'Elantra']
    SL = ['Rav4','Sorento', 'Paliside']
    LX = ['Corvette', 'Mustang', 'ModelX']
    if Type=="ST":
          Choice = str(input("Choose From Camry, Sentra or Elantra::"))
    elif Type == "SL":
          Choice = str(input("Choice from Rav4, Sorento or Paliside::"))
    elif Type=="LX":
          Choice = str(input("Choice from Corvette, Mustang, ModelX::"))
    return Choice
           
def CarPricing(Choice,StateCode):
     Price_Car = int(car_prices.get(Choice.lower(),"Car Not available in DealerShip"))
     TaxPercent = int(TaxCode.get(StateCode.upper(),"Invalid State"))
     TotalPrice = Price_Car+(TaxPercent/100*Price_Car)
     return Price_Car,TaxPercent,TotalPrice

Statecode = str(input("Enter State Code from these Choices - OR,WA,CA,TX:"))
Type = str(input("Enter the Type of Car from ST,SL,LX:"))

if Type == "ST" or Type == "SL" or Type == "LX":
    CarChoice = Cartype(Type)
    print("You have Selected ", CarChoice)
    Pricing = str(input("Do you want to Price the Car::"))
    if Pricing=="Yes":
          MSRP,Tax,Total = CarPricing(CarChoice,Statecode)
          print("The MSRP of the Car you Choose was: ", MSRP)
          print("The Tax for the State of ", Statecode, "Is ", Tax)
          print("The Total Price of the Car ",Total)
    else:
         print("Thank you for Contacting the DealerShip for your Interest:")
else:
    print("Please Select Valid Choice")

#code is over