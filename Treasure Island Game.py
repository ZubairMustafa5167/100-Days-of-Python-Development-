#short Game
#Welcome to Treasure Island.
#User Enter his/her Path
path=input("Enter your Path left or Right:")
if path == "left":path=input("Enter your Path left or Right:")
if path == "left":
    path=input("Enter your Path left or Right:")
if path == "left":
    #if path is left then move further otherwise fall
    choose=input(" Choose swim or wait :")
    #user choose swim or wait 
    if choose=="wait":
        #if choose wait move further otherwise Attacked
        door=input("Choose Door color : ")
        #User choose door color 
        if door=="yellow":
            #if door color is yellow then you win otherwise Burned, Eaten or Game over 
            print("You Win!")
        elif door=="red":
            print("Burned by fire.Game Over")
        elif door=="rlue":
            print("Eaten by beasts.Game Over")
        else:
            print("Game Over")
            
    else:
        print("Attacked by trout.Game Over")
        
else :
    print("Fall into a hole.Game Over")
