a=float(input("a  "))
z1=str(input("(+;-;*;/)  "))
b=float(input("b  "))
z2=str(input("(+;-;*;/)  "))
c=float(input("c  "))

def kalk(a,b,c,z1,z2):
    if z1=="/" and z2=="/":
        e=a/b/c
    elif z1=="/" and z2=="*":
        e=a/b*c
    elif z1=="/" and z2=="+":
        e=a/b+c
    elif z1=="/" and z2=="-":
        e=a/b-c

    if z1=="*" and z2=="/":
        e=a*b/c
    elif z1=="*" and z2=="*":
        e=a*b*c
    elif z1=="*" and z2=="+":
        e=a*b+c
    elif z1=="*" and z2=="-":
        e=a*b-c

    if z1=="+" and z2=="/":
        e=a+b/c
    elif z1=="+" and z2=="*":
        e=a+b*c
    elif z1=="+" and z2=="+":
        e=a+b+c
    elif z1=="+" and z2=="-":
        e=a+b-c

    if z1=="-" and z2=="/":
        e=a-b/c
    elif z1=="-" and z2=="*":
        e=a-b*c
    elif z1=="-" and z2=="+":
        e=a-b+c
    elif z1=="-" and z2=="-":
        e=a-b-c
    return e
f=kalk(a,b,c,z1,z2)
print(f)
