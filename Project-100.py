from ast import Break


class atm(object):
    def __init__(self,CardNumber,Pin,CashWithDrawl):
        self.CardNumber = CardNumber
        self.CashwithDrawel = CashWithDrawl
        self.Pin = Pin
        

    def cardnumber(self):
        Break
    def pin(self):
        Break
    def Withdraw(self):
        print("WithDrawed")
    
    
    
    

Adhyayan = atm(input("Please Input Your Card Number"),input("Please Enter Your Pin"),input("Please Input Your Withdrawal Amount"))
print(Adhyayan.cardnumber())
print(Adhyayan.pin())
print(Adhyayan.Withdraw())
