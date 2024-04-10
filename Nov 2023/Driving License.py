#create a variable recommended_age and store 18 in it



#take inputs from the user like his name, age, emailId, phone number, address



#write a print statement saying "We have received your registration form, below are the details you entered kindly verify once again and wait for us to verify if you are eligible for Driving License or not."



#print each user detail in each new line



#write a if condition to check if the user_age is greater than or equal to (>=) 18 or not. If it is greater than 18 then print 



recommended_age = 18
a=str(input("what is your name?: "))
b=int(input("what is your age?: "))
c=str(input("what is your email id?:"))
d=float(input("what is your phone number?: "))
e=str(input("what is your address?: "))
print(a)
print(b)
print(c)
print(d)
print(e)
if b>=recommended_age:
    print("Hooray!!, You are eligible for your Driving License!:)")
elif b<recommended_age:
    print("Sorry,you are not old enough to get your Driving License.:(")