total_meal_cost = float(input("Please enter in the total cost of the meal: $"))
print ()

low_tip = float(total_meal_cost * .15)
mid_tip = float(total_meal_cost * .18)
high_tip = float(total_meal_cost * .20)

low_total_with_tip = float(total_meal_cost + low_tip)
mid_total_with_tip = float(total_meal_cost + mid_tip)
high_total_with_tip = float(total_meal_cost + high_tip)

print ("15% Tip")
print (f"Total: ${total_meal_cost:.2f}")
print (f"Tip: ${low_tip:.2f}")
print (f"Total with tip: ${low_total_with_tip:.2f}")
print ()

print ("18% Tip")
print (f"Total: ${total_meal_cost:.2f}")
print (f"Tip: ${mid_tip:.2f}")
print (f"Total with tip: ${mid_total_with_tip:.2f}")
print ()

print ("20% Tip")
print (f"Total: ${total_meal_cost:.2f}")
print (f"Tip: ${high_tip:.2f}")
print (f"Total with tip: ${high_total_with_tip:.2f}")