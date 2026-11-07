item = str(input("Please enter in item: "))
quantity =  int(input("Please enter in quantity: "))

if item == 'A' or item == 'a': 
    unit_price = 10.00 
else: 
    unit_price = 20.00

extended_price = quantity * unit_price

print ("Item: ", item) 
print (f"Unit Price: ${unit_price:.2f}") 
print (f"Extended Price: ${extended_price:.2f}")