#Que-5

a=int(input("enter length of first side="))
b=int(input("enter length of second side="))
c=int(input("enter length of third side="))

def is_triangle(a,b,c) :

    return a+b>c and b+c>a and c+a>b

print(is_triangle(a,b,c))
