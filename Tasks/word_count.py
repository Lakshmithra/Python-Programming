try:
    with open ("Notes.txt" , "r") as file:
        content = file.read()
    if not content.strip():
        print("File is empty !")
        exit()
except FileNotFoundError:
    print("Error! File couldn't be opened !")
    exit()
except Exception as e:
    print(f"Error ! {e}")
    exit()

word_count = len(content.split())
line_count = content.count("\n") + 1
char_count = len(content)

print("\nWords : ",word_count)
print("Lines : ",line_count)
print("Characters : ",char_count)

words = content.split()
freq_dict = {}

for i in words:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
        
print()
print("-" * 32)
print(f"{'WORD':^15}|{'FREQUENCY':^15}|")
print("-" * 32)
for i , j in freq_dict.items():
    print(f"{i:^15}|{j:^15}|")
print("-" * 32)



        
