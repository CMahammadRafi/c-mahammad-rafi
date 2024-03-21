#) Tasks
# Write the code for the belwo tasks using function
# 1.) d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 'S'

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6] 
# n=2 --> [5, 6, 1,2,3,4]
# n=3--> [4,5,6, 1,2,3]

# ! method riding
# * polymorphism in classes using inheritance

# ? Eg:1

# class bank:
#     def ratio(self):
#         print("all banks has repo rate")

# class SBI(bank):
#     def ratio(self):
#         print("SBI rate is 9%")


# class IOB(bank):
#     def ratio(self):
#         print("IOB rate is 7.5%")

# i = IOB()
# i.ratio()

# s = SBI()
# s.ratio()

# ? Eg:2
# class usa:
#     def language(self):
#        print("english")

#     def capital(self):
#         print("washington dc")

# class india(usa):
#     def language(self):
#         print("none")

#     def capital(self):
#         print("new delhi")

# i = india()
# i.language()
# i.capital()

# Eg:3
# polymorphism using objects

# c1, c2 --> c1 = print(c1), print(c2)
# f1, f2

# class c1:
#     def fl(self):
#         print("class 1")

# class c2:
#     def f1(self):
#         print("class 2")

# obj1 = c2()
# obj1.f1()

# obj2 = c2()
# obj1.f2()

# * Eg:4
# class c1:
#     def f1(self):
#         print("class 1")

# class c2(c1):
#     def f1(self):
#         print("class 2")

# obj1 = c2()
# obj2 = c1()

# def display(a):
#     a.f1()
# display(obj1)
# display(obj2)

# * changing the functionality of buit in function
# a = 9
# b = 6
# print(a+b)
# print(a.__add__(b)) #? dunder method or mafic method
# print(a.__sub__(b))
# print(a.__mul__(b))

# ! Eg:5

# class shopping:
#    def __init__(self, l1):
#         self.items = l1

#     def __len__(self):
#         length = len(self.items)
#         return length
# s = shopping([1,2,3,4,5])
# print(len(s))

# ! ---> method overloading
# !  Eg:1
class suming:
    def add(self, a, b):
        print(a+b)
        
    def add(self, a, b, c):
         print(a+b+c)

s = suming()
# s.add(4, 3) # ! ----> error
s.add(4, 5, 1)



















    
