#CONTACT BOOK
i=0
name=[]
num=[]
def add():
    n=input("ENTER NAME:")
    if n in name:
        n=input("NAME ALREADY EXISTS ENTER ENOTHER NAME:")
    p=int(input("ENTER PHONE NUMBER:"))
    if p in num:
        p=int(input("NUMBER ALREADY EXISTS ENTER ANOTHER NUMBER:"))
    name.append(n.upper())
    num.append(p)
    print("CONTACT SAVED SUCCESSFULLY")
   
def view():
    if name==[]:
        print("THERE IS NO CONTACT SAVED")
    else:
        print("-------------------------------")
        print("YOUR CONTACTS ARE")
        for i in range(0,len(name)):
        
            print(name[i].upper(),"    :",num[i])
        print("------------------------------")
def search():
    s=input("ENTER NAME TO SEARCH:")
    t=0
    print("-------------------------------")
    for i in range(len(name)):
        if name[i].upper()==s.upper():
            print(name[i].upper(),"    :",num[i])
            t=1
    if t==0:
        print("NAME CANNOT BE FOUND")
    print("---------------------------------")
def update():
    n=int(input("[1] FOR EDIT NAME,\n[2] FOR EDIT MOBILE NUMBER\nENTER YOUR CHOICE:"))
    if n==1:
          
         a=input("ENTER NAME THAT YOU WANT TO EDIT:")
         if a.upper() not in name:
             print("ENTERED NAME NOT FOUND")
         else:
             
             b=input("ENTER THE NEW NAME FOR CONTACT:")
             for i in range(len(name)):
                 if name[i]==a.upper():
                     name[i]=b.upper()
                     print("CONTACT UPDATE SUCCESSFULLY")
                     print("---------------------------------")
                     print(name[i],":",num[i])
                     print("---------------------------------")
    else:
         a=int(input("ENTER NAME THAT YOU WANT TO EDIT:"))
         if a not in num:
             print("ENTERED NAME NOT FOUND")
         else:
             b=int(input("ENTER THE NEW NAME FOR CONTACT:"))
             for i in range(len(num)):
                 if num[i]==a:
                     num[i]=b
                     print("CONTACT NAME UPDATED SUCCESSFULLY")
                     print("---------------------------------")
                     print(name[i],":",num[i])
                     print("---------------------------------")

def delete():
    dn=input("ENTER NAME TO DELETE  FROM CONTACT:")
    if dn.upper() in name:
         for i in range(0,len(name)):
            if name[i]==dn.upper():
                name.pop(i)
                num.pop(i)
                print("CONTACT DELETED SUCCESFULLY")
                print("---------------------------------")
                view()
                print("---------------------------------")
    else:    
         print("ENTERED NAME NOT FOUND")
   
    
print("//////////////////////WELCOME TO CONTACT BOOK\\\\\\\\\\\\\\\\\\\\\\\\\\ \n")
while(1):
    try:
        t=int(input("\n\n\n[1 FOR ADD CONTACT],\n[2 FOR DELETE CONTACT],\n[3 FOR SEARCH CONTACT],\n[4 FOR UPDATE CONTACT],\n[5 FOR DISPLAY CONTACT],\n[6 FOR EXIT],\nENTER YOUR CHOISE:"))
    except:
        t=int(input("ENTER VALID NUMBER:"))
    if t<1 or t>6:
        print("YOU ENTERED A WRONG CHOICE TRY AGAIN!")
        t=int(input("ENTER CORRECT CHOICE:"))
    if t==1:
        add()
    elif t==5:
        view()
    elif t==3:
        search()
    elif t==4:
        update()
    elif t==2:
       delete()
    elif t==6:
        break
    print("**********************************************************************")
    
   
    
    
