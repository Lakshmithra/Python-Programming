name = 'Laksh'       #global 

def myfunc():
    name = 'Geetha'   #enclosed
    def func():
        name = 'Ramesh'   #local
        print("Local : ",name)
    func()
    print("Enclosed : ",name)
    
print("Global : ",name)
myfunc()
