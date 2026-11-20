run_program = str(input("Do you want to run this program (Yes / No):"))
sum_of_all_car_sales = 0
sum_of_all_msrp = 0

while run_program == 'Yes':
    def get_input ():
        make = str(input("Please enter in make of car: "))
        model = str (input("Please enter in model of car: "))
        electric_vehicle_code = str(input("Please enter in electric vehicle code(Y / N): "))
        msrp_sticker_price = float(input("Please enter in MSRP: "))
        return (make, model, electric_vehicle_code, msrp_sticker_price)

    def out_the_door_price (make, model, electric_vehicle_code, msrp_sticker_price):
        if electric_vehicle_code == 'Y':
            cost_of_vehicle = (msrp_sticker_price * .70) + ((msrp_sticker_price * .70)*.07)
        elif make == 'Honda' and model == 'Accord':
            cost_of_vehicle = (msrp_sticker_price * .90) + ((msrp_sticker_price * .90)*.07)
        elif make == 'Toyota' and model == 'Rav4':
            cost_of_vehicle = (msrp_sticker_price * .85) + ((msrp_sticker_price * .85)*.07)
        else:
            cost_of_vehicle = (msrp_sticker_price * .95)  + ((msrp_sticker_price * .95)*.07)
        return (cost_of_vehicle)

    def main ():
        (make, model, electric_vehicle_code, msrp_sticker_price) = get_input ()
        (cost_of_vehicle) = out_the_door_price (make, model, electric_vehicle_code, msrp_sticker_price)    
        print (f"Cost of vehicle: ${cost_of_vehicle:.2f}")
        return (cost_of_vehicle, msrp_sticker_price)
    (cost_of_vehicle, msrp_sticker_price) = main ()

    sum_of_all_car_sales += cost_of_vehicle
    sum_of_all_msrp += msrp_sticker_price

    run_program = str(input("Do you want to run this program (Yes / No):"))
    print (f"Sum of all car sales: ${sum_of_all_car_sales:.2f}")
    print (f"Sum of all MSRP: ${sum_of_all_msrp:.2f}")