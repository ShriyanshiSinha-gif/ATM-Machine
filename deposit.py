import data
from data import statement
def deposit():
    deposit = float(input("Enter the deposited amount"))
    data.balance = data.balance + deposit
    print("!!!Amount Deposited Successfullyy!!!")
    print("Current Balance is:",data.balance)
    statement.append("Deposited amount: " + str(deposit))
