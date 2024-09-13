amount = int(input("Enter the amount you need::: "))
interest = float(input("Please enter the interest rate::: "))
time = int(input("Please enter the total time for how long you need this loan(in years only)::: "))
simple_interest = amount*interest*time/100
print(simple_interest)