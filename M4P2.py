purchase_price_per_share = float(input("Please enter in price paid per share: $")) 
current_stock_price = float(input ("Please enter in current stock price: $"))
quantity_of_stock = int(input("Please enter in number of stocks owned: "))

value = float((purchase_price_per_share - current_stock_price)*quantity_of_stock)

print ("")