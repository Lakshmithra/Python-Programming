class Book:

    # __init__ → runs automatically when object is created
    # Purpose: store data inside the object (initialize attributes)
  
    def __init__(self , author , title , pages):

        print("Book is created !")
        self.author = author
        self.title = title
        self.pages = pages

    """
        __str__ → runs when we print the object (print(b))
        Without __str__, Python prints memory address like <Book object at 0x...>
        By defining __str__, we control how the object should be displayed in a readable format.
    """
    
    def __str__(self):
        return f"Book : {self.title}\nAuthor : {self.author}\nPages : {self.pages}"

    """
        __len__ → runs when len(object) is used
        Python does not know the length of a Book object,
        so we return pages to tell Python: "book length = number of pages".
    """
    
    def __len__(self):
        return self.pages

    """
        __del__ → runs when object is deleted (del b)
        Useful for messages, logging, or releasing resources before destruction.
        After del b, the object is removed from memory, so b cannot be used again.
    """
    def __del__(self):
        print("Book is destroyed")

b = Book('why me ?' , 'laksh' , 969)
print(b)
print("Length :- ",len(b))
del b
# print(b)  NameError: name 'b' is not defined
