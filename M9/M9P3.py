number_of_entries_made = 0
run_program = str(input("Would you like to run this program (Yes / No)? "))

while run_program == 'Yes':
        
    def get_input ():
        destination_city = str(input("Please enter in destination city: "))
        miles_travelled = float(input("Please enter in miles travelled: "))
        gallons_used = int(input("Please enter in gallons used: "))
        return (destination_city, miles_travelled, gallons_used)

    def miles_per_gallon (miles_travelled, gallons_used):
        MPG = (miles_travelled / gallons_used)
        return (MPG)

    def main ():
        (destination_city, miles_travelled, gallons_used) = get_input ()
        miles_per_gallon (miles_travelled, gallons_used) - main ()

        print ("Destination City: ", destination_city)
        print (f"Miles Travlled: {miles_travelled:.2f}")
        print ("Miles Per Gallon (MPG): ", mpg)

        number_of_entries_made += 1

        return (MPG)

    run_program = str(input("Would you like to run this program (Yes / No)? "))

print ("Number of entries made: ", number_of_entries_made)