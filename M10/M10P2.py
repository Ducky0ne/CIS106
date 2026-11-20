run_program = str(input("Do you want to run this program (Yes / No): "))

while run_program == 'Yes':
    def get_input ():
        length = float(input("Please enter in the length of the room: "))
        width = float(input("Please enter in the width of the room: "))
        height = float (input("Please enter in the height of the room: "))
        return (length, width, height)

    def gallons (length, width, height):
        wall_square_footage = 2*(length * height) + 2 * (width * height)
        gallons_needed_for_wall = wall_square_footage / 50
        ceiling_or_floor_square_footage = (length * width)
        gallons_needed_for_ceiling_or_floor = ceiling_or_floor_square_footage / 50
        return (wall_square_footage, gallons_needed_for_wall, ceiling_or_floor_square_footage, gallons_needed_for_ceiling_or_floor)

    def main ():
        (length, width, height) = get_input ()
        (wall_square_footage, gallons_needed_for_wall, ceiling_or_floor_square_footage, gallons_needed_for_ceiling_or_floor) = gallons (length, width, height)
        return (gallons_needed_for_wall, gallons_needed_for_ceiling_or_floor)
    (gallons_needed_for_wall, gallons_needed_for_ceiling_or_floor) = main ()

    print ("Gallons needed for walls: ", gallons_needed_for_wall)
    print ("Gallons needed for ceiling / floor: ", gallons_needed_for_ceiling_or_floor)

    run_program = str(input("Do you want to run this program (Yes / No): "))