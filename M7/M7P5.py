sum_of_all_discounts = 0


program = str(input("Do you want to run this program (Yes or No)? "))

while program == "Yes":
    quantity = int(input("Please enter in quantity: "))
    price_of_item = float(input("Please enter in price of item: "))
    extended_price = quantity * price_of_item

    if extended_price > 10000:
        discount_amount = (extended_price * .25)
    else:
        discount_amount = (extended_price * .10)

    total = (extended_price - discount_amount)

    print (f"Extended Price: ${extended_price:.2f}")
    print (f"Discount amount: ${discount_amount:.2f}")
    print (f"Total: ${total:.2f}")

    sum_of_all_discounts += discount_amount

    program = str(input("Do you want to run this program (Yes or No)? "))

print (f"Sum of all discounts: ${sum_of_all_discounts:.2f}")