from random import randint

door_A = 1
door_B = 2
door_C = 3

no_change_win_count = 0
change_win_count = 0
number_of_plays = 0
no_change_play = 0
change_play = 0


def door_select():
    door = randint(1, 3)
    return (door)


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

play = input ("Press space to continue, any other key to exit")
while play == " ":
    prize_door = door_select()
    if prize_door == 1:
        print ("Prize is behind door A")
    elif prize_door == 2:
        print("Prize is behind door B")
    else:
         print("Prize is behind door C")
    player_initial_select = door_select()
    if player_initial_select == 1:
        print("Player selected door A ")
    elif player_initial_select == 2:
            print("Player selected door B ")
    else:
        print ("Player selected door C ")

    revealed_door = reveal_non_prize(player_initial_select, prize_door)



    answer = input ("Do you want to change your selected door? .......  Y/N").upper()

    if answer == "N" and player_initial_select == prize_door:
        print ("You win!")
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
    play = input("Press space to continue, any other key to exit")