import sqlite3

def checK(ck):
	conn=sqlite3.connect("E:\Crypto\crypto project\AccountInfo.db")
	cmd="select * from Details where Card_No="+str(ck)
	cursor=conn.execute(cmd)
	profile=None
	for row in cursor:
		profile=row
	conn.close
	return profile
	
def update(Id):
	conn=sqlite3.connect("E:\Crypto\crypto project\AccountInfo.db")
	cmd="select * from Details where Card_No="+str(cardNo)
	cursor=conn.execute(cmd)
	ifRecordExist=0
	for row in cursor:
		ifRecordExist=1
	if(ifRecordExist==1):
		cmd="update Details SET Pin="+str(pin)+" where Card_No="+str(cardNo)
	conn.execute(cmd)	
	conn.commit()
	conn.close()
	
def updateB(Id):
	conn=sqlite3.connect("E:\Crypto\crypto project\AccountInfo.db")
	cmd="select * from Details where Card_No="+str(cardNo)
	cursor=conn.execute(cmd)
	ifRecordExist=0
	for row in cursor:
		ifRecordExist=1
	if(ifRecordExist==1):
		cmd="update Details SET Balance="+str(balance)+" where Card_No="+str(cardNo)
	conn.execute(cmd)	
	conn.commit()
	conn.close()
	
print ('\n______________________________Welcome___________________________\n')
a=int(input('\n1. Withdrawl \n2. Check Balance \n3. Change Pin \n4. Exit\nEnter the choice: '))
while(a!=4):
	if(a==1):
		cardNo=str(input('Enter the Card No.: '))
		profile=checK(cardNo)
		if(profile!=None):
			pin=profile[5]
			Pin=int(pin)
			balance=int(profile[4])
			if(Pin == 0):
				pin=str(input('Create a new Pin: '))
				if(len(pin)!=4):
					print('Create a correct Pin')
					pin=str(input('Enter the Pin: '))
				print('Pin Created Successfully')
				pin=hash(pin)
				update(cardNo)
			else:
				pin_user=int(input('Enter the pin: '))
				pin_user=str(pin_user)
				pin_user=hash(pin_user)
				if(Pin==pin_user):
					amnt=str(input('Enter the Amount to be Withdrawn: '))
					Amt=int(amnt)
					if(balance>Amt):
						balance=balance-Amt
						print ('Transaction Success')
						print ('Available Balance',balance)
						updateB(balance)
					else:
						print('Not Sufficient Balance')
				else:
					print('Enter the correct Pin')
		if(profile==None):
			print ('Enter Correct Card No')		
	if(a==2):
		cardNo=str(input('Enter the Card No.: '))
		profile=checK(cardNo)
		if(profile!=None):
			pin=profile[5]
			balance=profile[4]
			if(pin == 0):
				pin=str(input('Create a new Pin: '))
				if(len(pin)!=4):
					print('Create a correct Pin')
					pin=str(input('Enter the Pin: '))
				print('Pin Created Successfully')
				pin=hash(pin)
				update(cardNo)
			else:
				pin_user=int(input('Enter the pin: '))
				pin_user=hash(str(pin_user))
				if(pin==pin_user):
					print('Available Balance :',balance)
				else:
					print('Enter the correct Pin')
		if(profile==None):
			print ('Enter Correct Card No')
	if(a==3):
		cardNo=str(input('Enter the Card No.: '))
		profile=checK(cardNo)
		if(profile!=None):
			pin=profile[5]
			if(pin==0):
				pin=str(input('Create a new Pin: '))
				if(len(pin)!=4):
					print('Create a correct Pin')
					pin=str(input('Enter the Pin: '))
				print('Pin Created Successfully')
				pin=hash(pin)
				update(cardNo)
			else:
				pin_user=str(input('Enter Old Pin: '))
				pin_user=hash(pin_user)
				if(pin==pin_user):
					newpin=str(input('Create a new Pin: '))
					if(len(newpin)!=4):
						print('Create a correct Pin')
						newpin=str(input('Enter the Pin: '))
					print('Pin Created Successfully')
					pin=hash(newpin)
					update(cardNo)
		if(profile==None):
			print ('Enter Correct Card No')	
	z=int(input('\nDo you want to continue:\n1. Yes\t2.No \nEnter the Choice: '))
	if(z==1):
		a=int(input('\n1. Withdrawl \n2. Check Balance \n3. Change Pin \n4. Exit\nEnter the choice: '))
	if(z==2):
		break
if(a==4 or z==2):
	print ("Good Bye")
	exit


