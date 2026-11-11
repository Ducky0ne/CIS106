sum_of_all_discounts = 0

program = str(input("Do you want to run this program (Yes or No)? "))

while program == "Yes":
    quantity = int(input("Please enter in quantity: "))
    price_of_item = float(input("Please enter in price of item: "))
    extended_price = quantity * price_of_item

    if extended_price > 10000:
        extended_price * .25
    else:
        extended_price * .10

    sum_of_all_discounts += extended_price
    
    print

