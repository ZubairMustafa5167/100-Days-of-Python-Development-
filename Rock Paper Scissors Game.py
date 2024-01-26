#Rock Paper Scissors Game
#For random value user random module
import random 
rps=["Rock", "Paper", "Scissors"]
rand=random.choice(rps)
#User Input 
user=input("Put Rock Paper Scissors : ")
#If user value and random value from list are same then user enter again value 
if user==rand:
    user=input("Again Put Rock Paper Scissors :")
    # Rock win against Scissors
    if user == "Rock" and rand=="Scissors":
        print("User Win!")
    #Scissors win Against Paper
    elif user=="Scissors " and rand=="Paper":
     print("User Win!")
    # Paper win against Rock
    elif user=="Paper" and rand=="Rock": 
        print("User Win!")
else: print("User Loss Game Over" ,"Random value :",rand,",","User value :",user)