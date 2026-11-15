year = 1
total_interest_earned = 0

beginning_balance = float(input("Please enter in principal amount: "))
annual_interest = float(input("Please enter in annual interest as a decimal: "))
ending_balance = (beginning_balance * annual_interest) + (beginning_balance)
total_interest_earned += (beginning_balance * annual_interest)

print (f'{"Year":10} {"Beginning Balance":25} {"Ending Balance":25}')
print (f'{year} {beginning_balance:25.2f} {ending_balance:25.2f}')

while year < 5:  

    beginning_balance = ending_balance
    ending_balance = (beginning_balance * annual_interest) + (beginning_balance)
    total_interest_earned += (beginning_balance * annual_interest)

    year = year +1
    
    print (f'{"Year":10} {"Beginning Balance":25} {"Ending Balance":25}')
    print (f'{year} {beginning_balance:25.2f} {ending_balance:25.2f}')

print (f"Total Interest Earned: ${total_interest_earned:.2f}")