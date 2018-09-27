l = [1,2,2,3,1]
#list(set(l))


l1 = []

for i in l:
    if i not in l1:
        l1.append(i)

print(l1)
