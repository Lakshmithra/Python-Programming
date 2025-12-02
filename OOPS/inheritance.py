class Parent:

    def __init__(self):
        print("Hi , This is parent class !")    # Constructor runs when object is created

    def who_am_i(self):
        print("I am a parent")

    def work(self):
        print("I am working")

    def age(self):
        print("I am elder")     # Method not overridden in child

class Child(Parent):

    def __init__(self):
        Parent.__init__(self)                            # Calls Parent constructor (alternative: super().__init__())
        print("Hello , This is student class !")

    def who_am_i(self):
        print("I am a child")       # Overriding Parent method

    def work(self):
        print("I am a student")     # Overriding Parent method

        
p = Parent()
p.who_am_i()    # Calls Parent method
p.work()

c = Child()
c.who_am_i()  # Calls Child's overridden method
c.work()      # Calls Child's overridden method
c.age()       # Calls Parent method (inherited, not overridden)

Parent.work(p)  # Calls Parent method explicitly
Parent.work(c)  # Calls Parent method on Child object
Child.work(c)   # Calls Child method explicitly

"""
INHERITANCE IN PYTHON - SIMPLE GUIDE

1. What is Inheritance?
   - Child class can use properties and methods of Parent class.
   - Helps avoid repeating code.

2. How to use it:
   - Define child as: class Child(Parent):
   - Child can override Parent methods by redefining them.
   - Child automatically gets Parent methods if not overridden.
   - Use super().__init__() to call Parent constructor inside Child.
   - Can also call Parent.method(obj) explicitly if needed.

3. Practical Tips:
   - Don’t wrap print-methods with print() (they return None).
   - Only call Child methods on Child objects.
   - Python looks for methods in this order: Child → Parent → Grandparent.
"""
