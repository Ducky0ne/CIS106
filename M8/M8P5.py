students = 0
sum_of_all_tuition = 0

f=open("M8/M8P5 Data File.txt", "r")

last_name = str(f.readline().rstrip('\n'))
while last_name != "":
    district_code = str(f.readline().rstrip('\n'))
    credits_taken = int(f.readline())

    if district_code == "I":
        tuition_owed = credits_taken * 250
    else:
        tuition_owed = credits_taken * 500
        
    print ("Last name: ", last_name)
    print ("Credits taken: ", credits_taken)
    print (f"Tuition owed: ${tuition_owed:.2f}")

    students += 1
    sum_of_all_tuition += tuition_owed

    last_name = str(f.readline().rstrip('\n'))

print (f"Total tuition owed: ${sum_of_all_tuition:.2f}")
print ("Number of students: ", students)