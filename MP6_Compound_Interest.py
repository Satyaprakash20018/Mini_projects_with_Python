"""

Write a program to calculate compound interest for principal amount as Rs.10000 at rate of interest at 5% and number of
years the amount is deposited as 7 years.

"""


def compound_interest(p, x, n):
    print('StartingBalance\t', '\tInterest\t', '\tEnding Balance\t', '\tYear')
    r = x / 100
    tot = 0
    for i in range(1, n + 1):
        s_new = p * (1 + r) ** i - p
        s_old = p * (1 + r) ** (i - 1) - p
        tot = tot + (s_new - s_old)
        if i == 1:
            print("{0:.2f}\t".format(p), end="")
            print("\t\t{0:.2f}\t".format(s_new - s_old), end="")
            print("\t\t{0:.2f}\t".format(s_new + p), end='\t\t')
            print(i)
        else:
            print("{0:.2f}\t".format(p + s_old), end="")
            print("\t\t{0:.2f}\t".format(s_new - s_old), end="")
            print("\t\t{0:.2f}\t".format(s_new + p), end="\t\t")
            print(i)
    print("\nTotal interest deposited Rs. {0:.2f}".format(tot))


p = eval(input("Enter the amount of Principal"))
x = eval(input("Enter the Rate of Interest"))
n = eval(input("Enter number of year"))
compound_interest(p, x, n)
