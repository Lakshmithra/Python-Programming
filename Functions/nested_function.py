# Python program to access a function inside a function

def isdisplay():
    def isgreet():
        print("Hello Universe !")
    isgreet()
isdisplay()
