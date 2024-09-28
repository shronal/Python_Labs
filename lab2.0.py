# # qn 1
# num=int(input("Enter any num to have differenc with 17: "))
# diff=num - 17
# # print("The diff is", diff)
# if num > 17 :
#     print("Matches the question's criteria: ", 2*diff)
# else :
#     print("The number is not greater than 17")

# #EQn 2
# a=int(input("Enter the term:"))
# if a% 2==0:
#           print("The number is even")
# else:
#           print("The number is odd")

# #qn 7
# a=(input("Enter the string: "))
# b=a[::-1]
# print("The reversed string of",a," is", b)

#qn3 
# a=[1,2,3,2,3,4,4,5,64,4]
# print(type(a))
# v=a.count(4)
# print(v)

# a=[1,2,3,2,3,4,4,5,64,4]
# count=0
# for i in range(len(a)):
#     if (a[i]==4):
#         count=count+1
# print("The ", count)

# #qn4
# a,b=4,5
# a,b=b,a
# print("After swapping",a,b)


# #qn no 6
# num1=int(input("The first number is: "))
# num2=int(input("The second number is: "))
# print("""Noob calculator
#      1.Sum
#     2.Difference
#     3.Product
#     4.Quoitent
#     Press the number accordingly""")
# ch=int(input(" "))
# match ch:
#     case 1:
#         print("The sum is", num1+num2)
#     case 2:
#         print("The difference is", num1-num2)
#     case 3:
#         print("The product is", num1*num2)
#     case 4:
#         print("The quotiet is", num1/num2)
#     case _:
#         print("Invalid input")

# qn 8
# spam=int(input("Enter any 1 or 2 or anything you want: "))
# match spam:
#     case 1:
#         print("Hello")
#     case 2:
#         print("Hi")
#     case _:
#         print("Greetings!")

# #qn 10
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# op=100-age
# year=2081+op
# print(f"Hi {name}. In the year {year}, you will turn 100 :)")

# qn 11
# print("""What do you want to convert in:
#       1.degree C to degree F 
#       2.degree F to degree C""")
# ch=int(input("Enter choice: "))
# match ch:
#     case 1:
#         C=int(input("The temp in C is: "))
#         F = C * (9/5) + 32.
#         print(f"The temp of {C}C is {F}F")
#     case 2:
#         F=int(input("The temp in F is: "))
#         C = (F - 32) * 5/9
#         print(f"The temp of {F}F is {C}C")
#     case _:
#         print("Invalid !!")

# #qn 12
# age=int(input("Enter your age: "))
# if age < 12 :
#     print("Child")
# elif age>=13 and age<=19:
#     print("Teenager")
# elif age > 20:
#     print("Adult")

# #qn 13
# string=input("Enter your grade: ")
# match string:
#     case 'A':
#         print(f"The grade for A is 4.0")

#     case 'B':
#         print(f"The grade for B is 3.0")

#     case 'C':
#         print(f"The grade for C is 2.0")

#     case 'D':
#         print(f"The grade for D is 1.0")
    
#     case 'F':
#         print("FAil")


