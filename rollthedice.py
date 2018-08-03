import random as rand

roll_dice = input("Roll the dices[y=1/n=0]?\n")
while roll_dice != 0:
    if(roll_dice == 1):
        print("Player1:")
        print(rand.randint(1,6)) 
        print("Player2:")
        print(rand.randint(1,6)) 
        roll_dice = input("Roll the dices[y=1/n=0]?\n")
    else:
        print("Invalid response.Please type 'y' or 'n'.")
        roll_dice = input("Roll the dices[y=1/n=0]?\n")
        
print("Farewell!")
