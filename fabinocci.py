#fabinacci series

n=int(input("enter any number:"))
a,b=0,1

for i in range(n):
    print(a,end=' ')
    a,b=b,a+b

    
