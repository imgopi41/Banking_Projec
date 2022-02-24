class Bank: #creating a class in the name of 'Bank'.

    def __init__(self): #defining init constructor.
        self.balance=0  #initializing self balance as '0'.
        print("Your account is created")    #message for user

    def Deposit(self):  #defining a function "Deposit".
        amount = float(input("Enter the amount to deposit: "))  #Asking user to Deposit the amount.
        self.balance=self.balance + amount  #initial balance and user Depsoited amount will be stored in self.balance
        print("your amount is deposited %f" % self.balance) #prints the Deposited amount
       
    def Withdraw(self): #defining a function 'Withdraw'.
        amount = float(input("Enter the amount you want to withdraw: "))    #asking user to enter the amount to withdraw
        if(self.balance >= amount): #if-statment checks available balance is greater than & equal to amount which is entered for withdraw
          self.balance=self.balance - amount #if true you get your cash
          print("please collect your cash and remaining balance is %f" % self.balance)  #message for user
        else:   
            print("invalid amount") #if-condition is false it shows invalid 

    def enquiry(self):  #defining enquiry function
        print("Your account balance is %f" % self.balance)  #shows available balance.


acc = Bank()    #creating object in the name of 'acc' and calling our class "Bank".
acc.Deposit()   #calling function Deposit()
acc.Withdraw()  #calling function Withdraw()
acc.enquiry()   #calling function enquiry()
