print("WELCOME TO HDFC BANK")
print("INSERT YOUR ATM CARD")
pin=1234
balance=50000
if pin==1234:
    print("1.WITHDRAW")
    print("2.BALANCE ENQUIRY")
    print("3.DEPOSIT")
    print("4.CHANGE PIN")
    print("5.EXIT")
    option=int(input("Choose any option"))
    if option==1:
        withdraw=int(input("Enter the withdraw Amount"))
        if withdraw<=balance:
            balance=balance-withdraw
            print("Amount of ",withdraw ,"withdrawed")
            print("balance is ",balance)
    
