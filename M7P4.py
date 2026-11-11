counter = 0
sum_gross_pay = 0
program = str(input("Do you want to run this program (Yes or No)? "))

while program == "Yes":
    
    counter = counter + 1

    employee_last_name = str(input("Please enter in last name: "))
    hours_worked = int(input("Please enter in number of hours worked: "))
    rate_of_pay = float(input("Please enter in rate of pay: "))
    

    if hours_worked > 40:
        overtime_hours = (hours_worked - 40)
        gross_pay = (40 * rate_of_pay) + (overtime_hours * (1.5 * rate_of_pay))
    else:
        gross_pay = (hours_worked * rate_of_pay)
        
    sum_gross_pay += gross_pay

    print ("Employee Last Name: ", employee_last_name)
    print (f"Gross Pay: ${gross_pay:.2f}")
    print (f"Sum of all gross pays: ${sum_gross_pay:.2f}")
    print ("Number of employees who ran program: ", counter)
    
    program = str(input("Do you want to run this program (Yes or No)?"))