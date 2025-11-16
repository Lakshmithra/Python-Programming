def print_formatted_output(subjects, studmarks, studstats, topper, avg_topper, subject_topper):
    print('-' * 90)
    print(f"{'Student':<10}", end="")
    for s in subjects:
        print(f"{s:<10}", end="")
    print(f"{'Average':<10}{'High':<10}{'Low':<10}")
    print('-' * 90)

    for i, j in studmarks.items():
        print(f"{i:<10}", end="")
        for s in subjects:
            print(f"{j[s]:<10}", end="")
        print(f"{studstats[i]['avg']:<10.2f}{studstats[i]['high']:<10}{studstats[i]['low']:<10}")

    print()
    print(f"Topper : Student {topper}")
    print(f"Topper Average : {avg_topper:.2f}")

    print("\nSubject-wise Toppers:")
    for s, t in subject_topper.items():
        print(f"{s} topper : Student {t[0]} - Marks {t[1]}")


def get_input():
    studn = int(input("Enter number of students : "))
    subn = int(input("Enter number of subjects : "))
    subjects = []
    for i in range(subn):
        sub = input(f"Enter the name of subject {i+1} : ")
        subjects.append(sub)

    studmarks = {}
    for i in range(studn):
        submarks = {}
        print(f"\nEnter marks for student {i+1}")
        for j in subjects:
            m = int(input(f"Enter {j} mark : "))
            submarks[j] = m
        studmarks[i+1] = submarks

    return subjects, studmarks, subn, studn


def calculate_stats(studmarks, subn):
    studstats = {}
    for i, j in studmarks.items():
        v = list(j.values())
        stats = {
            'avg': sum(v) / subn,
            'high': max(v),
            'low': min(v)
        }
        studstats[i] = stats
    return studstats


def find_topper(subjects, studstats, studmarks):
    topper = None
    avg_topper = -1
    for i, j in studstats.items():
        if j['avg'] > avg_topper:
            topper = i
            avg_topper = j['avg']

    subject_topper = {}
    for s in subjects:
        subtopper = None
        topmark = -1
        for i, j in studmarks.items():
            if j[s] > topmark:
                subtopper = i
                topmark = j[s]
        subject_topper[s] = (subtopper, topmark)

    return topper, avg_topper, subject_topper

subjects, studmarks, subn, studn = get_input()
studstats = calculate_stats(studmarks, subn)
topper, avg_topper, subject_topper = find_topper(subjects, studstats, studmarks)
print_formatted_output(subjects, studmarks, studstats, topper, avg_topper, subject_topper)
