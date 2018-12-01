class account:
  def __init__(self,id,acc,bal,typ):
    self.userid=id
    self.account=acc
    self.balance=bal
    self.type=typ
  def deposit(self,amt):
    self.balance+=amt
  def withdraw(self,amt):
    self.balance-=amt
  def transfer(self,acc,amt):
    self.withdraw(amt)
    acc.deposit(amt)
  def __str__(self):
    return (" Account no. :"+str(self.account)+"\n Balance :"+str(self.balance)+"\n Type :"+self.type+"\n")
    