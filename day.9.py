# 1.)find uncommon words from 2 strings
# s1 = "hello how are you"
# s2 = "hello how is"

# s1 = "hello how are you"
# s2 = "hello how is"

# s1 = s1.split(" ")
# s2 = s2.split(" ")

# for val in s1:
#     if val not in s2:
#         print(val)
# for val in s2:
#     if val not in s1:
#         print(val)

# 2.)write a  code print the 8th fibanochi number
# 0, 1, 1, 2, 3, 5, 8

# n1 = 0
# n2 = 1
# ans = 0+1=1

# n1 = 1
# n2 = 1
# ans = 1+1=2

# n1 = 1
# n2 = 2
# ans = 1+2=3

# n1 = 2
# n2 = 3
# ans = 2+3=5

# find the 8th fibanochi number

# num = 8
# n1 = 0
# n2 = 1

# for val in range(num):
#     ans = n1+n2
#     n1 = n2
#     n2 = ans
# print(ans)

# ! constructors
# ? Eg:2

#unparametarised constructor
# class profile:
#     def __init__ (self):
#         print("hello world")
# obj =profile()
# obj.__init__()

# ? Eg:3
# * parametarised constructor
# class profile:
#     def __init__(self, id, name, age):
#        print(id, name, age)
# obj = profile(1, "rafi", 22)

# ? Eg:4
# class c1:
#     email = "rafi@gmail.com"

#     def m1(self):
#         name = "rafi"
#         place= "cbe"
#         print(name, place)
#         print(self.email)

# object = c1()
# object.m1()

# ? Eg:5
# class c1:
#     def m1(self):
#         name = "rafi"
#         age = 22
#         return name, age
#     def display(self):
        # ! print(name, age)
        # ! print(self.name, self.age)
#         print(self.m1())
# object = c1()
# object.display()
        
# ! Eg:6
# ? to use the variable inside the constructor in another methods
# class class1:
    # email = "rafi@gmail.com"   #static variable
#     def __init__(self):
#         self.name = "rafi"    #instatic variable
#         self.email = "rafi@gmail.com"
#         # return name, email # error ---> cannot use return with constructor


#     def display(self): # instance method
#         print(self.name, self.email)
# c1 = class1()
# c1.display()


# ! ------> Inheritance
# the process of utilising the methods and attributes of parent class
# throughout the object of child class it is called as inheritance

# 5 types of inheritance
# single inheritance
# multilevel inheritance
# multiple inheritance
# hybrid inheritance
# heirarichal inheritance

# * single inheritance
# it has only one parennt class and only one child class
# ! Eg:1
# class parent:
#     def m1(self):
#         print("iam parent class")

# class child(parent):
#    def m2(self):
#        print("iam child class")

# obj = child()
# obj.m1()

# ! Eg:2
# class c1:
#     def __init__(self):
#         print("iam constructor from parent class")

# class child1(c1):
#     pass

# obj = child1()

# ! Eg:3
# class parent:
#     name = "rafi"

# class child(parent):
    
#     def display(self):
#         print(self.name)
# d = child()
# d.display()

# ! multilevel inhritance
# ? Eg:1
# class voice:
#     def sound(self):
#         print("all the animals have their own voice")
        
# class dog(voice):
#     def dog_voice(self):
#         print("bark")
        
# class cat(dog):
#     def cat_voice(self):
#         print("meow")
        
# class parrot(cat):
#     def parrot_voice(self):
#         print("speak")

# all = parrot()
# all.dog_voice()
# all.cat_voice()
# all.sound()
# all.parrot_voice()

# ! multiple inheritance
# ? it has mulipe parent and 1child
              
# class white_petrol:
#     def function_w(self):
#         print("used to airplans")

# class organic_petrol:
#     def function_o(self):
#         print("used for bikes, cars")

# class premium_petrol:
#     def function_p(self):
#         print("sports cars, bikes")

# class petrol(white_petrol, organic_petrol, premium_petrol):
#     def defanition(self):
#         print("petrols types")

# p = petrol()
# p.defanition()
# p.function_o()

# ! Eg:2
# MRO --> Method resolution Order
# class addition:
#     def add(self, a, b):
#         print(a+b)
        
#     def mul(self, a, b):
#         print(a%b)
        
# class subract:
#     def sub(self, a, b):
#         print(a-b)
# class multiply:
#     def mul(self, a, b):
#         print(a*b)
# class division(addition, subract, multiply):
#     def div(self, a, b):
#         print(a/b)
        
# calc = division() 
# calc.add(3, 4)
# calc.mul(4, 2)

# ! heirarical inheritance
# class catagory:
#     def weight(self, weight):
#         print(weight)
        
#    def display(self, taste, color):
#          print(color, taste)
    
# class tomato(catagory):
#     def tomato_specs(self):
#         color="black"
#         taste = "neutral taste"
#         self.display(color, taste)

# class carrot(catagory):
#     def carrot_specs(self):
#         color="green"
#         taste = "sweet"
#         self.display(color, taste)
        
# c = carrot()
# c, =carrot_specs()
# c.weight("30gms")

# t = tomato
# t.tomato_specs()
# t.weight("20gms")

# ! hybrid inheritance
# ? the combination of above 4 inheritance is called hybrid inheritance
# class c1:
#     def m1(self):
#         print("class 1")
        
# class c2(c1):
#     def m2(self):
#         print("class 2")        

# class c3(c2):
#    def m3(self):
#         print("class 3")        
    
# class c4(c2):
#     def m4(self):
#         print("class 4")
      
#     def m3(self):
#         print("iam m3 from c4")
           
# class c5(c4):
#     def m5(self):
#         print("class 5")

# class c6(c5, c4, c2, c1):
#     def m6(self):
#         print("class 4")
# obj = c6()
# obj.m3()

# ! ----------> polymorphism
# poly - many, morph ---> form
# 1 functionality then it is considered to be as polymorphism


# * polymorphism in built in functions
# len()---> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min(()
# count()
# pop()
# and more....

# * polymorphism in operations
# +
# print(8+8)
# print("k"+'1')
# print([1,2,3]+[5,6])

# *
# print(6*7)
# l1 = [1,2,3,4]


        









    
