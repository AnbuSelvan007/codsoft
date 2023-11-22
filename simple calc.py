def add(a,b):
    print("-----------------------------")
    print(a,"+",b,"=",a+b)
    print("-----------------------------")
def sub(a,b):
    print("-----------------------------")
    print(a,"-",b,"=",a-b)
    print("-----------------------------")
def multi(a,b):
    print("-----------------------------")
    print(a,"*",b,"=",a*b)
    print("-----------------------------")
def div(a,b):
    print("-----------------------------")
    print(a,"/",b,"=",a/b)
    print("-----------------------------")
def rem(a,b):
    print("-----------------------------")
    print(a,"",b,"=",a%b)
    print("-----------------------------")
def power(a,b):
    print("-----------------------------")
    print(a,"**",b,"=",a**b)
    print("-----------------------------")
print("--------WELCOME TO SIMPLE CALCULATOR----------")
while(1):
    try:
        c=int(input("[1 FOR ADDITION],\n[2 FOR SUBTRACTION],\n[3 FOR MULTIPLICATION],\n[4 FOR DIVISION],\n[5 FOR REMINDER],\n[6 FOR POWER],\n[7 FOR EXIT]\nENTER YOUR CHOICE:"))
    except:
        c=int(input("ENTER VALID VALUE:"))
    if c==7:
        print("------------------SUCCESSFULLY ENDED--------------------------------")
        break
    try:
        a,b=map(int,input("ENTER VALUE OF A AND B SEPERATED BY SPACE:").strip().split())
    except:
        a,b=map(int,input("ENTER ONLY TWO NUMBERS SEPERATED BY SPACE FOR A AND B:").strip().split())
    if (c==1):
          add(a,b)
    elif c==2:
        sub(a,b)
    elif c==3:
        multi(a,b)
    elif c==4:
        if b==0:
            b=int(input("ENTER NON ZERO VALUE FOR B:"))
        div(a,b)
    elif c==5:
        rem(a,b)
    elif c==6:
        power(a,b)
   
    
