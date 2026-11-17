number_of_players = 0
run_program = str(input("Do you want to run this program (Yes/No): "))

while run_program == 'Yes':

    def get_input():
        players_last_name = str(input("Please enter in players last name: ")) 
        number_of_hits = int(input("Please enter in number of hits: "))
        at_bats = int(input("Please enter in number of at bats: "))
        return(players_last_name, number_of_hits, at_bats)

    def average(number_of_hits, at_bats):
        batting_average = float(number_of_hits/at_bats)
        return(batting_average)

    def main():
        (players_last_name, number_of_hits, at_bats) = get_input()
        batting_average = average (number_of_hits, at_bats)
        print ("Player's last name: ", players_last_name)
        print (f"Batting average: {batting_average:.3f}")
        return(batting_average)
    batting_average = main()

    number_of_players += 1
    run_program = str(input("Do you want to run this program (Y/N): "))

print ("Number of players who ran program: ", number_of_players)