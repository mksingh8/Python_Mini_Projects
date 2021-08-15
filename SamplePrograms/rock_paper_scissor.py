from random import randint

#  create the list of the option
options = ["Rock", "Paper", "Scissor"]
# assign random option to the computer
computer = options[randint(0, 2)]
# print(computer)

# set player to be false
player = True
while player:
    # get the input from player
    player = input("Rock, Paper or Scissor? Your Play: ")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You loose! ", computer, " covers ", player)
        else:
            print("You win! ", player, " smashes ", computer)
    elif player == "Paper":
        if computer == "Scissor":
            print("You loose! ", computer, " cuts ", player)
        else:
            print("You win! ", player, " covers ", computer)
    elif player == "Scissor":
        if computer == "Rock":
            print("You loose! ", computer, " smashes ", player)
        else:
            print("You Win! ", player, " cuts ", computer)
    else:
        print(player, " is not valid play, please check your spelling")
    player = False
    # ask the player if he want to play again
    replay = int(input("Enter 1 to play again and anything else to exit: "))
    if replay == 1:
        player = True
    else:
        player = False
    computer = options[randint(0, 2)]
    # print(computer)



