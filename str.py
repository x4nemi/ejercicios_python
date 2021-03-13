class Str:
    def __init__(self):
        self.__palabra = "hi"
    
    def getStr(self):
        self.__palabra = input("Dame string: ")
    
    def printStr(self):
        print(self.__palabra.upper())