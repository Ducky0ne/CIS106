run_program = str(input("Do you want to run this program (Yes / No): "))

while run_program == "Yes":
    def get_input ():
        last_name = str(input("Please enter in last name: "))
        month = str(input("Please enter in month (e.g. Jan, Feb, Mar, etc): "))
        sales = float(input("Please enter in sales: "))
        return (last_name, month, sales)

    def forecast (month, sales):
        if month == 'Jan' or month == 'Feb' or month == 'Mar':
            next_months_forecast = (sales * 1.10)
        elif month == 'Apr' or month == 'May' or month == 'Jun':
            next_months_forecast = (sales * 1.15)
        elif month == 'Jul' or month == 'Aug' or month == 'Sep':
            next_months_forecast = (sales * 1.20)  
        elif month == 'Oct' or month == 'Nov' or month == 'Dec':
            next_months_forecast = (sales * 1.25)
        return (next_months_forecast)

    def main ():
        (last_name, month, sales) = get_input ()
        (next_months_forecast) = forecast (month, sales)
        return (next_months_forecast)
    (next_months_forecast) = main ()

    print (f"Next month's forecast: ${next_months_forecast:.2f}")
    run_program = str(input("Do you want to run this program (Yes / No): "))