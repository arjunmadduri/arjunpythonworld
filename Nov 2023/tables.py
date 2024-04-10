num = int(input("Enter a number please?:"))
print("Table for the Number: ", num)
for i in range(1,11):
    result = num * i
    print(num , "X", i, "=", result)
    