print ("Please enter in make of vehicle:")
make = str(input())

print ("Please enter in model of vehicle:")
model = str(input())

print ("Please enter in MSRP")
msrp = float(input())

print ("Please enter in discount percent")
discount_percent = float(input())

amount_off = msrp * discount_percent 
discounted_price = msrp - amount_off

print ("Make: ", make)
print ("Model: ", model)
print (f"MSRP: , {msrp:.2f}")
print (f"Discount Percent: , {discount_percent:.0f}")
print (f"Amount Off: , {amount_off:.2f}")
print (f"Discount Price: , {discount_price:.2f}")