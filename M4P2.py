purchase_price_per_share = float(input("Please enter in price paid per share: $")) 
current_stock_price = float(input ("Please enter in current stock price: $"))
quantity_of_stock = int(input("Please enter in number of stocks owned: "))

value = float((current_stock_price - purchase_price_per_share)*quantity_of_stock)

print (f"The value of your account is: ${value:.2f}")

if value < 0: print ("You have lost money")