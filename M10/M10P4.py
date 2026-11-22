run_program = str(input("Do you want to run this program (Yes / No): "))
sum_of_all_tickets = 0

while run_program == 'Yes':
    def get_input ():
        last_name = str(input("Please enter in last name: "))
        miles_from_Chicago = int(input("Please enter in miles from downtown Chicago: "))
        return (last_name, miles_from_Chicago)

    def ticket_price (miles_from_Chicago):
        if miles_from_Chicago >=30:
            price = 12
        elif miles_from_Chicago >=20:
            price = 10
        elif miles_from_Chicago >=10:
            price = 8
        else:
            price = 5
        return (price)

    def main ():
        (last_name, miles_from_Chicago) = get_input ()
        (price) = ticket_price (miles_from_Chicago)
        print (f"Your ticket price is: ${price:.2f}")
        return (price)
    (price) = main ()

    sum_of_all_tickets += price
    run_program = str(input("Do you want to run this program (Yes / No): "))
print (f"Sum of all tickets sold: ${sum_of_all_tickets:.2f}")