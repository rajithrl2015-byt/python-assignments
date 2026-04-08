#BANKING
print("WELCOME TO THE RL BANK OF FOREIGN INVESTMENT\nyour goodwill is our aim - since 2026")
print("....................................................................................")
while True:                             #  " while loop " since the contition remain true code shall be excicuted
    class bank:
        def __init__(self):             #    "__init__" setup function for class  "self" used to store values iside the object, 
            self.balance = 0
        
        def name(self):
            name = input("Enter your name  :- ").upper()          #upper used to convert lower case into upper case[capitals]
            print("Welcome to the rl banking services",name)
            print(" -   -   -   -   -  -   -   -   -   -   -")
        def credit(self):
            cre =float(input("Enter your deposit value  :-  "))
            print("   -   -   -   -   -   -   -   -   -   -   ")
            (self.balance) = self.balance+cre
            print("Your amount",cre,"has been suucessfully credited to your acount")
            print("   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  ")
        def chek(self):
            print("Your acount balance is",self.balance)
            print("-   -   -   -   -   -   -   -   -   -  ")
        def withdrawal(self):
            draw = float(input("enter your amount to be withdrawn"))
            print("-   -   -   -   -   -   -   -  -  -  -  -")
            if self.balance >= draw:                    # withdrawal is only posible while the accound has sufficent value
                (self.balance)=self.balance-draw
                print("the amount",draw,"has been sucessfully withdrawn from your savings")
            elif self.balance!=draw :           
                print("insuficient balance,you need to to credit your accout")  
            else:
                print("try again ")     

        
    ban = bank()    # atributes from the "class bank" is store in the object named as "ban"          
    ban.name()
    ban.credit()
    ban.withdrawal()
    ban.chek()