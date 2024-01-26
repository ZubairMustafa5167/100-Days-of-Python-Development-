#Password Generator
#import two libraries string and random
import random
# numbers for password
num=[0,1,2,3,4,5,6,7,8,9]
# for random 2 random numbers 
rnd_num=random.sample(num,2)
# Symbols for password 
chrt=["~","!","@","#","$","%","^","&","*",")","-","_","=","+"]
# for random symbol
rnd_chrt=random.sample(chrt,2)
# for small alphabets 
lower_alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rnd_lwr=random.sample(lower_alpha,2)
# for capital Alphabets 
upper_alpha= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rnd_upr=random.sample(upper_alpha,2)
# add the all random numbers, symbols, alphabests
pswd=rnd_num + rnd_upr + rnd_chrt + rnd_lwr
# shuffle the all elements 
random.shuffle(pswd)
for element in pswd:
    print(element,end=" ")

