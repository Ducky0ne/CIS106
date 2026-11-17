run_program = str(input("Do you want to run this program (Yes / No): "))
total_extended_price = 0

while run_program == 'Yes':

    def get_input():
        quantity = int(input("Please enter in quantity; "))
        unit_price = float(input("Please enter in unit price: "))
        return (quantity, unit_price)

    def calculate_total (quantity, unit_price):
        total = quantity * unit_price

        if total > 10000:
            total = total *.90
        return(total)

    def main ():
        (quantity, unit_price) = get_input()
        total = calculate_total(quantity, unit_price)
        print ("Quantity:", quantity)
        print (f"Price: ${unit_price:.2f}")
        print (f"Total: ${total:.2f}" )
        return (total)
        
    total = main()

    total_extended_price += total

    run_program = str(input("Do you want to run this program (Yes / No): "))

print (f"Total Extended Price: ${total_extended_price:.2f}")