def primenumber(x):
    a,b=x,2
    if a<=1:
        return False
    while b*b<=x:
        if(x%b==0):
            return False
        b=b+1
    return True

a=int(input("enter the lower range "))
b=int(input("enter upper range "))
x=a
while x<=b:
    if primenumber(x):
        print(x)
    x=x+1
    


    

            
    

