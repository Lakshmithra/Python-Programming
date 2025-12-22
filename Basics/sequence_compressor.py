n = str(input("Enter elements : ")).split()
a =  [int(x) for x in n]

b = True
sequence = []
s = []

for i in a:
    if b:
        s.append(i)
        prev = i
        b = False
    else:
        if i - prev == 1:
            s.append(i)
            prev = i
        else:
            if len(s)!= 1:    
                f = str(s[0])
                l = str(s[len(s)-1])
                sequence.append(f+"-"+l)
            else:
                sequence.append(str(s[0]))
                
            s = [i]
            prev = i
            
if len(s)!=1:
    f = str(s[0])
    l = str(s[len(s)-1])
    sequence.append(f+"-"+l)
else:
    sequence.append(str(s[0]))
print(sequence)
