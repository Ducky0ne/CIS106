run_program = str(input("Do you want to run this program (Yes / No): "))

while run_program == 'Yes':
    def get_input ():
        length = float(input("Please enter in the length of the room: "))
        width = float(input("Please enter in the width of the room: "))
        height = float (input("Please enter in the height of the room: "))
        return (length, width, height)

    def gallons (length, width, height):
        wall_square_footage = 2*(length * height) + 2 * (width * height)
        gallons_needed = wall_square_footage / 50
        return (wall_square_footage, gallons_needed)

    def main ():
        (length, width, height) = get_input ()
        (wall_square_footage, gallons_needed) = gallons (length, width, height)
        return (gallons_needed)
    gallons_needed = main ()

    print ("Gallons needed: ", gallons_needed)

    run_program = str(input("Do you want to run this program (Yes / No): "))