x="123456789"
y=x[::2]
print(y)

z="vikram dandu"
a=z.split()
b=a[0] +" rakesh " + a[1]
print("hello "+b.title())

names=['Vikram','Rakesh','Sowmya','Sriha']
for i in range(len(names)-1,-1,-1):
    print(i)
    print("Hello "+names[i].title())

guests=['Elon Musk','Einstein','Sam Altman','Andrej Karpathy','Andrew ng']
for j in range(len(guests)):
    print(guests[j] + " Please come to my Dinner party\n")
guest_not_gonna_make='Einstein'
guests.remove(guest_not_gonna_make)
print(guest_not_gonna_make + " is not gonna make it to the party")
for j in range(len(guests)):
    print(guests[j] + " Please come to my Dinner party\n")
guests.insert(0,'Lex')
guests.insert(int(len(guests)/2),'Joe Rogan')
guests.append('Narendra Modi')
print(guests)
xyz=guests.pop()
print(xyz)
print(sorted(guests,reverse=True))
guests.reverse()
print(guests)

list=[i for i in range(1,21)]
print(max(list),min(list),sum(list))

list=[i for i in range(1,20,3)]
print(list)

list=[]
for i in range(3,30):
    list.append(i*3)
print(list)

list=[i*i*i for i in range(1,11)]
print(list)

for k in list[-3:]:
    print(k)

my_pizzas=['onion','chicken','tomato']   
friend_pizzas=my_pizzas[:]
friend_pizzas.append('pepperoni') 
print(friend_pizzas,my_pizzas)
my_pizzas=('onion','chicken','tomato')
print(my_pizzas.index('onion'))


usernames=['admin','tomato','potato','brinjal','carrot']
username=input()
for i in range(len(usernames)):
    if username == usernames[i]:
        if username=='admin':
            print('Hello '+ username +', would you like to see a status report?')
            break
        else:
            print('Hello '+ username + ' thank you for logging in again' )
            break
else:
    print('no user found')

original_list = [1, 2, 3]
copied_list=[5,6,7]
original_list.extend(copied_list)  # copied_list is a new list [1, 2, 3]
original_list.insert(3,23)
#original_list.sort(reverse=True)
sam=[0,1,23]
sam=original_list
print(original_list,sam[::-1])

tuple={
    'vikram':27,
    'sowmya':24
}
tuple['sriha']=1
tuple['vikram']=26
del tuple['sriha']
age_of_sowmya=tuple['sowmya']
print('age of sowmya is ',age_of_sowmya)
print(tuple.get('sriha','no user exists'))
for names,values in tuple.items():
    print(names.title(),' age is', values)