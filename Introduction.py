while True:
    num = int(input("Pick a number between 0 and 100!"))
    
    rand = random.randint(0,100)

    if num == rand:
        print("Bingo!")
        break
    elif num < rand:
        print("Too low!")
    else:
        print("Too high!")
