quantity = int(input("Please enter in the amount of widgets: "))

if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30

extended_price = quantity * price

tax_amount = float(extended_price * .07)

total = extended_price + tax_amount

print ("Extended Price: $", extended_price)
print (f"Tax Amount: ${tax_amount:.2f}")
print (f"Total: ${total:.2f}")