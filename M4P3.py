total_meal_cost = float(input("Please enter in the total cost of the meal: $"))

low_tip = float(total_meal_cost * .15)
mid_tip = float(total_meal_cost * .18)
high_tip = float(total_meal_cost * .20)

low_total_with_tip = float(total_meal_cost + low_tip)
mid_total_with_tip = float(total_meal_cost + mid_tip)
high_total_with_tip = float(total_meal_cost + high_tip)

print (float("Total: $", total_meal_cost))
print (float("Tip: $", low_tip))
print (float("Total with tip: $", low_total_with_tip))