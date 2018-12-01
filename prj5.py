'''
      Module 5
   15bcs030-Arunbalaji
   15bcs032-Hari Krishnan
   15bcs041-Surya
'''

import mysql.connector as sql
import os
import getpass
import account as accoun

def connection():
  try:
    con=sql.connect(host="localhost",user="root",password="",database="bank")
    return con
  except:
    print("Database error")
    con.rollback()
    
def entry(id):
  con=connection()
  cur=con.cursor()
  qu="select * from trans where userid = %d"%(id)
  cur.execute(qu)
  transactions=cur.fetchall()
  print("--- Deposits and withdraws ---")
  for trans in transactions:
    print(" ",trans[2]," :Rs.",trans[3]," on ",trans[4])
  qu="select * from transaction where userid = %d"%(id)
  cur.execute(qu)
  transactions=cur.fetchall()
  print("\n--- Transactions ---")
  for trans in transactions:
    print(" Deposit to account : ",trans[2]," :Rs.",trans[3]," on ",trans[4])
    
def stmt(id):
  con=connection()
  cur=con.cursor()
  qu="select fname,lname from users where userid = %d"%(id)
  cur.execute(qu)
  usr=cur.fetchone()
  usr=str(usr[0])
  usr1=str(usr[1])
  qu="select accno,balance,type from account where userid = %d"%(id)
  cur.execute(qu)
  min=cur.fetchone()
  acc=int(min[0])
  bal=float(min[1])
  typ=str(min[2])
  print(" UserId : ",id)
  print(" User Name : ",usr)
  print(" Account no. : ",acc)
  print(" Account Type. : ",typ)
  print(" Balance : ",bal)
  return 1;

def fix(id):
  con=connection()
  cur=con.cursor()
  qu="select * from fixed where userid = %d"%(id)
  cur.execute(qu)
  accounts=cur.fetchall()
  for account in accounts:
    print(" FD id : ",account[1])
    print(" Duration(In months) : ",account[2])
    print(" Deposit : ",account[3])
  
def signup():
  print("\n\t -- Enter your details --\n")
  con=connection()
  cur=con.cursor()
  fnam=input("Enter your First name : ")
  lnam=input("Enter your Last name : ")
  phone=int(input("Enter your phone no. : "))
  addr1=input("Enter address line 1 : ")
  addr2=input("Enter address line 2 : ")
  city=input("Enter your city : ")
  state=input("Enter your state : ")
  pin=int(input("Enter your pincode : "))
  typ=input("Enter the Type of account(saving/current) : ")
  pas=input("Enter the password : ")
  amt=float(input("Money to deposit : "))
  if amt<5000 and typ.lower()=='current':
    print(" ! ! Minimum balance is Rs.5000")
    amt=float(input("Money to deposit : "))
  qu="insert into users (fname,lname,phone,addressline1,addressline2,city,state,pin) values('%s','%s',%d,'%s','%s','%s','%s','%d')"%(fnam,lnam,phone,addr1,addr2,city,state,pin)
  cur.execute(qu)
  con.commit()
  qu="select userid from users where phone = %d"%(phone)
  cur.execute(qu)
  id=cur.fetchone()
  id=int(id[0])
  qu="insert into login values(%d,'%s')"%(id,pas)
  cur.execute(qu)
  con.commit()
  qu="insert into account(userid,balance,type) values(%d,%f,'%s')"%(id,amt,typ)
  cur.execute(qu)
  con.commit()
  print("\n------ Account created sucessfully -------")
  print("-- Account Details --")
  i=stmt(id)

def signin():
  con=connection()
  cur=con.cursor()
  c=0
  while c<3:
    id=int(input("Enter your User id. : "))
    qu="select userid from login "
    cur.execute(qu)
    cek=cur.fetchall()
    lis=[]
    for ce in cek:
      lis.append(ce[0])
    i=lis.count(id)
    if(i==0):
      print(" ! Incorrect Userid ")
      c+=1
    else:
      c=5
  if(c==3):
    return False
  c=0
  while c<3:
    pas=getpass.getpass()
    qu="select password from login where userid=%d"%(id)
    cur.execute(qu)
    cek=cur.fetchone()
    cek=str(cek[0])
    if(pas!=cek):
      print(" --- ! Incorrect password ---")
      c+=1
    else:
      c=5
  if(c==3):
    return False  
  opt=1
  print("------ LoggedIn Sucessfully -------")
  qu="select * from account "
  cur.execute(qu)
  cek=cur.fetchall()
  lis=[]
  for ce in cek:
    l=[ce[0],ce[1],ce[2],ce[3]]
    lis.append(l)
  accounts=[]
  for ce in cek:
    accounts.append(accoun.account(ce[0],ce[1],ce[2],ce[3]))
  for a in accounts:
    if id==a.userid:t=a
  while opt!=9:
    print("\n\t -- Sign In --\n")
    print("\t 1 - Address change")
    print("\t 2 - Deposit")
    print("\t 3 - Withdraw")
    print("\t 4 - Ministatement")
    print("\t 5 - Transfer")
    print("\t 6 - Account closure")
    print("\t 7 - Create Fixed deposit")
    print("\t 8 - Avail Loan")
    print("\t 9 - Logout")
    opt=int(input("\n...Enter your option : "))
    
    if(opt==1):
      print("\n------ Address change -------\n")
      print(" ---- Existing Address ----")
      qu="select addressline1,addressline2,city,state,pin from users where userid=%d"%(id)
      cur.execute(qu)
      addr=cur.fetchone()
      print (" AddressLine 1 : ",addr[0])
      print (" AddressLine 2 : ",addr[1])
      print (" City : ",addr[2])
      print (" State : ",addr[3])
      print (" Pincode : ",addr[4])
      addr1=input("Enter address line 1 : ")
      addr2=input("Enter address line 2 : ")
      city=input("Enter your city : ")
      state=input("Enter your state : ")
      pin=int(input("Enter your pincode : "))
      qu="update users set addressline1='%s',addressline2='%s',city='%s',state='%s',pin=%d where userid=%d"%(addr1,addr2,city,state,pin,id)
      cur.execute(qu)
      con.commit()
      print("--- Address changed sucessfully ---")
      
    if(opt==2):
      print("\n------ Money Deposit -------\n")
      print("\t Current balance is Rs.",t.balance)
      dep=float(input("Enter the amount to be deposited into your account : Rs."))
      t.deposit(dep)
      qu="update account set balance=%f where userid=%d"%(t.balance,id)
      cur.execute(qu)
      con.commit()
      qu="insert into trans values(%d,%d,'deposit',%f,curdate())"%(id,t.account,dep)
      cur.execute(qu)
      con.commit()
      print("..Deposited sucessfully")
      print("\t New balance is ",t.balance)
    
    if(opt==3):
      print("\n------ Money Withdrawal -------\n")
      print("\t Current balance is Rs.",t.balance)
      amt=float(input("Enter the amount to be withdrawn from your account : Rs."))
      if amt>t.balance:
        print(".. ! Amount exceeds the balance ")
        print(".. ! Withdraw Unsucessfull")
      else:
        t.withdraw(amt)
        qu="update account set balance=%f where userid=%d"%(t.balance,id)
        cur.execute(qu)
        con.commit()
        qu="insert into trans values(%d,%d,'withdraw',%f,curdate())"%(id,t.account,amt)
        cur.execute(qu)
        con.commit()
        print("..Deposited sucessfully")
        print("\t New balance is ",t.balance)
        
    if(opt==4):
      print("\n------ Mini Statement -------\n")
      i=stmt(id)
      entry(id)
      
    if(opt==5):
      print("\n------ Transfer Money -------\n")
      print("\t Current balance is Rs.",t.balance)
      c=0
      while c<3:
        acc=int(input("-- 'TO' Account no. : "))
        for i in accounts:
          if acc==i.account and acc!=t.account:
            toacc=i
            c=5
        if c!=5:
          print(" ! Incorrect Account no. ")
          c+=1
      if(c==3):
        return False
      qu="select fname from users where userid=%d"%(toacc.userid)
      cur.execute(qu)
      nam=cur.fetchone()
      print("Account holder : ",nam[0])
      amt=float(input("Enter the amount to deposit in account : Rs."))
      if amt>t.balance:
        print(".. ! Amount exceeds the balance ")
        print(".. ! Transaction Unsucessfull")
      else:
        t.transfer(toacc,amt)
        qu="update account set balance=%f where userid=%d"%(t.balance,id)
        cur.execute(qu)
        con.commit
        qu="update account set balance=%f where accno=%d"%(toacc.balance,acc)
        cur.execute(qu)
        con.commit()
        qu="insert into transaction (userid,fromacc,toacc,amount,transdate) values (%d,%d,%d,%f,curdate())"%(id,t.account,acc,amt,)
        cur.execute(qu)
        con.commit()
        print("..Transaction sucessfull")
        print("\t New balance in your account is Rs.",t.balance)
      
    if(opt==6):
      print("\n------ Close Account -------\n")
      print("-- Account Details --")
      i=stmt(id)
      cnf=str(input("Are you sure ? (yes/no) : "))
      if(cnf.lower()== 'no'):
        print("-- Account not closed --")
      elif(cnf.lower()== 'yes'):
        acc=t.account
        qu="insert into closed (userid,accno,closedate) values(%d,%d,curdate())"%(id,acc)
        cur.execute(qu)
        con.commit()
        qu="delete from trans where userid=%d"%(id)
        cur.execute(qu)
        con.commit()
        qu="delete from transaction where userid=%d"%(id)
        cur.execute(qu)
        con.commit()
        qu="delete from account where userid=%d"%(id)
        cur.execute(qu)
        con.commit()
        qu="delete from login where userid=%d"%(id)
        cur.execute(qu)
        con.commit()
        qu="delete from users where userid=%d"%(id)
        cur.execute(qu)
        con.commit()
        os.system('cls')
        print(" ---- Account Closed ----")
        print("Successfully logged out")
        return True
      else:
        print(" ! Invalid option ")
      
    if(opt==7):
      print(" ---- Create Fixed Deposit ----")
      amt=float(input("Enter the amount to deposit : "))
      c=0
      while c==0:
        if amt<=1000:
          print(" ! ! Minimum balance is Rs.1000")
          amt=float(input("Enter the amount to deposit : "))
        if amt>=1000:
          c=1
      term=int(input("Duration of Fixed deposit in months : "))
      c=0
      while c==0:
        if term<12:
          print(" ! ! Minimum duration is 12 months")
          term=int(input("Duration of Fixed deposit in months : "))
        if term>=12:
          c=1
      qu="insert into fixed (userid,duration,amount,start) values (%d,%d,%f,curdate())"%(id,term,amt)
      cur.execute(qu)
      con.commit()
      print("\n------ Fixed deposit created sucessfully -------")
      print("-- Fixed deposit Details --")
      fix(id)
    
    if(opt==8):
      if(t.type.lower() != 'saving'):
        print(" --- ! You cannot avail loan")
      else:
        print(" ---- Avail a loan ----")
        amt=float(input("Enter the aviling loan amount : "))
        c=0
        while c==0:
          if amt>2*t.balance:
            print(" ! ! Your loan limit is (2 times the balance) Rs.",2*t.balance)
            amt=float(input("Amount to deposit : "))
          if amt<=2*t.balance:
            c=1
        term=int(input("Repayment term in years : "))
        c=0
        while c==0:
          if term<1:
            print(" ! ! Minimum duration is 1 year")
            term=int(input("Repayment term in years : "))
          if term>=1:
            c=1
        qu="insert into loan (userid,lamount,repayterm,start) values (%d,%f,%d,curdate())"%(id,amt,term)
        cur.execute(qu)
        con.commit()  
        t.deposit(amt)
        qu="update account set balance=%f where userid=%d"%(t.balance,id)
        cur.execute(qu)
        con.commit()
        qu="insert into trans values(%d,%d,'Loancredit',%f,curdate())"%(id,t.account,amt)
        cur.execute(qu)
        con.commit()
        print("..Loan Sanctioned sucessfully")
        print("\t New balance is ",t.balance)
      
    if(opt==9):
      os.system('cls')
      print("--- Successfully logged out ---")
      return True
  
  
def admin():
  id=input("Enter your User id. : ")
  pas=getpass.getpass()
  if(id =='root' and pas=='admin'):
    print("------ LoggedIn Sucessfully -------")
    opt=1
    while opt!=4:
      print("\n\t -- Admin login --\n")
      print("\t 1 - Closed account History")
      print("\t 2 - Fixed Deposit History")
      print("\t 3 - Loan details")
      print("\t 4 - Logout")
      opt=int(input("\n...Enter your option : "))
      if opt==1:  
        print("----- Closed accounts History ------")
        con=connection()
        cur=con.cursor()
        qu="select * from closed "
        cur.execute(qu)
        cek=cur.fetchall()
        lis=[]
        c=0
        for ce in cek:
          c=1
        if c==0:
          print("--- No Accounts are closed ---")
        else:
          for ce in cek:
            print(" Userid : ",ce[0],"  Account no. :",ce[1],"  Closed date. :",ce[2])
            
      if opt==2:  
        print("----- Fixed Deposit History ------")
        con=connection()
        cur=con.cursor()
        qu="select * from fixed "
        cur.execute(qu)
        cek=cur.fetchall()
        lis=[]
        c=0
        for ce in cek:
          c=1
        if c==0:
          print("--- No Fixed deposits ---")
        else:
          for ce in cek:
            print(" Userid : ",ce[0],"  Fixed deposit id :",ce[1],"Duration : ",ce[2],"  Amount :Rs.",ce[3]," On ",ce[4])
            
      if opt==3:  
        print("----- Loan Details ------")
        con=connection()
        cur=con.cursor()
        qu="select * from loan "
        cur.execute(qu)
        cek=cur.fetchall()
        lis=[]
        c=0
        for ce in cek:
          c=1
        if c==0:
          print("--- No Loans are availed ---")
        else:
          for ce in cek:
            print(" Userid : ",ce[0],"  Loan id. :",ce[1],"  Loan amount. :",ce[2],"Repay terms : ",ce[3]," On ",ce[4])
            
      if(opt==4):
        os.system('cls')
        print("......Successfully logged out")
        return True  
  else:
    return False
    
print("....connected......")
os.system('cls')
opt1=1
while(opt1!=4):
  print("\n\t---------- Welcome to Tech Bank ----------\n")
  print("\t\t 1 - SignUp")
  print("\t\t 2 - SignIn")
  print("\t\t 3 - Admin LogIn")
  print("\t\t 4 - Quit")
  opt1=int(input("\n...Enter your option : "))

  if(opt1==1):
    signup()
  
  elif(opt1==2):
    c=0
    ret=signin()
    if ret==False:
      print(" --- !Login failed ---")
      
  
  elif(opt1==3):
    admin()
  
  elif(opt1==4):
    print("..... Thank you exit .......")
    
  else:
    print(" ... ! Invalid option !")