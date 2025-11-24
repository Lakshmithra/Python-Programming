def str_upper_lower(string):
    lower = 0
    upper = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            continue
    return lower , upper
l , u = str_upper_lower("I am on my periods.")
print(f"Uppercase : {u}")
print(f"Lowercase : {l}")
