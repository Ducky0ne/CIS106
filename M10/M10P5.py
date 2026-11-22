run_program = str(input("Do you want to run this program (Yes / No): "))
sum_of_all_market_values = 0
sum_of_all_assessed_values = 0

while run_program == 'Yes':
    def get_input ():
        county = str(input("Plese enter in county: "))
        market_value = float(input("Please enter in market value of home: "))
        return (county, market_value)

    def value (county, market_value):
        if county == 'Cook':
            assessed_value = (market_value * .90)
        elif county == 'DuPage':
            assessed_value = (market_value * .80)
        elif county == 'McHenry':
            assessed_value = (market_value * .75)
        elif county == 'Kane':
            assessed_value = (market_value * .60)
        else:
            assessed_value = (market_value * .70)
        return (assessed_value)

    def main ():
        (county, market_value) = get_input ()
        (assessed_value) = value (county, market_value)
        print (f"Your homes assessed value is ${assessed_value:.2f}")
        return (market_value, assessed_value)
    (market_value, assessed_value) = main ()

    sum_of_all_market_values += market_value
    sum_of_all_assessed_values += assessed_value

    run_program = str(input("Do you want to run this program (Yes / No): "))

print (f"Sum of all market value: ${sum_of_all_market_values:.2f}")
print (f"Sum of all assessed value: ${sum_of_all_assessed_values:.2f}")