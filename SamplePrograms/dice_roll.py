from random import randint
while True:
    print('''Enter 1 to play and 2 to exit
    ''')
    user = int(input())
    if user == 1:
        print(randint(1, 6))
    else:
        break

# https://github.com/mksingh8/Python_Mini_Projects.git