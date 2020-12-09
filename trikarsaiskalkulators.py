
a=float(input("a  "))
z1=input("dl/rz/pl/mn  ")
b=float(input("b  "))
z2=input("dl/rz/pl/mn  ")
c=float(input("c  "))

def kalk(a,b,c,z1,z2):
    if z1=="dl" and z2=="dl":
        e=a/b/c
    elif z1=="dl" and z2=="rz":
        e=a/b*c
    elif z1=="dl" and z2=="pl":
        e=a/b+c
    elif z1=="dl" and z2=="mn":
        e=a/b-c

    if z1=="rz" and z2=="dl":
        e=a*b/c
    elif z1=="rz" and z2=="rz":
        e=a*b*c
    elif z1=="rz" and z2=="pl":
        e=a*b+c
    elif z1=="rz" and z2=="mn":
        e=a*b-c

    if z1=="pl" and z2=="dl":
        e=a+b/c
    elif z1=="pl" and z2=="rz":
        e=a+b*c
    elif z1=="pl" and z2=="pl":
        e=a+b+c
    elif z1=="pl" and z2=="mn":
        e=a+b-c

    if z1=="mn" and z2=="dl":
        e=a-b/c
    elif z1=="mn" and z2=="rz":
        e=a-b*c
    elif z1=="mn" and z2=="pl":
        e=a-b+c
    elif z1=="mn" and z2=="mn":
        e=a-b-c
    return e
f=kalk(a,b,c,z1,z2)
print(f)
