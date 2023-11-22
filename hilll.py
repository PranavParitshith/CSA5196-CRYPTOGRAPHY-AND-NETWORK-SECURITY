a = []
for i in range(65,91):
    a.append(chr(i))

p = input("Enter the Plain Text : ")

k =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        k[i][j] = int(input("Enter : "))

if len(p)%3 != 0:
    p = p + 'X'
print(p)

pairs = [p[i:i+3] for i in range(0, len(p), 3)]

def multiply(matrix1, matrix2):
    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[j] += matrix1[i][j] * matrix2[i]
    return result
print("Plain Text Pairs:", pairs)
c = ""
for pair in pairs:
    mat = [ord(pair[0])-65,ord(pair[1])-65,ord(pair[2])-65]
    result = multiply(k,mat)
    print(result)
    result[0] = (result[0]%26)+65
    result[1] = (result[1]%26)+65
    result[2] = (result[2]%26)+65
    
    c = c + chr(result[0])+chr(result[1])+chr(result[2])
print("CIPHER : "+c)
