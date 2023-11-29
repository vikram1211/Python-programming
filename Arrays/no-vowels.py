def Replace(a):
    n=len(a)
    b=list(a)
    for i in range(n):
        if b[i]=='A' or b[i]=='a':
            b[i]='6'
        elif b[i]=='E' or b[i]=='e':
            b[i]='3'
        elif b[i]=='I' or b[i]=='i':
            b[i]='1'
        elif b[i]=='O' or b[i]=='o':
            b[i]='0'
    a=''.join(b)
    return a

def main():
    a=input("enter the word you want to convert ")
    replace=Replace(a)
    print(replace)

main()