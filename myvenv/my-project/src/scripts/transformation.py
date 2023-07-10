import sys

class transform():

    def __init__(self):
        print(sys.argv[0])
        self.code = self.readRawCode(userInput)
        self.result = self.transformCode(self.code)
    
    def readRawCode(self,userInput) :
        return userInput

    def transformCode(self,input) :
        return (str(input).upper())
    
    def getResult(self) :
        return self.result

