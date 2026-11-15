fixed_costs = float(input("Please enter in your fixed costs: "))
price_per_unit = float(input("Please enter in price per unit: "))
cost_per_unit = float(input("Please enter in cost per unit: "))
break_even = int(fixed_costs / (price_per_unit - cost_per_unit))

print ("Your break even point is:", break_even, "units")