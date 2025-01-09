'''n=int(input())
flag=False
if(n<=1):
    print("Not a prime")
for i in range(2,n):
    if(n%i==0):
        flag= True
if flag:
    print("Not a prime number")
else:
    print("Prime number")
'''

def prime(n):
    if(n<=1):
       return "Not a prime"
    for i in range(2,n):
        if(n%i==0):
            return "Not a prime"
    return "Prime"
a=int(input())
print(prime(a))
    
