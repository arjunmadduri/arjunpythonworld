# 
# The fibonacci sequence is a series of numbers in which each number is the sum of the two that precede it. Starting at 0 and 1, the sequence looks like this:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
# and so on forever.Arvind is very interested to know the 100th term of the Fibonacci series.
# He was adding the values manually in a calculator but it was taking so much time for him to find any term of the Fibonacci series.
# To help Arvind write a program that can print nth term of the Fibonacci series where n is the given term by the user.
# Also, write the entire program inside a loop so that the user can use the program multiple times without running the program again and again

n1 = 0
n2 = 1
n = int(input("how many numbers of the fibonacci series::: "))
if n == 1:
    print(n1)
elif n == 2:
    print(n1)
    print(n2)
elif n > 2:
    print(n1)
    print(n2)
    for i in range(n-2):
        n3 = n1+n2
        n1 = n2 
        n2 = n3
        print(n3)
