def palindrome(string):
    string = string.replace(" ","")
    reverse = string[::-1]
    return string == reverse

string = "nurses run"
n = palindrome(string)

if n:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")
