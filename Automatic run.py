from random import randint

door_A = 1
door_B = 2
door_C = 3

no_change_win_count = 0
change_win_count = 0
number_of_plays = 0
no_change_play = 0
change_play = 0
n = 0


def door_select():
    door = randint(1, 3)
    return(door)


def reveal_non_prize(player_initial_select, prize_door):
    if door_A == player_initial_select:
        if door_B == prize_door:
            print("Door C has a goat")
        elif door_C == prize_door:
            print("Door B has a goat")
        else:
            open = randint (1, 2)
            if open == 1:
                print("Door B has a goat")
            else:
                print("Door C has a goat")
    elif door_B == player_initial_select:
        if door_A == prize_door:
            print("Door C has a goat")
        elif door_C == prize_door:
            print("Door A has a goat")
        else:
            open = randint (1, 2)
            if open == 1:
                print("Door A has a goat")
            else:
                print("Door C has a goat")
    elif door_C == player_initial_select:
        if door_B == prize_door:
            print("Door A has a goat")
        elif door_A == prize_door:
            print("Door B has a goat")
        else:
            open = randint (1, 2)
            if open == 1:
                print("Door B has a goat")
            else:
                print("Door A has a goat")

def get_number_of_runs():
    while True:
        try:
            play = int(input ("Type in how many runs you wish the system to perform: "))
        except ValueError:
            print("This is not a whole number.\nPlease try again.")
            continue
        else:
            return play



play = get_number_of_runs()

while n < play:
    prize_door = door_select()
    if prize_door == 1:
        print ("Prize is behind door A")
    elif prize_door == 2:
        print("Prize is behind door B")
    else:
        print("Prize is behind door C")
    player_initial_select = door_select()
    if player_initial_select == 1:
        print ("Player selected door A ")
    elif player_initial_select == 2:
            print("Player selected door B ")
    else:
        print ("Player selected door C ")

    #revealed_door = reveal_non_prize(player_initial_select, prize_door)



    choice = randint(1,2)
    if choice == 1:
        answer = "N"
    elif choice == 2:
        answer = "Y"

    if answer == "N" and player_initial_select == prize_door:
        print("You win!")
        no_change_win_count += 1
        no_change_play += 1
    elif answer == "N" and player_initial_select != prize_door:
        print("You lose!")
        no_change_play += 1
    elif answer == "Y" and player_initial_select == prize_door:
        print("You lose!")
        change_play += 1
    elif answer == "Y" and player_initial_select != prize_door:
        print("You Win!")
        change_win_count += 1
        change_play += 1
    number_of_plays += 1

    print("\nNumber of plays = ", number_of_plays)
    print("\nNumber of no change plays = ", no_change_play)
    print("\nNumber of no change wins = ", no_change_win_count)
    print("\nNumber of change plays = ", change_play)
    print("\nNumber of change wins = ", change_win_count)

    n += 1

percent_no_change_wins = no_change_win_count * 100 / no_change_play
percent_change_wins = change_win_count * 100 / change_play
print ("\nNo change wins percentage:", percent_no_change_wins)
print("\nChange wins percentage: ", percent_change_wins)