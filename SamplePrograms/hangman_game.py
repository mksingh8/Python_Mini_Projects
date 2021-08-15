import random


# user to guess the right word by choosing the alphabets
def hangman():
    # randomly choose the word to be guessed
    marvel_character = random.choice(
        ["ironman", "hulk", "thor", "captainamerica", "clint", "loki", "avengers", "nick", "phil", "maria"])
    # define valid letter to be guessed
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    # print(marvel_character)

    # set the counter to 10
    turns = 10
    guessmade = ''

    while len(marvel_character) > 0:
        main = ""
        missed = 0

        for letter in marvel_character:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == marvel_character:
            print(main)
            print("You win!")
            break

        print("Guess the marvel_character:", main)
        guess = input()
        guess = guess[0]

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
            guess = guess[0]

        if guess not in marvel_character:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
            if turns == 8:
                print("8 turns left")
            if turns == 7:
                print("7 turns left")
            if turns == 6:
                print("6 turns left")
            if turns == 5:
                print("5 turns left")
            if turns == 4:
                print("4 turns left")
            if turns == 3:
                print("3 turns left")
            if turns == 2:
                print("2 turns left")
                print("1 turns left")
                print("Last breaths counting, Take care!")

            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                break


name = input("Enter your name: ")
print("Welcome ", name)
print("-------------------")
print("try to guess the Marvel character in less than 10 attempts")
hangman()
print()
