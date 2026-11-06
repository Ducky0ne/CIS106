number_of_concert_tickets = int(input("Please enter in the number of concert tickets: "))

if number_of_concert_tickets >=25:
    price_per_ticket = 50
elif number_of_concert_tickets >=10:
    price_per_ticket = 60
elif number_of_concert_tickets >=5:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = number_of_concert_tickets * price_per_ticket

print ("Number of tickets: ", number_of_concert_tickets)
print ("Price per ticket: $", price_per_ticket)
print ("Total Cost: $", total_cost)