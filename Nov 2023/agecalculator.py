# Rakshita wants to calculate her age. So she subtracted her year of birth from the current year.
#  Her classmates also wanted to find their age in the same way. So she decides to write a python program where students can input their year of birth,
#  then the program will print their age. Write the same program to find your age and help your classmates in finding their age]2014


def age_calculation(birthyear_input,presentyear_input):
    if birthyear_input < 1924 or birthyear_input > 2024:
        print("Invalid Birthyear:::")
    elif birthyear_input >= 1924:
        result = presentyear_input-birthyear_input
        print(result," Years Old")

birthyear_input = int(input("Enter the year you were born::: "))
presentyear_input = int(input("Enter the present year::: "))

age_calculation(birthyear_input,presentyear_input)