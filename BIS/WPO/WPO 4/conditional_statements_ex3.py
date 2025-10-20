"""
VAT

Depending on where an individual is from, Amazon needs to tax them 
appropriately. 

Belgium          21
Germany          19
France           20
The Netherlands  21
"""

country = "Belgium"
purchase_amount = 20.00

if country == "Belgium" or "The Netherlands":
    tax_amount = .21
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(country, total_cost)
elif country == "France":
    tax_amount = .20
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(country, total_cost)
elif country == "Germany":
    tax_amount = .19
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(country, total_cost)

print(result)