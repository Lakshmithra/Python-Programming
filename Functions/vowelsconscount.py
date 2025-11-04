# Program to count the vowels and consonants in a word

def countword(w):
    vowelcount = 0
    consonantcount = 0
    vowels = 'aeiouAEIOU'
    for i in w:
        if i.isalpha():
            if i in vowels:
                vowelcount += 1
            else:
                consonantcount += 1
    return vowelcount , consonantcount

word = str(input("Enter a word : "))
v , c = countword(word)
print(f"Vowels : {v}\nConsonants : {c}")
