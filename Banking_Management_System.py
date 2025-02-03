#program code starts
import sqlite3
import random
mydb=sqlite3.connect('bank.db')
mycursor=mydb.cursor()
mycursor.execute("create table Account_Details (Account_No bigint(50), Name varchar(30), ph_no int(10), Address varchar(50), Current_balance float(30))")
mydb.commit()


def NewAccount():
	inamount=int(input("Deposit initial amount minimum Rs 1000:"))
	if inamount>=1000:
		urname=input("Enter your name")
		urphno=int(input("Enter your phone number"))
		uraddress=input("Enter your address")
		newaccno=random.randint (10000,50000)
		mycursor.execute("insert into Account_Details values (?,?,?,?,?);",(newaccno,urname,urphno,uraddress,inamount))
		mydb.commit()
		print("Your account has been successfully created")
		mycursor.execute("select * from Account_Details where Account_No=?;",(newaccno,))
		r=mycursor.fetchone()
		print("Account Number,Name,Phone Number,Address,Balance")
		for i in r:
			print (i,end=" ")
	else:
		print("Error! Incorrect initial amount.Try Again.")
		
		
def DepositMoney():
	a=eval(input("Enter your account number"))
	mycursor.execute("select Account_No from Account_Details")
	recs=mycursor.fetchall()
	for i in recs:
		for j in i:
			if j==a:
				inamount=eval(input("Enter amount to be deposited"))
				mycursor.execute("update Account_Details set Current_balance=Current_balance+? where Account_No=?",(inamount,a,))
				mydb.commit()
				mycursor.execute("select Current_balance from Account_Details where Account_No=?",(a,))
				mydb.commit()
				recs=mycursor.fetchone()
				for i in recs:
					print("Your updated balance is:",i)
				break    
			else:
				break
				

				
def WithdrawMoney():
	b=eval(input("Enter your account number"))
	mycursor.execute("select Account_No from Account_Details")
	recs=mycursor.fetchall()
	for i in recs:
		for j in i:
			if j==b:
				inamount=eval(input("Enter amount to be withdrawn"))
				mycursor.execute("select Current_balance from Account_Details where Account_No=?",(b,))
				mydb.commit()
				r=mycursor.fetchone()
				for i in r:
					c=i
					break
				if inamount<=c:
					mycursor.execute("update Account_Details set Current_balance=Current_balance-? where Account_No=?",(inamount,b))
					mydb.commit()
					mycursor.execute("select Current_balance from Account_Details where Account_No=?",(b,))
					recs=mycursor.fetchone()
					for i in recs:
						print("Update Account Balance is:",i)
				else:
					print("Withdrawl Amount cannot exceed Current Balance")
				break
			else:
				break
		
		
def BalanceEnquiry():
	c=eval(input("Enter your account number"))
	mycursor.execute("select Account_No from Account_Details")
	recs=mycursor.fetchall()
	for i in recs:
		for j in i:
			if j==c:
				mycursor.execute("select Current_balance from Account_Details where Account_No=?",(c,))
				recs=mycursor.fetchone()
				for i in recs:
					print("Your current balance is:",i)
				break
			else:
				break						
						
def ModifyAccount():
	def NewName():
		a=eval(input("Enter your account number"))
		mycursor.execute("select Account_No from Account_Details")
		recs=mycursor.fetchall()
		for i in recs:
			for j in i:
				if j==a:
					urname=input("Enter new name")
					mycursor.execute("update Account_Details set Name=? where Account_No=?",(urname,a))
					mydb.commit()
					print("Your name was changed to",urname)
					break
				else:
					break
		
	def NewPhone():
		a=eval(input("Enter your account number"))
		mycursor.execute("select Account_No from Account_Details")
		recs=mycursor.fetchall()
		for i in recs:
			for j in i:
				if j==a:
					urphno=input("Enter new phone number")
					mycursor.execute("update Account_Details set ph_no=? where Account_No=?",(urphno,a))
					mydb.commit()
					print("Your phone number was changed to",urphno)
					break
				else:
					break
		
	def NewAddress():
		a=eval(input("Enter your account number"))
		mycursor.execute("select Account_No from Account_Details")
		recs=mycursor.fetchall()
		for i in recs:
			for j in i:
				if j==a:
					uraddress=input("Enter new address")
					mycursor.execute("update Account_Details set Address=? where Account_No=?",(uraddress,a))
					mydb.commit()
					print("Your address was changed to",uraddress)
					break
				else:
					break
		
#main	
	while True:
		print("Input 1 to change name")
		print("Input 2 to change phone number")
		print("Input 3 to change address")
		print("Input 4 to exit")
		choice=int(input("Enter your choice(1-4)"))
		if choice==1:
			NewName()
		if choice==2:
			NewPhone()
		if choice==3:
			NewAddress()
		if choice==4:
			break
		elif choice>4 or choice<1:
			print("Invalid input")


def CloseAccount():
	print("Are you sure you want to close your account in our bank?")
	print("Input 1 to confirm snd 0 to cancel")
	b=int(input())
	if b==1:
		a=eval(input("Enter your account number"))
		mycursor.execute("select Account_No from Account_Details")
		recs=mycursor.fetchall()
		for i in recs:
			for j in i:
				if j==a:
					mycursor.execute("Delete from Account_Details where Account_No=?;",(a,))
					mydb.commit()
					print("Your account was closed")
				else:
					break
	elif b==0:
		print("Your account was not closed")
	else:
		print("Invalid input")
	
			
	
#main
while True:
	print("\nMain Menu")
	print("1.Create New Account")
	print("2.Deposit Money")
	print("3.Withdraw Money")
	print("4.Balance Enquiry")
	print("5.Modify Account")
	print("6.Close Account")
	print("7.Exit")
	ch=int(input("Enter your option(1-7)"))
	if ch==1:
		NewAccount()
	if ch==2:
		DepositMoney()
	if ch==3:
		WithdrawMoney()
	if ch==4:
		BalanceEnquiry()
	if ch==5:
		ModifyAccount()
	if ch==6:
		CloseAccount()
	if ch==7:
		print("Thank you for using our portal")
		print("Have a great day!!!")
		print("Created by Pratham Lohia")
		break
	elif ch>7 or ch<1:
		print("Invalid Option")
#program code ends
		

		
	
