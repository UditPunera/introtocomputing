Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Question_1:-
"""
M1 = float(input("Enter Your marks:"))
if M1 < 25:
    print("Your Grade is:- F ")
elif 25 <= M1 <45:
    print("Your Grade is:- E ")
elif 45 <= M1 <50:
    print("Your Grade is:- D ")
elif 50 <= M1 < 60:
    print("Your Grade is:- C ")
elif 60 <= M1 < 80:
    print("Your Grade is:- B ")
else:
    print("Your Grade is:- A ")
"""
#Question_2:-
"""
Year = int(input("Enter the Year:"))
if Year % 4 == 0:
    print("A Leap Year.")
elif Year % 100 == 0:
    print("Not a Leap Year.")
elif Year % 400 == 0:
    print("A Leap Year.")
else:
    print("Not a Leap Year.")
"""
#Question_3:-
"""
import random
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    user_output = int(input(f"{num1}X{num2}="))
    if user_output == (num1*num2):
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}")
"""
#Question_4:-
x=200
for candies in range(x):
    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies,'Candies are there in the bowel.')
             break