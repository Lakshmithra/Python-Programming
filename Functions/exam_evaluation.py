def display_rank_list(ranklist):
    print("\nRank List\n")
    print("-" * 30)
    print(f"{'Name':<10}{'Score':<10}{'Grade':<10}")
    print("-" * 30)
    for i , j in ranklist:
        print(f"{i:<10}{j[0]:<10}{j[1]:<10}")
    print("-" * 30)


answerkey = ['A','B','A','D','D','C','B','C','A','B']
studn = int(input("Enter number of students : "))
studans = {}
for i in range(studn):
    name = input(f"Enter name of student {i+1} : ")
    keys = list(input("Enter the answers (as one string) : ").upper())
    studans[name] = keys

studmarks = {}
for i,j in studans.items():
    score = 0
    for k in range(len(j)):
        if answerkey[k] == j[k]:
            score += 1
    if score == 10 or score == 9:
        grade = 'A'
    elif score == 8:
        grade = 'B'
    elif score == 7:
        grade = 'C'
    elif score == 6:
        grade = 'D'
    elif score < 6:
        grade = 'E'
    studmarks[i] = [score , grade]

items = studmarks.items()
ranklist = sorted(items , key = lambda x: x[1][0] , reverse = True)

display_rank_list(ranklist)

