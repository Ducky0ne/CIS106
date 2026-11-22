number_of_entries_made = 0
run_program = str(input("Would you like to run this program (Yes / No)? "))

while run_program == 'Yes':
        
    def get_input ():
        destination_city = str(input("Please enter in destination city: "))
        miles_travelled = float(input("Please enter in miles travelled: "))
        gallons_used = int(input("Please enter in gallons used: "))
        return (destination_city, miles_travelled, gallons_used)

    def miles_per_gallon (miles_travelled, gallons_used):
        MPG = float(miles_travelled / gallons_used)
        return (MPG)

    def main ():
        (destination_city, miles_travelled, gallons_used) = get_input ()
        MPG = miles_per_gallon (miles_travelled, gallons_used)

        print ("Destination City: ", destination_city)
        print (f"Miles Travlled: {miles_travelled:.2f}")
        print (f"Miles Per Gallon (MPG): {MPG:.2f}")
        return (MPG)
    MPG = main ()

    number_of_entries_made += 1
    run_program = str(input("Would you like to run this program (Yes / No)? "))

print ("Number of entries made: ", number_of_entries_made)