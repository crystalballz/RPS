import random

def title_screen():
    print
    print("8888888b.  8888888b.   .d8888b.  ")
    print("888   Y88b 888   Y88b d88P  Y88b ")
    print("888    888 888    888 Y88b.      ")
    print("888   d88P 888   d88P  \"Y888b.   ")
    print("8888888P\"  8888888P\"      \"Y88b. ")
    print("888 T88b   888              \"888 ")
    print("888  T88b  888        Y88b  d88P ")
    print("888   T88b 888         \"Y8888P\" ")
    print
    print("A Classic Rock Paper Scissor Game")
    print
    return

def game_over():
    print
    print(" .d8888b.         d8888 888b     d888 8888888888 ")
    print("d88P  Y88b       d88888 8888b   d8888 888        ")
    print("888    888      d88P888 88888b.d88888 888        ")
    print("888            d88P 888 888Y88888P888 8888888    ")
    print("888  88888    d88P  888 888 Y888P 888 888        ")
    print("888    888   d88P   888 888  Y8P  888 888        ")
    print("Y88b  d88P  d8888888888 888   \"   888 888        ")
    print(" \"Y8888P88 d88P     888 888       888 8888888888 ")
    print
    print(" .d88888b.  888     888 8888888888 8888888b.     ")
    print("d88P\" \"Y88b 888     888 888        888   Y88b    ")
    print("888     888 888     888 888        888    888    ")
    print("888     888 Y88b   d88P 8888888    888   d88P    ")
    print("888     888  Y88b d88P  888        8888888P\"     ")
    print("888     888   Y88o88P   888        888 T88b      ")
    print("Y88b. .d88P    Y888P    888        888  T88b     ")
    print(" \"Y88888P\"      Y8P     8888888888 888   T88b    ")
    return


title_screen()


print "Welcome to RPS!"

computer_wins = 0
player_wins = 0
while True:
    play = raw_input("Do you want to play?")
    if play.lower() == "yes" or play.lower() == "y":
        print
        print "Okay let's play"
        print "When you want to end the game type \"end\""
        while True:
            moves = ["rock", "paper", "scissor"]
            end_game = ["end","End"]
            computer_move = random.choice(moves)
            player_move = raw_input("Rock Paper or Scissor?")
            if player_move in end_game:
                print
                print "Final Score:"
                print "Computer - " + str(computer_wins)
                print "Player - " + str(player_wins)
                if player_wins > computer_wins:
                    print
                    print "You won the series!"
                else:
                    print
                    print "Computer won the series"
                break
            elif player_move not in moves:
                print "Not a valid choice"
            elif player_move == computer_move:
                print "Draw"
                print
            elif abs(moves.index(player_move) - moves.index(computer_move)) == 1:
                print
                print "You Win!"
                print
                player_wins += 1
            else:
                print
                print "You Lose"
                print
                computer_wins += 1
    elif play.lower() == "n" or play.lower() == "no":
        game_over()
        break
    else:
        pass
