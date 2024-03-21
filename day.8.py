# ! Eg:1
# def profile(name, age, place):
#     txt = "my name is {}. iam {} years old. iam from {}."
#     print(txt.format(name, age, place))
# profile("nani", 29, "india")

# ! Eg.2
# ? function with return statement

# return
# 1.) a variable declared inside the function can be accessed
#     outside the function using return
# 2.) return does not print anything
# 3.) we cannot write any code below return statement


# def f1():
#     z = 8
# f1()
# print(z) # error --> cannot use outside the function


# def f1(a, b):
#     c = a*b
#     return c
#   print(f1(6, 8)
# obj = f1(6, 8)
# obj1 = f1(4, 6)         

# def gracemark(object):
#     print(object+4)
# gracemark(obj)
# gracemark(obj1)

# 123
# def palindrome(n):
#     string = str(n)
#     rev = str(n)[::-1]
#     if string==rev:
#         print(n,  "palidrome")
#     else:
#         print("not palindrome")
# a = int(input("enter the value: "))
# palindrome(a)

# ? based on the declaration of parameter an args
# ? functions are divided into 5 categories

# positional args
# keywords args
# default args
# variable length args
# keywords variable length args

# * positional args
# ? the position of a parameter have to be same position as arguments
# ! Eg:1
# def profile(name, phone, marks):
#     txt = "my name is {}. my phone number is {}. i got {} marks."
#     print(txt.format(name, phone, marks))
# profile("nani", 9347614535, 95)

# * keyword args
# ! Eg:1
# ? to overcome the disadvantage of positional args, we use keyword args

# def profile(name, phone, marks):
#     txt = "my name is {}. my phone number is {}. i got {} marks."
#     print(txt.format(name, phone, marks))
# profile(name="rafi", marks=92, phone=9347614535)

# todo --> exception of keyword args function
# def profile(name, phone, marks):
#     txt = "my name is {}. my phone number is {}. i got {} marks."
#     print(txt.format(name, phone, marks))
# profile(name="rafi", 123445567, marks=95) # error -> positional args follow keyword args
# profile(123445567, name="rafi", marks=95) # error --> name has multiple values
# profile("rafi",marks=95, phone=123445567)

# * default args
# the method of assigning the argument to the parameter while declaring the funcion
# ! Eg:1
# def profile(name, phone, place="kadapa"):
#     txt = "my name is {}. my phone number is {}. i am from {}."
#     print(txt.format(name, phone, place))
# profile("rafi", 9347614535)    
    
# ! Eg:2
# def profile(name, place="KADAPA", phone): # error --> coz default args should not
                                          # follow positional parameteres
#     if place == "kadapa" or place=="KADAPA" or place=="kadapa":
#         txt = "my name is {}. my phone number is {}. i am from {}."
#         print(txt.format(name, phone, place))
#     else:
#         print("you are not eligible to signup")
# profile("rafi", 9347614535)

# * variable length parameters
# ! Eg:1
# to pass more than 1 arg to a parameter means we use variable length args
# to convert normal parameter to variable length parm, add *to their prefix of param

# name = "rafi", 'name2', 'name3'
# def profile(*name):
#     for val in name:
#         print("my name is",val)
# profile("rafi", 'name2', 'name3')

# ! Eg:2
# def profile(age , *name,):
#     for val in name:
#         print("my name is",val, "my age is", age)
# profile(28, "rafi", 'name2', 'name3')

# * keyword variable length args
# kwargs --> which is used to provide the args in the form of key value pair.
# ! Eg:1
# def price(**price_list):
#     print(price_list)
# price(shirt=1000, iphone=80000)

# n = 5
# {1:1, 2:4, 3:9, 4:16, 5:25}
# n = int(input("enter the number: "))
# d1 = {}
# for val in range(1, n+1):
#     d1[val] = val**2
# print(d1)

# def dict1(n):
#     d1 = {}
#     for val in range(1, n+1):
#         d1[val] = val**2
#     print(d1)
# dict1(5)

# ! -------> object oriented programming
# the panadigms of objects oriented programming are

# class
# objects
# inheritance
# polymorphims
# abstraction
# encapsulation

# ! class is a blue print of object
#  l1 = [1,2,3,4,5,6]

# ? Eg:1
# class c1:
#     name1 = "nani"
#     print(name1)

# ? Eg:2
# class person:
#     name = "nani"
# c = person()
# print(c.name) 
    
# ? Eg : 3
#creation of method
#when the function is created with a class is called as method

#class person:
#    def display(person):
#        print("Hello welcome to classes")
#p = person()
#p.display()

#? Eg:4
#class person:
#    def display(person, name, age):
#        print(name, age)

#p = person()
#p.display("suri", 28)


# ? Eg: 5
# class person1:
#     fname = "suri"
#     lname = "T"

#     def first_name(self):
#         print(self.fname)

#     def full_name(self):
#         print(self.fname+" "+self.lname)

# p = person1()
# p.first_name()
# p.full_name()

# ? Eg:6
# constructors -->_init_()
# this is a special method which has the ability to excute itself
# without calling it manually through the process of instantiation

# class profile:
#     def_init_(self): # constructor method
#         print("hey")
# p = profile() # through this process

    


    






