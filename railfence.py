depth = int(input("Enter the Depth : "))
p = input("Enter the plain text : ")
l = len(p)
a = [[0 for _ in range(l)] for _ in range(depth)]
dir = 1
row = 0
for j in range(l):    
    a[row][j] = p[j]
    row = row + dir
    if row == depth-1 or row == 0:
        dir = dir * -1
c = ""
for i in range(depth):
    for j in range(l):
        if a[i][j] == 0:
            continue
        else:
            c = c + a[i][j]
print("Cipher : ",c)
