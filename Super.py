class parent:
    def __init__(self,txt):
        self.message=txt
    def printmessage(self):
        print(self.message)
class child(parent):
    def __init__(self,txt):
        super().__init__(txt)
x=child("Hello , and welcome !")
x.printmessage()
