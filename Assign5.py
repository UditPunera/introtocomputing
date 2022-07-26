Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# question-1------------------------------------------------------------------------------------------------------------------
print("ANS.1")
string = input("Enter the the string :")
print(string[::-1])

# question-2-------------------------------------------------------------------------------------------------------------------
print("ANS.2")
x = int(input("Enter the minimum value :"))
y = int(input("Enter the maximum value: "))
num = int(input("Enter the number for divisibility check :"))
i = x
while i <= y:
    if i % num == 0:
        print(i)
    i += 1

# question-3--------------------------------------------------------------------------------------------------------------------
print("ANS.3")
a = float(input("Enter the length of side:"))
b = float(input("Enter the length of side:"))
c = float(input("Enter the length of side:"))
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    ar_tri = (s * (s - a) * (s - b) * (s - c)) ** (0.5)
    print(ar_tri)
else:
    print("Error")

# question-4--------------------------------------------------------------------------------------------------------------------
print("ANS.4")
n = int(input("Enter the no. of rows :"))
t = (n // 2) + 1
l = n // 2
for i in range(1, t + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
for q in range(l, 0, -1):
    for r in range(q, 0, -1):
        print("*", end="")
    print()

# question-5---------------------------------------------------------------------------------------------------------------------
print("ANS.5")
row = int(input("Enter the number of rows"))
n = 0

for i in range(0, row + 1):

    for j in range(i):
        if n == 26:
            n = 0
        else:
            pass
        y = chr(65 + n)
        print(y, end="")
        n += 1
    print("")

# question-6---------------------------------------------------------------------------------------------------------------------------------
print("ANS.6")
lower_value = int(input("Enter the Lowest Range Value : "))
upper_value = int(input("Enter the Upper Range Value : "))  # input from user the lowest and the upper range

print("The Prime Numbers in this range are : ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):  # Check for each number if it has any factor between 1 and itself
            if (number % i) == 0:  # if YES, the code will move on
                break
        else:
            print(number)  # if NO, the code prints the number

# question-7---------------------------------------------------------------------------------------------------------------------------------
print("ANS.7")
accum = []
for i in range(1, 500):
    if i % 7 == 0 and i % 11 == 0:
        accum.append(i)
print("The numbers divisible by 11 and are multiple of 7 are :", accum)

# question-8----------------------------------------------------------------------------------------------------------------------------------
print("ANS.8")
pos = []
neg = []
odd = []
even = []
times = {}
li = []
for i in range(10):
    num = int(input("Enter the number "))
    li.append(num)
    if num >= 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num not in times:
        times[num] = 1
    else:
        times[num] += 1
print("Positive numbers are: ", pos)
print("Negative numbers are: ", neg)
print("Even numbers are: ", even)
print("Odd numbers are: ", odd)
print("Number of times each number occurs in the List", times)

# question-9---------------------------------------------------------------------------------------------------------------------------------------
print("ANS.9")
n = int(input("Number of words: "))
li = []
for i in range(n):
    word = input("Enter the word: ")
    li.append(word)
times = {}
for i in li:
    if i not in times:
        times[i] = 1
    else:
        times[i] += 1
print("Number of occurences: ", times)
"""
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

===== RESTART: C:/Users/Divyanshu/OneDrive/Desktop/Assignment 5 input Q.py =====
ANS.1
Enter the the string :ELEPHANT
TNAHPELE
ANS.2
Enter the minimum value :2
Enter the maximum value: 80
Enter the number for divisibility check :8
8
16
24
32
40
48
56
64
72
80
ANS.3
Enter the length of side:5
Enter the length of side:8
Enter the length of side:9
19.8997487421324
ANS.4
Enter the no. of rows :9
*
**
***
****
*****
****
***
**
*
ANS.5
Enter the number of rows5

A
BC
DEF
GHIJ
KLMNO
ANS.6
Enter the Lowest Range Value : 1
Enter the Upper Range Value : 86
The Prime Numbers in this range are : 
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
ANS.7
The numbers divisible by 11 and are multiple of 7 are : [77, 154, 231, 308, 385, 462]
ANS.8
Enter the number 98
Enter the number -88
Enter the number -65
Enter the number -43
Enter the number 91
Enter the number 73
Enter the number 28
Enter the number 64
Enter the number 98
Enter the number 91
Positive numbers are:  [98, 91, 73, 28, 64, 98, 91]
Negative numbers are:  [-88, -65, -43]
Even numbers are:  [98, -88, 28, 64, 98]
Odd numbers are:  [-65, -43, 91, 73, 91]
Number of times each number occurs in the List {98: 2, -88: 1, -65: 1, -43: 1, 91: 2, 73: 1, 28: 1, 64: 1}
ANS.9
Number of words: 8
Enter the word: SKY
Enter the word: SLEEP
Enter the word: OPEN
Enter the word: CLOSE
Enter the word: OPEN
Enter the word: SLICE
Enter the word: LIVE
Enter the word: SLICE
Number of occurences:  {'SKY': 1, 'SLEEP': 1, 'OPEN': 2, 'CLOSE': 1, 'SLICE': 2, 'LIVE': 1}
"""