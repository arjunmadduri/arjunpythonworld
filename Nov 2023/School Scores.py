#Variable for students and subjects
intro = ("Welcome to the fun grading system!")
students = int(input("How many students are in your class: "))
subjects = int(input("How many subjects do you have in your class: "))
studentmarks = []
#for loop
for i in range (students):
#variable for marks
    marks = []
    print (f"student {i+1}")
#nested loop
    for j in range (subjects):
#variable for mark
        mark = int(input(f"Enter marks for subject {j+1}:"))
#functions for code
        marks.append(mark)
    studentmarks.append(marks)
def calculate(studentmarks):
#other functions for the code
    averages = []
    for marks in studentmarks:
        average = sum(marks)/len(marks)
        averages.append(average)
    return averages
#variables for average marks and print statements
averagemarks = calculate(studentmarks)
for i,avg in enumerate(averagemarks):
    print (f"Average marks for student: {i+1}is{avg}")
#Variable for students and subjects
students = int(input("How many students are in your class: "))
subjects = int(input("How many subjects do you have in your class: "))
studentmarks = []