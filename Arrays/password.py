def Valid_Password(a):
    n=len(a)
    lower_case=False
    upper_case=False
    number=False
    symbol=False
    for i in range(n):
        b=ord(a[i])
        if b>=65 and b<91:
            upper_case=True
        elif b>=97 and b<123:
            lower_case=True
        elif b>=48 and b<58:
            number=True
        elif b>=33 and b<48:
            symbol=True
    if lower_case==True and upper_case==True and number==True and symbol==True:
        return True
    else:
        return False

def main():
    a=input("enter your password ")
    b=Valid_Password(a)
    if b:
        print("Your password is valid")
    else:
        print("Your password needs at least one uppercase letter, lowercase letter, number and symbol!")

main()