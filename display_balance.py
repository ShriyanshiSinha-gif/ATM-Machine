import data
from data import statement
def show_balance():
    if data.balance==0:
      print("Please deposit amount first")
    else:
       print(data.balance)
    statement.append("Current Balance is:"+ str(data.balance))
       