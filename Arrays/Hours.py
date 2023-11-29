def Calc_hours(a,b):
    if b=='T':
        print(sum(a))
    elif b=='A':
        print(round((sum(a)/len(a)),1))
    else:
        print("invalid input")

def main():
    n=int(input("enter number of weeks taking CS50 "))
    a=[]
    for i in range(n):
        a.append(int(input(f"Week {i} HW Hours ")))
    b=input("Enter T for total hours, A for average hours per week: ")
    calc_hours=Calc_hours(a,b)

main()