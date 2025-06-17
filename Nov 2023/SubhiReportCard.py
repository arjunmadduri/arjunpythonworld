# Now that Subhi has received a general idea of the percentage of marks she has scored,
#  she wants to check if the marks are graded or not. Check the marks for each subject and grade the subjects accordingly.
#  Pass greater than 50 and Fail is lesser than 50.
# Using print statements display a report card for the following program displaying the marks in every subject,
#  their respective grade. Also display the percentage of marks calculated.
# Use print statements to make the program visually appealing.

print("Subhi report card")
math = int(input("How many marks did you get on math::: "))
reading = int(input("How many marks did you get on reading::: "))
history = int(input("How many marks did you get on history::: "))
science = int(input("How many marks did you get on science::: "))
writing = int(input("How many marks did you get on writing::: "))
def Math():
    if math >=50:
        print("Math Pass",math)
    elif math <50:
        print("Math Fail",math)
    else:
        print("Invalid test score, please try again")
def Reading():
    if reading >=50:
        print("Reading Pass",reading)
    elif reading <50:
        print("Reading Fail",reading)
    else:
        print("Invalid test score, please try again")
def History():
    if history >=50:
        print("History Pass",history)
    elif history <50:
        print("History Fail",history)
    else:
        print("Invalid test score, please try again")
def Science():
    if science >=50:
        print("Science Pass",science)
    elif science <50:
        print("Science Fail",science)
    else:
        print("Invalid test score, please try again")
def Writing():
    if writing >=50:
        print("Writing Pass",writing)
    elif writing <50:
        print("Writing Fail",writing)
    else:
        print("Invalid test score, please try again")
total = math+reading+history+science+writing
percantage = total/5
highest= 500
print("Total marks",total,"out of",highest)
print(percantage)
Math()   
Reading()
History()
Science()
Writing()