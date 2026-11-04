user_last_name = str(input("Please enter in last name: "))
number_of_dependents = int(input("Please enter in number of dependents: "))
gross_income = float(input("Please enter in gross income: "))




# Adjusted gross incomes over $50,000 have a tax rate of 20%. Adjusted gross incomes $50,000 or under have a tax rate of 10%. 
# Once you determine the tax rate, compute income tax to be adjusted gross income times tax rate. If the income tax is less than 0, set the income tax to $100.


adjusted_gross_income = gross_income - (number_of_dependents * 12000) 
income_tax = tax_rate * adjusted_gross_income 



