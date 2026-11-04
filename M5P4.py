name_of_appliance = str(input ("Please enter in name of appliance: ")) 
cost_of_appliance = float(input("Please enter in the cost of the appliance: $"))

if cost_of_appliance > 1000:
    warranty = (cost_of_appliance * .10) 
else:
    warranty = (cost_of_appliance * .05)

total = (cost_of_appliance + warranty)

print()

print ("Name of applicance", name_of_appliance)
print ("Cost of appliance", cost_of_appliance)
print (f"Warranty: ${warranty:.2f}")
print (f"Your total is: ${total:.2f}")