s = "k:1|k1:2|k2:3|k3:4"

#{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }
l = s.split("|")
d = {}
for i in l:
    l1 = i.split(":")
    d[l1[0]] = l1[1]

print(d)
