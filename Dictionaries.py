def create_aliens():
    aliens_list=[]
    while True:
        color=input('provide the color of the alien ')
        points=int(input('provide the points for the alien '))
        aliens={'color':color,'points':points}
        aliens_list.append(aliens)
        print("provide yes/no if you want to provide another alien or not ")
        a=input()
        if a.lower()!="yes":
            break
    return aliens_list

def create_pizza():
    pizza_list=[]
    while True:
        crust=input("provide the crust of pizza ")
        toppings=[]
        while True:
            a=input("enter the topping you want ")
            toppings.append(a)
            b=input("type yes if you want to add one more topping ")
            if b.lower()!='yes':
                break
        pizza={'crust':crust,'toppings':toppings}
        pizza_list.append(pizza)
        c=input("provide yes/no if you want to provide another pizza or no ")
        if c.lower() != 'yes':
            break
    return pizza_list
          
def Fav_languages():
    fav_languages={}
    while True:
        name=input("enter a person's name ")
        languages=[]
        while True:
            a=input("enter the person's favourite language ")
            languages.append(a)
            b=input("enter yes if you want to enter another favourite language or no if there is no other favourite language ")
            if b.lower() != 'yes':
                break
        fav_languages[name]=languages
        c=input("enter yes if you want fav languages of another person or no if you want to close ")
        if c.lower() != 'yes':
            break
    return fav_languages

def Create_users():
    user={}
    while True:
        name=input("enter name of the user ")
        details={}
        first=input("enter first name of the user ")
        details['first']=first
        last=input("enter last name of the user ")
        details['last']=last
        location=input("enter the location of the user ")
        details['location']=location
        user[name]=details
        a=input('enter yes if you want to enter details of another user ')
        if a.lower() != 'yes':
            break
    return user

alien_list=create_aliens()
print(alien_list)
for alien in alien_list:
    val=alien['color']
    print(val)

pizza_list=create_pizza()
print(pizza_list)

fav_languages_list=Fav_languages()
print(fav_languages_list)
for person,fav_languages in fav_languages_list.items():
    print('\n'+ person.title() +"'s favorite languages are")
    for languages in fav_languages:
        print(languages.title())

create_users=Create_users()
print(create_users)

        
        
        




