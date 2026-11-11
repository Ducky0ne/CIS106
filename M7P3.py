counter = 0
program = str(input("Do you want to run this program (Yes or No)? "))

print (program)

while program == "Yes":
    
    last_name = str(input("Please enter in last name: "))
    first_exam = int(input("Please enter in 1st exam score: "))
    second_exam = int(input("Please enter in 2nd exam score: "))
    average = (first_exam + second_exam) / 2
    number_of_times_program_has_ran = counter

    counter = counter +1

    print (last_name)
    print (first_exam)
    print (second_exam)
    print()
    print (last_name, ", Your average is:", average)
    
    program = str(input("Do you want to run this program (Yes or No)? "))
print ("Number of students who ran program: ", counter)