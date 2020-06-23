from random import *

try:
    #Initializing all counts to 0
    user_win_count = 0
    computer_win_count = 0
    count_game = 0

    #The choices in the game
    choices = ["stone", "paper", "scissors"]

    print("Welcome to the game\n")


    #Another game question, function definition
    def yes_or_no(question):
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            print("Thank you for playing the game")
            return False
        else:
            return yes_or_no("Uhhhh... please enter ")


    #another_game represents the state whether the user intends to play another game 
    another_game = True
    while another_game:
        count_game = count_game+1

        user_choice = str(input("Please choose one: 'stone','paper','scissors': ").lower().strip())

        while(user_choice not in choices):
            user_choice = str(input("Invalid choice. Please choose one of them: 'stone','paper','scissors': "))


        # Pick a random choice from the list of choices ["stone", "paper", "scissors"]
        computer_choice = sample(choices,  1)

        print("\nThe user's choice is " + user_choice + "\nThe computer's choice is " + computer_choice[0] + "\n")

        # Associate Stone to 0, Paper to 1 and Scissors to 2
        choice_n = {'stone': 0,'paper': 1, 'scissors': 2} 

        # Represent user and computer choices in terms of 0,1,2
        user_choice_n = choice_n.get(user_choice)
        computer_choice_n = choice_n.get(computer_choice[0])

        #Rules for the game in a matrix with Stone, Paper and Scissors as rows, and the same fields as columns
        #The row and column number represent the user and computer choice respectively and the corresponding entry represents the winner
        #the value of the entries represent the winner with a 9 representing a Tie 
        game_rules=[[9,1,0],[1,9,2],[0,2,9]]

        winner = game_rules[user_choice_n][computer_choice_n]

        if(user_choice_n==winner):
            user_win_count=user_win_count+1
            print("USER IS THE WINNER")
        elif(computer_choice_n)==winner:
            computer_win_count=computer_win_count+1
            print("COMPUTER IS THE WINNER")
        else:
            print("IT'S A TIE")

        print("Total games played : %d\nUser Win : %d game(s)\nComputer Win : %d game(s)" % (count_game, user_win_count,computer_win_count))
        print("\n")
        another_game = yes_or_no("Do you want to play another game?")

except KeyboardInterrupt:
    print("\nGame Ended")
    




########## References #########
#https://gist.github.com/garrettdreyfus/8153571





