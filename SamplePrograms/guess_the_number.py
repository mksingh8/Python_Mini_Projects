from random import randint

number = randint(0, 10)
# print(number)
for i in range(0, 3):
    guess = int(input("Enter your number: "))
    if guess == number:
        print("You won! The number is: ", number)
        break

if guess != number:
    print("You loose. The correct number was ", number)



