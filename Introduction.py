while True:
    num = int(input("Pick a number!"))
  
    if num == 50:
        print("Bingo!")
        break
    elif num < 50:
        print("Too low!")
    else:
        print("Too high!")
