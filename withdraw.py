import data
from data import statement
def withdraw():
    withdraw = float(input("Enter the withdrawn amount"))
    if data.balance >= withdraw:
      data.balance=data.balance-withdraw
      print("!!!Amount Withdrawn Successfully!!!")
      print("Current Balance is:",data.balance)
    else:
        print("Insufficient Amount")
    statement.append("Withdrawn amount: " + str(withdraw))