# Program to convert a word in lowercase to uppercase

def lowertoupper(str):
   return str.upper()

s = str(input("Enter the word (lowercase) : ")).lower()
us = lowertoupper(s)
print(f"Uppercase : {us}")
