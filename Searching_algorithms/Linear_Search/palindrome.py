def linear_search_palindrome(arr):
    palindrome = []
    for i in arr:
        if i == i[::-1]:
            palindrome.append(i)
    return palindrome

lst = ['radar','hello','level','world']
o = linear_search_palindrome(lst)
print(o)
