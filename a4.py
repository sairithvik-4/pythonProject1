class Name:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def print(self):
    print(self.firstname, self.lastname)
a=input("enter the first name :")
b=input("enter the last name :")

x = Name(a,b)
x.print()