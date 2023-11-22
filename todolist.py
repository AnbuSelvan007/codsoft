s=[]#variable act as container to store task data
def add(a):
    s.append(a)
    print("_____________________________________")
    print("TASK ADDED SUCESSFULLY")
    print("_____________________________________")
def remove(a):
    
    print("_____________________________________")
    if str(a) not in s:
        print("THE GIVEN TASK NOT FOUND")
    else:
        s.remove(a)
        print("TASK REMOVED SUCESSFULLY")
    print("_____________________________________")
def display():
    print("_____________________________________")
    if s!=[]:
       
        
        for i in range(0,len(s)):
             print(s[i].upper()," TASK COMPLETED")
       
    else:
        print("NO TASK ARE COMPLETED")
    print("_____________________________________")
def search(a):
     print("_____________________________________")
     print("TASK","           ","STATUS")
     for i in s:
        
        if a.upper() in s:
           
            print(a.upper(),"           ","COMPLETED")
     else:
         print(a.upper(),"           ","NOT COMPLETED")
     print("_____________________________________")
print("__________________________/WELCOME TO TODO LIST\_________________________");
while(1):
    try:
        t=int(input("\n\n\n[1 FOR ADD TASK],\n[2 FOR REMOVE TASK],\n[3 FOR DISPLAY TASK],\n[4 FOR SEARCH],\n[5 FOR EXIT]\nENTER YOUR CHOICE :"))
    except:
        t=int(input("ENTER VALID INPUT:"))
    if t==1:
        k=input("ENTER COMPLETED TASK:")
        add(k)
            
    elif t==2:
        k=input("ENTER TASK NAME TO REMOVE:")
        remove(k)
            
    elif t==3:
        display()
    elif t==4:
        k=input("ENTER SEARCH NAME OF TASK TO SEARCH:")
        search(k)
            
    elif t==5:
        print("-----------------------------EXITED SUCCESSFULLY------------------------------")
        break
    else:
        print("INVALID")
        
    
            
            
            
