n = [2,7,11,15,9]
t,l = 9,[]
for i in range(0,4):
    for j in range(1,4):
        if n[i]==t or n[j]==t:
            l.append(i)
            l.append(j)
        if n[i]+n[j]==t:
            l.append(i)
            l.append(j)
        
print(l)