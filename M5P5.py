user_last_name = str(input("Please enter in last name: "))
number_of_dependents = int(input("Please enter in number of dependents: "))
gross_income = float(input("Please enter in gross income: "))
adjusted_gross_income = gross_income - (number_of_dependents * 12000)

if adjusted_gross_income > 50000:
    tax_rate = .20
else:
    tax_rate = .10

income_tax = float(f"{tax_rate * adjusted_gross_income:.2f}")

if income_tax < 0:
    income_tax = 100

print ("Last Name: ", user_last_name)
print (f"Gross Income: ${gross_income:.2f}")
print ("Dependants: ", number_of_dependents)
print (f"Adjusted Gross Income: {adjusted_gross_income:.2f}")
print ("Income Tax: ", income_tax)