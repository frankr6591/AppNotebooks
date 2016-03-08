from app.appclass import appclass1
class myclass1(appclass1):
    def __init__(self):
        super(myclass1,self).__init__()
        print("nbClass1 entered")
    def doSomething(self,a,b):
        return a+b