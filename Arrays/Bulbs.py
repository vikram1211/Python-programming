def Get_string():
    string=input('Message: ')
    msg_to_ASCII=list(string)
    n=len(msg_to_ASCII)
    l=[]
    for msg in msg_to_ASCII:
        i=ord(msg)
        l.append(i)
    return l

def Print_bulb(list):
    a=[]
    for n in list:
        b=[]
        while n!=0:
            b.insert(0,n%2)
            n=int(n/2)
        c=len(b)
        while c<8:
            b.insert(0,0)
            c=c+1
        a.append(b)
    for d in a:
        for i in range(len(d)):
            if d[i]==0:
                d[i]=('⚫')
            elif d[i]==1:
                d[i]=('🟡')
        s=''.join(d)
        print(s)
    

def main():
    a=Get_string()
    b=Print_bulb(a)

main()


    