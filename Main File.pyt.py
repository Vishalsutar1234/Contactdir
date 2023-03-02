'''
Main File
=========
'''
def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():
        fp=open('data.txt','a')
        n=input("Enter Name:")
        mn=input("Enter Mobile Number:")
        res=validate_mob(mn)
        #print(res)
        if res==1:
            a,b=searchmob(mn)
            if b==1:
                print("Number Already Exist")
            else:
                d=n+":"+mn+'\n'
                fp.write(d)
                fp.close()
                print("Contact Created Successfully!!")
        else:
            print("Please enter Valid mobile Number!!")
def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("====Contact Directory====")
    print()
    print(d)
    print("===========================")
print("Welcome to Contact Dircctory console app")
print()

def searchmob(n):
     fp=open('Data.txt','r')
     data=fp.readlines()
     for x in data:
        l=x.split(":")
        if int(n)==int(l[1]):
            #print("Contact Found:")
            #print(x)

            return x,1
        else:
            return'',0
def searchname():
     print("Search contact Number by Name")
     ns=input("Enter Name:")
     fp=open('data.txt','r')
     data=fp.readlines()
     #print(data)
     for x in data:
        #print(x)
        l=x.split(":")
        #print(l)
        #print(l[0])
        if ns.upper()==l[0].upper():
            print("Contact Found")
            print(x)
            flag=1
            if flag==0:
                print("Not Found!!!")
               
while True:
    print()
    print("1.Create Contact")
    print("2.View contacts")
    print("3.Search by Name")
    print("4.Search by Mobile Number")
    print("5.Exit")
    ch=int(input("Enter Your Choice:"))

    if ch==1:
        create_contact()
    elif ch==2:
        display()
    elif ch==3:
        searchname()
        
    elif ch==4:
       ms=input("Enter Mobile number to be searched")
       a,b=searchmob(ms)
       #print(a)
       #print(b)
       if b==1:
           print("Number Found:")
           print(a)
       else:
           print("Not Found")
       
    elif ch==5:
        break
    else:
        print("Please Enter Valid Option!!!")

print("Thank You for Using Application")


























