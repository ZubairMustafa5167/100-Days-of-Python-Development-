import time

class Prompt:
    def get_user_input(self):
        user_prompt = input("What would you like? \n 1 Coffee \n 2 Off Machine \n ")
        if user_prompt == "1":
            self.milk = float(input("Enter Milk Quantity in ml: "))
            self.water = float(input("Enter Water Quantity in ml: "))
            self.coffee = float(input("Enter Coffee Quantity in ml: "))
        elif user_prompt == "2":
            print("Machine is off now")
        else:
            print("Invalid input")

class calculation(Prompt):
    def clctn(self):
        # Call the method to get user input
        self.get_user_input()

        # Perform the calculation based on user input
        self.milk_cost = self.milk * 0.5 + self.water * 0.25 + self.coffee * 0.75

        # Print the report
        print("Report:\nWater = {}\nMilk = {}\nCoffee = {}\nMoney = {} $".format(self.water, self.milk, self.coffee, self.milk_cost))

class payment(calculation):
    def user_payment(self):
        self.get_user_input()  # Call get_user_input before clctn
        self.clctn()
        
        while True:
            pymt = float(input("Pay the amount: "))
            if pymt == self.milk_cost:
                print("Payment has been successful \nProcess start.... ")
                time.sleep(15)
                print("Here is your Coffee. Enjoy!")
                break  # Exit the loop when payment is successful
            elif pymt > self.milk_cost:
                rtn = pymt - self.milk_cost
                print("Get return amount = {} $ \nPayment has been successful \nProcess start.... ".format(rtn))
                time.sleep(15)
                print("Here is your Coffee. Enjoy!")
                break  # Exit the loop when payment is successful
            elif pymt < self.milk_cost:
                print("Insufficient Balance")
                # Update user input values
                self.get_user_input()

# Create an instance of the payment class
obj = payment()
# Call the user_payment method to start the payment process
obj.user_payment()



