# Number of days in a Month
print("This program will print the number of days in a given Month")
# init
flag = 1  # Assuming that the user input a valid number(1-12)
# Get the number of month from the user
n = int(input("Enter the number of the Month: "))

if n == 2:  # For the month of February
    y = int(input("Enter the year: "))
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):  # To check for leap year
        num_days = 29
    else:
        num_days = 28

elif n in (1, 3, 5, 7, 8, 10, 12):
    num_days = 31

elif n in (4, 6, 9, 11):
    num_days = 30

else:
    print("Number of the month should be in between 1 to 12")
    flag = 0

if flag == 1:
    print("The number of days are ", num_days, " in the ",n," Month")
