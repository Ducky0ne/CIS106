principle_amount_of_CD = int(input("Please enter in the principal amount of the CD: "))
year_to_maturity = int(input("Please enter in years to maturity: "))

if principle_amount_of_CD >100000 and year_to_maturity == 5:
    interest_rate = .06	 
elif principle_amount_of_CD >=50000 and year_to_maturity == 10:
    interest_rate = .05
elif principle_amount_of_CD >= 50000 and year_to_maturity == 5:
    interest_rate = .04 
else:
    interest_rate = .02

first_year_interest = principle_amount_of_CD * interest_rate

print ("Principle: $", principle_amount_of_CD)
print ("Interest Rate: ", (interest_rate * 100), "%")
print (f"1st year interest amount: ${first_year_interest:.2f}")