import random
i=1
print("_______________________WELCOME TO ROCK PAPPER SISSOR GAME______________________\n")
p=input("enter [r] for rock,[p] for paper,[s] for sissor,[e] for exit:")
l="rRPpSseE"
if(p not in l):
    print("invalid")
    p=input("enter [r] for rock,[p] for paper,[s] for sissor,[e] for exit:")
if p=="e" or p=="E":
    print("                        SUCCESSFULLLY EXITED")
    i=2
a=0
b=0
while(i==1):
    l="rRPpSs"
    if(p not in l):
        print("invalid")
        p=input("enter [r] for rock,[p] for paper,[s] for sissor,[e] for exit:")
        if p=="e" or p=="E":
            print("                        SUCCESSFULLLY EXITED")
            break
    if(p=="r" or p=="R"):
        k="rock"
        p="r"
    if p=="p" or p=="P":
        k="paper"
        p="p"
    if p=="s" or p=="S":
        k="sissor"
        p="s"     
    c=["rock","paper","sissor"]
    s=random.choice(c)
    #s-computer and k-player
    if s==k: 
        if p=="r":
            print("                 YOU:ROCK | COMPUTER:ROCK")
        elif p=="p":
            print("                 YOU:PAPPER | COMPUTER:PAPPER")
        else:
            print("                 YOU:SISSOR | COMPUTER:SISSOR")
        print("                 ******DRAW******")
    elif s=="rock":
        if k=="paper":
            print("                 YOU:PAPER | COMPUTER:ROCK")
            print("                 *****YOU WON:)*****")
            a+=1
        if k=="sissor":
            print("                 YOU:SISSOR | COMPUTER:ROCK")
            print("                  *****YOU LOSE:(*****")
            b+=1
    elif s=="paper":
        if k=="rock":
            print("                 YOU:ROCK | COMPUTER:PAPPER")
            print("                 *****YOU LOSE:(*****")
            b+=1
        if k=="sissor":
            print("                 YOU:SISSOR | COMPUTER:PAPPER")
            print("                  *****YOU WON:)******")
            a+=1
    elif s=="sissor":
        if k=="rock":
            print("                 YOU:ROCK | COMPUTER:SISSOR")
            print("                  ******YOU WON:)*****")
            a+=1
        if k=="paper":
            print("                 YOU:PAPPER | COMPUTER:SISSOR")
            print("                  *****YOU LOSE:(*****")
            b+=1
    print("              \n                       YOUR POINT:",a,"COMPUTER POINT:",b)
     
    if a==5:
        print("<<<<<<<<<<<<<<<<<<<YOU WON>>>>>>>>>>>>>>>>>>")
        i=2
    if b==5:
        print("<<<<<<<<<<<<<<<<<<<COMPUTER WON>>>>>>>>>>>>>>>>>>")
        i=2
    else:
        print("____________________________________________________________________________\n") 
    p=input("\nenter [r] for rock,[p] for paper,[s] for sissor,[e] for exit:")
    l="rRPpSseE"
    if(p not in l):
        print("invalid")
        p=input("enter [r] for rock,[p] for paper,[s] for sissor,[e] for exit:")
        
    if p=="e" or p=="E":
        print("                         SUCCESSFULLLY EXITED")
        i=2
    
        
       
    
    
