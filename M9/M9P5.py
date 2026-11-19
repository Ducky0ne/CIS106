run_program = str(input("Do you want to run this program (Yes / No): "))
all_tuition_owed = 0

while run_program == 'Yes':
    def get_input ():
        last_name = str(input("Please enter in student's last name: "))
        credit_hours = int(input("Please enter in number of credit hours: "))
        district_code = str(input("Please enter in district code (I/O): "))
        return (last_name,credit_hours,district_code)

    def tuition_calculation (credit_hours, district_code):
        if district_code == 'I':
            tuition_owed = (credit_hours * 250)
        elif district_code == 'O':
            tuition_owed = (credit_hours * 550)
        return (tuition_owed)

    def main ():
        (last_name, credit_hours, district_code) = get_input ()
        (tuition_owed) = tuition_calculation
        print ("Student Name: ", last_name)
        print ("Tuition Owed: ", tuition_owed)
        return (tuition_owed)
        tuition_owed = main ()

all_tuition_owed += tuition_owed
run_program = str(input("Do you want to run this program (Yes / No): "))