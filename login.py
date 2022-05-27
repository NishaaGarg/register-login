def register():
    a=input('Create a username: ')
    p=input('Create a password: ') 
    
    b=(" ".join(a))
    c=list(b.split(" "))
    d,e="`~@#$!%^&*()-+=<>,./?|\[]}{","1234567890"
    q=(" ".join(p))
    r=list(q.split(" "))
    s=len(p)
    d,e="`~@#$%!^&*()-+=<>,./?|\[]}{","1234567890"
    u=any(t.isupper() for t in p)
    v=any(t.islower() for t in p)
    
    if "@." in a:
        print("Please enter a valid email address")
        register()
    elif c[0] in d or c[0] in e:
        print("Username/Email can not start with special characters and numbers. Please try again!") 
        register()
    elif "@" and "." not in a:
        print('Please enter a valid username')
        register()
    elif 5>s or s>16:
        print("The password should have more than 5 and less than 16 characters. Try again!")
        register()
    elif any(t in d for t in p)==False:
        print('Password should have atleast one special character')
        register()
    elif any(t in e for t in p)==False:
        print('Password should have atleast one number')
        register()
    elif u==False or v==False:
        print('Password should have atleast one uppercase and one lower case character')
        register()
    else:
        with open("database.txt","a") as db:
            db.write(f"{a}, {p}\n")

def login():
    db= open("database.txt","r")

    a=input('Enter your Username: ')
    b=input('Enter your password: ')

    listofusers=[]
    listofpassw=[]

    for i in db:
        user,passw=i.split(', ')
        passwo=passw.strip()
        listofusers.append(user)
        listofpassw.append(passwo)
        data=dict(zip(listofusers, listofpassw))

    if a in data:
        if data[a]==b:
            print('You have been loggen in successfully')
        else:
            print('Wrong credentials')
            z=input("Press 'f' if you have forgotten your password or press 'r' to register again: ")
            if z=='f':
               reenter=input('Please enter your registered email')
               if reenter in listofusers:
                   print(f'Your password is: {data[reenter]}')
            elif z=='r':
                register()
            else:
                print('Please enter a valid response') 
    else:
        print('Above entered Email is not found. Please register yourself')
        ab=input("Press 'r' to register yourself: ")
        if ab=='r':
            register()
        else:
            None
        
choose=input("Please press 'r' to register or 'l' to login:  ")
if choose=='r':
    register()
elif choose=='l':
    login()
else:
    print('Please enter a valid option')