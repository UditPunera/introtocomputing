#Que-6

a=int(input("Enter first number="))
b=int(input("Enter second number="))

c=a^b
count = 0
while c:
     c = c & (c - 1)     
     count = count + 1
 
print("Number of bits needed to be flipped to convert a to b is:",count)
