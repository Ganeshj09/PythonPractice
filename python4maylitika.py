# -*- coding: utf-8 -*-
"""Python4MayLitika.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1reWej7yNNXEagXsXSUIcBuDtRtYlNdKC

What is Python ?
it is a programming language created by Guido Van Rosum in 1991, it is a high level language interpretted langugae which makes use of Object oriented programming.

General Purpose programming language (GPL)
It can be used in web development(server side), mathematics, Scripting, Softwares and in collaboration with other tech stacks.

Why python ?
1) it is easy to code and understand
2) Versatile or flexible to use
3) Open source and Open/Free software
4) large number of functions and great build in libraries.
"""

print("Hello World!")

Print("Hello World!") #case sensitive

#Comments - non executable lines
#you may write a comment

#Variables - are the pointers to the memory location they can have different values.
#for eg => a = 10 , a = 12 , a - 20

# create variables
#1st Rule) A variable name can not begin with a number
#2nd Rule) A variable can not be created by special sysmbols but only and only underscore
#3rd Rule) a variable can have alphanumeric values
#Assigning value to a variable
#4th Rule) Empty variable can be created by var = None
a = 10
_1var = 12
str1 = '10$' #is this a number or a string => its a string bcoz its in quaotations
string1 = 'hey'
string2 = "hello"
string3 = ''' jsdhgfasjdfsdf
sdfsdfsdfsfsddfsdf'''
print("This is the value of string 1 :",str1)
print(string1)
print(string2)
print()
#assigning multiple values
a, b, c = 12, "Hey there", 34
print(a)
print()
print(b)
print()
print(c)
print(a, c)
#Empty variable
h = None
print(h)
j #does not allow empty variable declaration

#Arithmetic operators
3/2 #used to return the decimal value

3//2 #double division or floor division returns an integer value

4%2

3%2

#Keywords - Fixed or reserved words with a specific meaning which can not be used as a variable

#Data Types
#Immutable data type - Number(integer, float, complex num), String , Tuples
#Tuple creation - ( )
#Tuple can contain both string and numeric data
#tuples allow for duplicate value
fruit_tup = ("grapes", "bananas", "orange", "apples")
print(fruit_tup)
mix_tup = (1,4,7,'a','b','a')
print(mix_tup)
print(mix_tup.index('a'))

#accessing an element in tuple
print(fruit_tup[0])
print(fruit_tup[2])
print(fruit_tup[3])

#fetch the index of bananas from fruit_tup - .index(elementname)
fruit_tup.index('bananas')

#Mutable - Lists, Dictionary, sets
#Lists - []
# they are sequential data type, allow duplicates
#creating a list
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1)
mix_list = ['1', 1, '2', 2, 2]
print(mix_list)

print(list1[2]) # access element 'c'
print(mix_list[1]) #access element int 1

#update c to C
#listname[index at which the value is] = updated value
list1[2] = 'C'
list1

#to check the length = len()
len(list1)

#removing a value
list1.remove('C')

list1

#adding an element to the end of a list => append()
list1.append('C')
list1

list2 = [19, 34, 33, 75, 45, 67, 93]
#sorting the elements
list2.sort()
list2

#printing a list with the help of index
print(list2[0 : 4]) #slicing
print(list2[2:4])
print(list2[0:7:2])

mix_list = ['a', 'b', 1, 3]
mix_list
#if this was entirely alphabetic or numeric then only sortng is possible

list_1 = ['a','b','c','d','e','f','g','h','i']
#print every 3rd element in the list
list_1[0:9:3]

#insert z in between d and e
#listname.insert(index, item/value)
list_1.insert(4, 'z')
list_1

list_1[: : -1]

l1 = ['hi','hey','hello']
l1[ : : -1]

#Dictionary - non sequntial data types there is no specific order in the elements
#Dictionary  = { Key : value }
#dictionaries do not allow for duplicacy in keys
dict1 = {"Year": 2020, "Car_type" : "sedan", "Brand": "Skoda", "color" : "Blue", "y" : 2020}
dict1

#access all keys  and values
dict1.items()

dict1.keys()

dict1.values()

dict1['Year'] #fetching value with the key

#adding a new key pair in dictionary
dict1['Wheel_type'] = "alloy"
dict1

dict1['Wheel_type'] = 'nill'

dict1

del dict1['y']

dict1

#Sets - are mutable data types with immutable elements
#non sequential, duplicates not allowed
#set will be created by = {}
set1 = {1, 43, 9, 18, 30, 30 }
set1

#access an element in sets => can not access individual elements
#there is no indexing no keys
# however can add or remove
set1.add(5)
set1

set1.remove(30)
set1

print("Poped item :", set1.pop())
set1

print("Poped item :", set1.pop())
set1

print("Poped item :", set1.pop())
set1

print("Poped item :", set1.pop())
set1

print("Poped item :", set1.pop())
set1

a = 90
b = 100
#syntax if condition
# if condition : body(inthe next line)
#finding the greater number
if a > b :
  print("A is the greater number :", a)

if b > a :
  print("B is the greater number :" , b)

if a > b :
  print("A is the greater number :", a)
else:
  print("B is the greater number :" , b)

# compare for a if it is greater than or equal to 90
if a >=90 :
    print("A is greater than equal to 90 : ", a)
else:
    print("A is less than 90 : ", a)

a = 20
b = 90
c = 100
#check and print the smallest number
if a > b:
  print("b is smaller")
elif a > c:
  print("c is smaller")
else:
  print("a is the smallest number")

#print the larger or equal number in the above 3 numbers

#print the larger or equal number in the above 3 numbers
if a>=b:
 print("a is larger or equal to b")
elif b>=c:
 print("b is larger or equal to c")
else:
 print("c is the larger number")

if (c>a) and (c > b):
 print("c is greater")
elif (a>c)and (a>b):
  print("a is greater")
else:
 print("b is greater")

#for loop
#iteratable variable - u can give any meaningful short name
set1 = {'a', 'b', 'c', 'd', 'e'}
for i in set1:
  print(i)

a = 100
b = 10
#format- string in print
print( f" the two variables are {a} and {b}")
print(" the two variables are {} and {}".format(b,a))

list1 = ["Anu", "Dheeraj", "Anubhav", "usha", "Rama"]
iter_num = 1
for names in list1:
    print(f"The names from the list are {names} and the iteration number is {iter_num}")
    iter_num += 1

for i in range(11):
  print(i)

count = 0
for i in range(5):
  print(count)
  count = count +1

count = 0
for i in range(5):
  count = count +1  #increment counter
  print(count)

list_num = [1, 2, 3, 4, 5, 6,7 ,8,9 ,10 ]
n = len(list_num) - 1

while n >= 0:
  print(list_num[n]) # put in the same line , end = " " in the print statement
  n = n -1 #decrement counter

counter = 0
while counter < 5:
  print(counter)
  counter = counter + 1 # increment counter

counter = 0
while counter < 5:
  counter = counter + 1 # increment counter
  print(counter)

# functions - built in function are already created
# user defined functions
max(12, 234)

if a > b :
  print(a)

# to create a func def func_name(): function body
def greater_num(): #creating a function
  a = 10
  b = 19
  if a > b :
    print(a)
  else:
    print(b)

greater_num()    #calling a function

def greater_num(a, b): #currently a and b are arguments
  if a > b :
    print(a)
  else:
    print(b)


greater_num(10, 2) # the values are parameters

def cal(a,b, c =0):
  print(f"name is {a}")
  print(f"age is {b}")


cal("Anubhav",19)

cal("rama", 20)

#lambda function
add_lambda = lambda x, y : x+y
add_lambda(123,1342)

#create a list of sqaures from a goven number list
number = [1, 2, 3, 4, 5]
num_func = list(map(lambda x : x**2, number))
print(num_func)

num_func = lambda x : x**2
num_func(4)

min(12, 3123,123, 23 ,4545, 2)

