Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Question:- 1
"""
n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")
"""
#Question:- 2
"""
print("Select an operation to perform : ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()
if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is :" + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is :" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is :" + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The division is :" + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")
"""
#Question:- 3
#import math
"""
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
Ans =(a + b)*(c)
print("Ans =",Ans)

#Q3.b
n = int(input("Enter the value of n :"))
Ans = n*(n-1)/2
print("Ans =",Ans)

#Q3.c
r = str("radius_of_sphere")
Ans = str("4*math.pi*r**2")
print("Ans =",Ans)

#Q3.d
r = str("radius")
Ans = str("math.sqrt(r*(math.cos(a))*2+r(math.sin(a))**2")
print("Ans =",Ans)

#Q3.e
y1 = str("variable 1")
y2 = str("variable 2")
x1 = str("variable 3")
x2 = str("variable 4")
Ans = str("y2-y1)/(x2-x1")
print("Ans =", Ans)
"""
#Question:- 4.a:-
"""
for i in range(5):
    print(i, end = " ")
print()#0 1 2 3 4
#b:-
for i in range(3,10):
    print(i, end=" ")
print()#3 4 5 6 7 8 9
#c:-
for i in range(4,13,3):
    print(i, end=" ")
print()#4 7 10
#d:-
for i in range(15,5,-2):
    print(i, end=" ")
print()#15 13 11 9 7
#e:-
for i in range(5,3):
    print(i, end=" ")
print()
"""
#Question:- 5
"""
print("Molecular weight of a compound of H, C and O atoms :")
H = eval(input("How many hydrogen atoms? "))
C = eval(input("Carbon? "))
O= eval(input("Oxygen? "))
MW= (H * 1.00794) + (C * 12.0107) + (O * 15.9994)
print("Total molecular weight of the compound:", MW)
"""