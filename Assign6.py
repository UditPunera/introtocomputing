Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Q.1
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


print(perfect_number(28))


# Q.2
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if string[left_pos] != string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(isPalindrome('madam'))

# Q.3
# Print Pascal's Triangle in Python
from math import factorial

n = 5
for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    print()

# Q.4
import string, sys


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(ispangram('The quick brown fox jumps over the lazy dog'))

# Q.5
n = input("enter the string: ")
l = n.split('-')
l.sort()
print('-'.join(l))


# Q.6
def student(student_id, student_name, student_class):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'


print(student('21102127', 'Abhishek_Narine', 'B.Tech_1st_year'))


# Q.7
class Student:
    pass


class Marks:
    pass


student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))


# Q.8
class py_solution:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


# Q.9
class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))