#SHOWING HOW MUCH AMOUNT MONEY LEFT IN USER BANK ACCOUNT

total_amount=10000
withdraw=int(input("enter a amount to withdraw"))

if withdraw<total_amount:
    balance=total_amount-withdraw
    print("your account balance is :",balance)
elif withdraw>total_amount:
    print("insufficient balance")