'''
variables
'''
# a=7, 8
# print(a)
# print(type(a))

# a, b, c = 9, 8, 7, 8
# print(a, b, c)

# a, b=c=7, 8
# print(a)
# print(b)
# print(c)

# a=b, c=4, 2
# print(a, b, c,)

# ----> swapping of variables
# a = 7
# b = 5

# Eg:1
# temp=a #temp= 7
# a=b    #a=5
# b=temp #b=7

# # a=5, b=7
# print(a, b)

# Eg:2
# a=a+b #a=12
# b=a-b #b=12-7=5
# a=a-b #a=12-5=7

# print(a, b)

# a, b=b, a # only in python
# print(a, b)

# a=a*b #a=35
# b=a/b #b=35/7 = 5.0
# a=a/b #a=35/5 = 7.0
# print(int(a), int(b))

# id() --. used to find the memory 
# a = 7
# b = 8
# print(a)
# print(id(a))
# print(id(b))

# -----> keywords
#keywords are reserved words which provides special meaning to compiler or interpretor

# import keyword
# print(keyword.kwlist)
# print(type(keyword.kwlist))

# to check if the string is keyword or not
# print(keyword.iskeyword("sid")) # false

# if = 8
# print(if) # error coz if is a keyword

# !----> literals
# literal is the constant value assigned to a variable
# A variable is considers to be constant when it is defines in constant

# a= 78 # a is variable
# A= 78 # A is constant

# hash()---> it creates has value for constant datatypes and
# provides error for non constant datatypes

# n1 = 89+7j
# print(hash(n1))

# f1 = (7, 8, 9)
# print(hash(f1)) # error --> list non-constant or mutable datatypes

#! ---> operators
# operators are symbols which is used to perform various operation
# between 2 or more operations

# Arithmatic poperator
# Logical operator
# relational or comparision operator
# identify operator
# membership operator 

# todo ---> arithmatic --> +, -, *, /, ? , %, //, **
# Eg:1
# a = 8
# b = 9
# c = 10
# print(a+b+c)

# input() --> used to get the runtime input
# eval()--> used to get the runtime values of all datatype
# n1 = eval(input("enter the value: "))
# print(type(n1))

# a = 4
# b = 2
# print(a/b) # is used to get the quotient value
# print(a%b) # IS used to get the remainder value

# ! // ---> floor division

# a = 765433
# b = 19
# print (a//b) # -> the output will be in integer & the output
# based on floor value

# ! ** --> used for a power of a number
# print(2**4) # --> 16

# ! aasignment --> +-=, -=, /=, *=, //=, **=, &=, |=, %=
# a= 8
# a+=2
# print(a)

# a=30
# a-=5
# print(a)

# ! comparision --> ==, >, <, !=, <=, >=
# a = 8
# b = 7
# print(a>b) # true

# a = 9
# b = 5
# print(a==b)

# ! bitwise operator --> &, |, ^, ~, <<, >>
# a = 7
# b = 4
# print(a|b)

# 2^4 2^3 2^2 2^1 2^0
#  8    4    2    1

#  0    1    1    1  #--> 7
#  0    1    1    0  #--> 6 &
#  --------------------
#  0    1    1    0 # ---> 7

# AND
# A B A&B
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

# OR
# A B A|B
# 0 0 0
# 0 1 0
# 1 0 1
# 1 1 1

# ~ --->
# a = 9876
# print(~a)
# a = 9

# 128 64 32 16 8 4 2 1
# 0   0  0  0 1 0 0 1 # --> 9
# 1   1  1  1 1 0 11 0 # --> -10
# 0  0 0  0  1  0 1 0 --> 10

# 1 1 1 1 10 1 0 1s complement of 10
               # 2s compi,ent
 
# ---------------------
# 1 1 1 1 0 1 1 0 --> -10


# ! logical operator --> used to compare the expressions
# and, or , not
# a = 6
# print(a>3 and a<10)
# print(a>7 or a<30)
# print(not(a>8 and a<10))

#! identity operator
# ? it is used to compare the memory location that the values
# ? are stored 
# is, is not
# a = 8
# b = 8
# print(a is b)
# print(a==b)

# a = (1, 2, 3)
# b = (1, 2, 3)
# print(a is b)

# ! membership operator
# in, not in
# l1 = [7, 8, 9, 0, 6, 5]
# num = 55
# print(num in l1)
# print(num not in l1)

# num = 678
# print(8 in num)# error

# ! conditional statements
# if, elif, else

# python syntax
# if condition:
#    statement
#    statement
#    statement
# statement

# eg:1
# a = 6
# if a:
#     print("hello")


# Eg:2
# a = 6
# if a>3:
#     print("hey")
# else:
#     print("no")

# Eg:3
# if 7>8:
#     print("hello")
# else:
#     print("yes")

# a number is even or odd
# n = int(input("enter the number:  "))
# if n %2==0:
#     print(n, "is even")
# else:
#     print(n, "is odd")

# sum: 2
name = input("enter the name: ")
age = int(input("enter the age: "))
nationality = input("enter the nation: ")

if age>18 and nationality== "indian" :
    print("eligible for vote")
else:
    print("not eligible")





 
 






