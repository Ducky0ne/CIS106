number_of_books = int(input("Please enter in the number of books: "))
cost_per_book =  float(input("Please inut the cost per book: "))
order_total = float(number_of_books * cost_per_book)

if order_total > 50:
    shipping_charge = 0 
else:
    shipping_charge = 25 

print (f"Your order total is: ${order_total:.2f}")
print (f"Shipping Charge: {shipping_charge:.2f}")