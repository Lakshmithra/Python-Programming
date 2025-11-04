# Program to count the uppercase and lowercase characters in a string

def stringcase(s):
    uppercount = 0
    lowercount = 0
    for i in s:
        if i.isupper():
            uppercount += 1
        elif i.islower():
            lowercount += 1
        else:
            continue
    return uppercount , lowercount

st = str(input("Enter the string : "))
uppercase , lowercase = stringcase(st)

print(f"No of uppercase characters : {uppercase}")
print(f"No of lowercase characters : {lowercase}")
