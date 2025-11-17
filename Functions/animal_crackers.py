def animal_crackers(string):
    s = string.split()
    if s[0][0] == s[1][0]:
        return True
    else:
        return False
a = animal_crackers('Dancing Deer')
b = animal_crackers('Lazy donkey')
print(a , b)
