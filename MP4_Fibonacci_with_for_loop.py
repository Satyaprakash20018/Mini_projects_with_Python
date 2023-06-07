"""
The fibonacci series is a sequence of number where the first two numbers are 0 and 1 then the next numbers will be the
sum of previous two numbers.
Ex: 0 1 1 2 3 5 8 13 21 34 ....
"""

First_number = int(input("Enter the First number: "))
Second_number = int(input("Enter the Second number: "))
Fib_number = int(input("Enter the number of Fibonacci series to be print: "))
sum = 0
print(First_number, end=" ")
print(Second_number, end=" ")

for i in range(Fib_number+1):
    sum = First_number + Second_number
    First_number = Second_number
    Second_number = sum
    print(sum, end=" ")
