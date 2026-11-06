last_name = str(input("Please enter in last name: "))
salary = float(input("Please enter in salary: $"))
job_level =  int(input("Please enter in job level: "))

if job_level >=10:
    bonus_rate = .25
elif job_level >=5:
    bonus_rate = .20
else:
    bonus_rate = .10  

bonus = salary * bonus_rate

print ("Last Name: ", last_name)
print (f"Bonus: ${bonus:.2f}")