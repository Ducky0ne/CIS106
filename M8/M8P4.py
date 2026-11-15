count = 0
sum_of_extended_prices = 0

f = open("M8P4 Data File.txt", "r")

item = str(f.readline().rstrip('\n'))
while item != "":
    quantity = int(f.readline())
    price = float(f.readline())
    extended_price = quantity * price

    print ("Item: ", item)
    print ("Quantity: ", quantity)
    print (f"Price: ${price:.2f}")
    print (f"Extended Price: ${extended_price:.2f}")

    count = count + 1
    sum_of_extended_prices += extended_price

    item = str(f.readline().rstrip('\n'))

average_order = sum_of_extended_prices / count

print (f"Sum of all extended prices: ${sum_of_extended_prices:.2f}")
print ("Number of orders: ", count)
print (f"Average order: ${average_order:.2f}")