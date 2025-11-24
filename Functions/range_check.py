def range_check(num , low,high):
    if num in range(low , high+1):
        print(f"{num} is in range between {low} and {high}")
    else:
        print(f"{num} is not in range between {low} and {high}")
range_check(5,2,7)
