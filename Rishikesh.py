#PRINT NUMBERS USING FOR LOOP:-
# for i in range(1, 11):
#     print(i)

# for i in range(2, 51, 2):
#     print(i)
#================================================================================
#TUPLE:-
# student_info = ("Suraj Singh", 48)
# hobbies = {"Vlogging", "", "Cricket"}

# subjectmarks = {
#     "Python": 95,
#     "DBMS": 19,
#     "Data Structures": 88,
#     "Mathematics": 12,
# }

# student_details = [student_info, hobbies, subjectmarks]

# print("Student Information")
# print("Name:", student_details[0][0])
# print("Roll Number:", student_details[0][1])

# print("\nHobbies:")
# for hobby in student_details[1]:
#     print("-", hobby)

# print("\nSubject Marks:")
# for subject, marks in student_details[2].items():
#     print(subject, ":", marks)
#================================================================================
#LIST:-
# list = ["Apple","Banana", "mango"]
# list.clear()
# print(list)

#APPEND:-
# fruits = ["apple", "banana"]
# fruits.append("orange")

# print(fruits)
#================================================================================
#
# name = input("enter yor name:")
# age = int(input("enter your age:"))
# print("Name:",name)
# print("Age:",age)
#================================================================================
#ADDITION,MULTIPLICATION,DIVISION,MODULAR,SUB:-
# a = int(input("(enter your value"))
# b = int(input("(enter your value"))

# sum = a+b
# print("sum",sum)
#==
# a = int(input("(enter your value:"))
# b = int(input("(enter your value:"))

# print("Addition:", a + b)          
# print("Subtraction:", a - b)       
# print("Multiplication:", a * b)    
# print("Division:", a / b)          
# print("Modulus:", a % b)
#================================================================================
#While Loop:-

# battery = int(input("Enert your battery:"))
# while battery < 100:
#     print(f"changing...{battery}%")
#     battery = battery +1
# print("Phone is fully charged!")

# pin = ""
# while pin != "1234":
#     pin = input("Enter your 4-digit PIN:")
# if pin != "1234":
#     print("incorrect pin pls try again!")

# print("correct PIN! Access Granted")
#================================================================================
#break statment:-

# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)

#continue

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

#Pass

# for i in range(1,6):
#     if i == 3:
#         pass
#     print(i)
#================================================================================
#EXP5:- write a program for an ATM:
        #If the user enters 0, stop the ATM using break.
        #If the user an invalid amount, skip the transaction using continue.
        #If the withdrawl amount is more than 10,000, use pass.

# print("ATM Withdral Sytmes")

# while True:
#     Amount = int(input("\n Enter Withdrawal amount(0exit):"))
#     if Amount == 0:
#         break
#     if Amount < 0:
#         print("Invalid amount!")
#         continue
#     if Amount > 10000:
#         pass
#     print("withdrawal amount $", Amount)
#     print("\n Thank you for using the ATM")
#================================================================================
#All ARE FUNCTION:-

# def welcome():
#     print("Welcome to Python")
# welcome()

#Function with one Parameter:

# def greet(name):
#     print("Hello", name)
# greet("Rahul")

#Function with Two Parameters:

# def add(a,b):
#     print(a+b)
# add(10, 20)

#Funtion using user 

# def add (a, b):
#     print(a+b)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# add(a, b)

#Based on their Position Arguments:

# def student(name, age):
#     print("Name:",name)
#     print("Age:", age)
# student("Rahul", 22)

#Keyword Arguments:

# def student(name, age):
#      print("Name:",name)
#      print("Age:", age)
# student(age = 20, name = "Rahul")

#Variable-Length Arguments(*args): user this when you don't know many values the user will pass.

# def add(*numbers):
#     print(numbers)
# add(10, 20)
# add(10, 20, 30)
# add(1, 2, 3, 4, 5)

# def add(*numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     print(total)
# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40)

#Lambda Function (Anonymous Function)

# square = lambda x: x * x
# print(square(5))

#Built-in Function

numbers = [10, 20, 30, 40]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))