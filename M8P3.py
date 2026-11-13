f = open("M8P3 Data File.txt", "r")
sum_of_all_bonus = 0
name = str(f.readline().rstrip('\n'))

while name != "":
    salary = float(f.readline())

    if salary >=100000:
        bonus = (salary * .20)
    elif salary >= 50000:
        bonus = (salary * .15)
    else:
        bonus = (salary * .10)

    sum_of_all_bonus += bonus

    print ("Name: ", name)
    print (f"Salary: ${salary:.2f}")
    print (f"Bonus: ${bonus:.2f}")

    name = str(f.readline().rstrip('\n'))

print (f"Sum of all bonuses: ${sum_of_all_bonus:.2f}")
