import random

rand = random.randint(0,100)

while True:
    num = int()

    try:
        num = int(float(input("Pick a number between 0 and 100!\n"))) #converts floating point input to integer
    except ValueError: #gives the opportunity to try again (to input) if something not accepted is entered
        print("Input invalid. Please enter a number: \n")
        continue
        
    if num == rand:
        print("Bingo!")
        break
    elif num < rand:
        print("Too low!")
    else:
        print("Too high!")
