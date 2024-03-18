# ----> while loop
# ----> break using while loop
# Eg:1
# 1.) iterate from 20 to 30 and break the loop in 27

# i = 20
# while i<31:
#    if i == 27:
#        break
#     print(i)
#     i+=1

# Eg:2
# i = 20
# while i<31:
#    print(i)
#    i+=1
#    if i == 27:
#       break


# 3.) 
# i = 20
# while i<31:
#     print(i)
#     if i == 27:
#         break
#     i+=1

# 4.) 
# i = 20
# while i<31:
#     if i==27:
#         print(i)
#         break
#     i+=1

# -----> continue
# ---> Eg:1
# i = 20
# while i<31:
#     i=i+1
#     if i==27:
#         continue
#     print(i)

# while to iterate from 12 to 22
# find the sum of all numbers

# i = 12
# sum = 0
# while i<23:
#        sum=sum+i
#        i+=1
# print(sum)

# ! Eg:
# find the average of value from 20 to 25

# i = 20
# sum = 0
# count = 0
# while i<=30:
#     sum=sum+i
#     count+=1
#     i+=1
# print(count)
# print(sum/count)

# ----> Nested for loop
# Eg:1

# for row in range(1, 3):
#     for col in range(1, 4+1):
#         print(row, col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

# for row in range(1):
#     for col in range(4):
#         print("*", "*", "*", "*")
#    print()

# rows = int(input("enter the rows"))
# cols = int(input("enter the cols"))
# for row in range(rows):
#     for col in range(cols):
#         print("*", end=" ")
#     print()    


# for row in range(5):
#     for col in range(5):
#         print(row, end=" ")
#    print()

# sum = 0
# for row in range(5):
#     for col in range(5):
#         sum= sum+1
#         print(sum, end=" ")
#     print()

# for row in range(0, 6):
#     for col in range(0, row):
#         print("*", end=" ")
#     print()

# for row in range(0, 5):
#     for col in range(row, 5):
#         print("*", end=" ")
#     print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# for row in range(5):
#     for col in range(5):
#         if col==0 or col==5-1 or row ==0 or row ==5-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#     *
#    * *
#   * * *
#  * * * *

# for row in range(0, 5):
#     for col in range(0, 6):
#         if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4))or
#                                   (row==2 and (col>=1 and col<=5))):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# ----> List
# ! ---> datatypes
# primary

# number --> int, float complex
# string
# boolean
# none

# collection
# list
# tuple
# set
# dictionary

# ! --->List
# 1.) if the collection of elements are sorounded by square brackets, it is considered to be list
# ! Eg:1
    # l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9 ,0]]

# characteristics of list
# 1.) list have to be sorounded by []
# 2.) it is mutable (the elements in the list are changable)
# 3.) every element inside list is indexed
# 4.) the elements inside the list will be orderd format
# 5.) it can hold duplicate values
# 6.) it is heterogeneous

# To access the elements in the list
lst1 = [1, 4, 1, 89.7, 7.5, "p", "i"]
# print(l1)

# ---> indexing
# the collection datatypes like list, tuple, string, the ellements will be alloted with predefines unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side 

# Positive indexing
# print(lst1[0])
# print(lst1[4])
# print(lst1[6])

# ? --> Negative indexing
lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1[-1])
print(lst1[-5])



