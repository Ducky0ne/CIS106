# This program converts an input Fahrenheit temperature to Celsius.

# print("Enter Fahrenheit temperature:")
# fahrenheit = float(input())

# celsius = (fahrenheit - 32) * 5 / 9

# print(str(fahrenheit) + "° Fahrenheit is " + str(celsius) + "° Celsius")

# print(f"the value of c is {c:10.2f} {units}.”)



print ("Please enter in the ticker symbol: ")
ticker_symbol = str(input())

print ("Please enter in the number of shares: ")
number_of_shares = int(input())

print ("Please enter in the cost per share: $")
cost_per_share = float(input())

amount_invested = number_of_shares * cost_per_share

print (f"Amount Invested = ${amount_invested:.2f}")