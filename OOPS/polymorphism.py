# Two independent classes (no inheritance)

class Son:

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Hello , This is ",self.name)

class Daughter:

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Hi , Myself ",self.name)

# Creating objects

s = Son('Ramesh')
d = Daughter('Radha')

# Calling speak() directly

s.speak()
d.speak()

# Example of polymorphism using a loop
# Both Son and Daughter objects respond to speak() even though they are different classes

for i in [s,d]:
    i.speak()
    
# Example of polymorphism using a function
# Function can take any object as long as it has a speak() method


def p_speak(a):
    a.speak()

p_speak(s)
p_speak(d)

"""
POLYMORPHISM IN PYTHON - QUICK GUIDE

- Polymorphism means "many forms": same method name behaves differently depending on the object.
- In Python, polymorphism can happen:
    1. With inheritance (method overriding)
    2. Without inheritance (different classes having the same method name)
- Key idea: Python decides which method to call at runtime based on the object (duck typing).

- Practical tip: Any function or loop that calls a method will work with any object that has that method.
"""
