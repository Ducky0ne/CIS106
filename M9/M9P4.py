run_program = str(input("Do you want to run this program (Yes / No): "))
total_gross_pay = 0

while run_program == 'Yes':
    def get_input ():
        last_name = str(input("Please enter in last name: "))
        job_code = str(input("Please enter in job code (L, A, or J): "))
        while job_code != 'L' and job_code != 'A' and job_code != 'J':
            print ('Please enter in valid job code: ')
            job_code = str(input("Please enter in job code (L, A, or J): "))
        hours_worked = int(input("Please enter in hours worked: "))
        
        return (last_name, job_code, hours_worked)

    def rate_of_pay (job_code, hours_worked):
        if job_code == 'L' and hours_worked <= 40:
            pay_rate = (hours_worked * 25)
        elif job_code == 'L' and hours_worked > 40:
            pay_rate = ((hours_worked - 40) * (25 * 1.50))+ (40 * 25)        
        elif job_code == 'A' and hours_worked <= 40:
            pay_rate = (hours_worked * 30)
        elif job_code == 'A' and hours_worked > 40:
            pay_rate = ((hours_worked - 40) * (30 * 1.50))+ (40 * 30)        
        elif job_code == 'J' and hours_worked <= 40:
            pay_rate = (hours_worked * 50)
        elif job_code == 'J' and hours_worked > 40:
            pay_rate = ((hours_worked - 40) * (50 * 1.50))+ (40 * 50)
        return (pay_rate)

    def main ():
        (last_name, job_code, hours_worked) = get_input ()
        (pay_rate) = rate_of_pay (job_code, hours_worked)
        print ("Last Name:", last_name)
        print ("Gross Pay: $", pay_rate)
        return (pay_rate)
    pay_rate = main ()

    total_gross_pay += pay_rate
    run_program = str(input("Do you want to run this program (Yes / No): "))