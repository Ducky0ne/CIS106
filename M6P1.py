quantity = int(input("Please enter in the amount of widgets: "))

if quantity > 10000:
    price = 10
elif quantity >= 5000 and quantity <=10000:
    price = 20
else:
    price = 30

print (quantity)
print (price)