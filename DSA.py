p = int(input("Enter a prime number : "))
def prime(num):
    count = 1
    for i in range(2,num+1):
        if num%i == 0:
            count = count+1
    if count == 2:
        return True
    else:
        return False
if prime(p) == False:
    print("Not a prime number")
    exit()
q = 0
for i in range(2,p):
    if (p-1)%i == 0 and prime(i) == True:
        q = i
print("Prime Divisor : ",q)

g = 0
for i in range(2,p):
    if (i**q)%p == 1:
        g = i
        break
print("Value of g is : ",g)

h = int(input("Enter a hash number : "))

x = int(input("Select a private key between 0 and q :"))

y = (g**x)%p

print("y : ",y)

k = int(input("Enter a number k between 0 and q : "))

r = ((g**k)%p)%q

print("r : ",r)

s = ((k**-1)*((h+x)*r)%q)

print("s : ",s)

w = 0
for i in range(0,10000):
    if (s*i)%q == 1:
        w = i
        break
print("w : ",w)

u1 = (h*w)%q

print("u1 : ",u1)

u2 = (r*w)%q

print("u2 : ",u2)

v = (((g**u1)*(y**u2))%p)%q

print("v : ",v)

if v == r:
    print("Verification Successfull")
else:
    print("Verification Unsuccessfull")

