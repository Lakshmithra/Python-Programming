class Parent:

    def __init__(self,name):
        self.name = name
        print("vanakkam ! This is Chinthaselvam")

    # Abstract method: child classes must implement
    # If a child class does not override this, calling speak() will raise error
  
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Son(Parent):      #inherits Parent

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Hello , This is ",self.name)     # Overriding Parent's abstract method

class Daughter(Parent):     #inherits Parent

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Hi , Myself ",self.name)      # Overriding Parent's abstract method

# Polymorphism: same method behaves differently for different objects

p = Parent("Chinthaselvam")
s = Son('Ramesh')
d = Daughter('Radha')

s.speak()
d.speak()

# p.speak() -> This will raise NotImplementedError

"""
ABSTRACT METHODS - SIMPLE GUIDE

1. An abstract method is a method that is **declared in a parent class but has no code**. 
2. It is like a **rule**: any child class must implement this method. 
3. You cannot use the abstract method directly from the parent class.
4. Helps in **polymorphism**: all child classes have the same method name, but behavior can differ.
5. In Python:
   - Manual way: raise NotImplementedError inside the parent method.
   - Better way: use abc module and @abstractmethod decorator.
"""




