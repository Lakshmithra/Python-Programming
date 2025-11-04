# Program that accepts a hyphen-separated sequence of words as input 
# And prints the words in a hyphen-separated sequence after sorting them alphabetically

def hypensortstring(s):
    s.sort()
    sortedstr = '-'.join(s)
    return sortedstr
  
string = str(input("Enter the hypen-separated string : ")).split('-')
sortedstring = hypensortstring(string)
print(f"Sorted hypenated string : {sortedstring}")
