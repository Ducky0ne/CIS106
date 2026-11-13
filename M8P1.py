year = 1

beginning_balance = float(input("Please enter in principal amount: "))
annual_interest = float(input("Please enter in annual interest as a decimal: "))
ending_balance = (beginning_balance * annual_interest) + (beginning_balance)

print ("Year", year)
print (f"Beginning Balance {beginning_balance:.2f}")
print (f"Ending Balance {ending_balance:.2f}")

while year < 5:  

    beginning_balance = ending_balance
    ending_balance = (beginning_balance * annual_interest) + (beginning_balance)

    year = year +1

    print ("Year", year)
    print (f"Beginning Balance {beginning_balance:.2f}")
    print (f"Ending Balance {ending_balance:.2f}")