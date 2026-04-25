from display_balance import show_balance
from deposit import deposit
from withdraw import withdraw
from statement import show_statement

def atm_machine():
    while True:
        print("\n1: SHOW BALANCE  ")
        print("2: DEPOSIT MONEY")
        print("3. WITHDRAW MONEY ")
        print("4. STATEMENT")
        print("5. Exit")
        preference = int(input("Enter your preference: "))
        
        if preference==1: show_balance()
        elif preference==2: deposit()
        elif preference==3: withdraw()
        elif preference==4: show_statement()
        elif preference==5:
          print("Thanks for visiting our ATM!")
          break
        else:
          print("Invalid choice")
atm_machine()
