limit = 200
n1 = 0
n2 = 1
print (n1)
print (n2)

s = n1 + n2

while limit > s:
    s = n1 + n2
    print (s)
    n1 = n2
    n2 = s 
