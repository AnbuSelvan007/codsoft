print("--------/\/\PASSWORD GENERATOR/\/\----------")
import random
pas_range=int(input("ENTER THE LENGTH OF PASSWORD:"))
password=""
for i in range(pas_range):
    lwr="abcdefghijklmnopqrstuvwxyz"
    upr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smp="!@#$&*"
    num="1234567890"
    rand_choice=random.choice([lwr,upr,smp,num])
    rand_onechoice=random.choice(rand_choice)
    password+=rand_onechoice
print("---------------------------------------------")
print("/tYOUR PASSWORD:",password)
print("---------------------------------------------")
