print ("Please enter in total amount received for competed job")
completed_job_fee = int(input())

amount_per_person = completed_job_fee / 3

print (f"Employee 1: ${amount_per_person:.2f}")
print (f"Employee 2: ${amount_per_person:.2f}")
print (f"Employee 3: ${amount_per_person:.2f}")