def Rotate(char,key):
    key=key%26
    x=ord(char)
    if x>=65 and x<=90:
        c=x+key
        if c>90:
             c=c+64-90
        char=chr(c)
        return char
    elif x>=97 and x<=122:
        c=x+key
        if c>122:
            c=c-122+96
        char=chr(c)
        return char
    else:
        return char

def main():
    key = int(input('Enter the key '))
    plaintext=input('Enter the string ')
    cnvrt_list=list(plaintext)
    for i in range(len(cnvrt_list)):
        cnvrt_list[i]=Rotate(cnvrt_list[i],key)
    ciphertext=''.join(cnvrt_list)
    print(ciphertext)
    
main()