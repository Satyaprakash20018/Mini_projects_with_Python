"""
 An Armstrong number is a number which is equal to the sum of the digits raised to the power of number of digits.
 Ex: 153:
     no. of digits = 3
     1**3 + 5**3 + 3**3 = 1 + 125 +27 = 153
     so, it's an armstrong number 
"""
#  init

n = int(input("Enter the number to check for Armstrong: "))
res = n
l = len(str(n))  # as len() function is only applicable to strings
sum = 0

while n > 0:
    dig = n%10
    sum = sum + dig**l
    n = n//10

if sum == res:
    print(res, " is An Armstrong number")
else:
    print(res, " is not An Armstrong number")

