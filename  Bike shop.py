#  Bike shop
class BikeShop:
   
    def rentbike(self):
        while True:
            avlb=int(input('''
1 Availbale Bikes 
2 I want Bike
3 Check Bike Rent 
4 Exit 
'''))
            a=int(100)
            if avlb == 1:
                print("Availbale Bikes :", a)
            elif avlb == 2:
                b=int(input("How many Bikes do you need? : "))
                rent= int(100)
                print("Rent for Bikes :",b * rent)
                a= 100
                a -=b
                print("Availbale Bikes :",a)
                break
            elif avlb == 3:
                print("Reent for 1 bike: 100 ")
            else:
                print("Invalid input Try Again")
obj=BikeShop()
obj.rentbike()