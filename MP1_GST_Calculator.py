"""
We all buy various Goods from a store. Along with the price of goods we wish to buy, we also have to pay an additional
tax, which is calculated as a specific % on the total price. This is called GST on the products.
The GST has two components: CGST(ex. @9%) and SGST(ex. @9%) and the overall cost of the product will be the aggregate of
original costs and the GST costs.
Formula to calculate the Total cost is :
            Org_Cost + CGST on product + SGST on product
"""

CP = float(input("Enter the original cost of the product: "))
CGST = float(input("Enter the central GST of the product: "))
SGST = float(input("Enter the state GST of the product: "))

COST = CP + ((CGST/100) * CP) + ((SGST/100) * CP)

print("The final cost of the product is : ", format(COST, ".2f"))  # format() is used to print 2 digit after decimal
