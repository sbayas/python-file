https://codingcompiler.com/python-coding-interview-questions-answers/



1. Get max consequtive number from the list



num = [1,2,3,4,5,11,12,22,23,14]

# get total number of values

count = 0

for k in num:

    count = count + 1

# Create empty list

a = []

for i in range(0,count):

    if num[i+1] == num[i]+1:

        a.append(num[i])

        if num[i+2] != num[i+1]+1:

            a.append(num[i+1])

            break

print(a)





2. Check prime number



num = int(input("Enter number to check prime or not "))



flag = False



if num > 1:

    for i in range(2, num):

        if (num % i) == 0:

            flag = True

            break

if flag == True:

    print(num, "not prime")

else:

    print(num, "prime")







3. Python program to display all the prime numbers within an interval



lower = int(input("Lower numner is : "))

upper = int(input("Upper numner is : "))



print("Prime numbers between", lower, "and ", upper,  "are:")



for num in range(lower, upper+1):

    if num > 1:

        for i in range(2, num):

            if (num % i) == 0:

                break

        else:

            print(num)





4. Factorial of a Number using Loop



def fact(x):

    if x == 1:

        return 1

    else:

        return (x * fact(x-1))



print("factorial is:", fact(1))





5. Display multiplication table



num = int(input("Table of : "))



for i in range(1, 11):

    print(num,"x",i,"=",num*i)





6. Python Slice()  ==  slice(start, stop, step)



text = "Python Programing"



print(text[slice(6)])



Python



7. # Python zip()



languages = ['Java', 'Python', 'JavaScript']

versions = [14, 3, 6]



print(dict(zip(languages, versions)))





8. Current time using datetime object

 

from datetime import datetime

import pytz

print("current_time_is",datetime.now(pytz.timezone('Asia/Kolkata')).strftime(" %r"))







9. Write a Python Program to Find the Second Largest Number in a List?



a = []

n = int(input("Enter number of elements : "))

for i in range(1,n+1):

    b=int(input("Enter element : "))

    a.append(b)



a.sort()

print("Second largest element is : ",a[n-2])







10. Write a Python Program to Swipe fist and the Second Number in a List?



a=[]

n=int(input("Enter number of elements : "))

for i in range(1,n+1):

    b=int(input("Enter element: "))

    a.append(b)

print(a)



temp=a[0]

a[0]=a[n-1]

a[n-1]=temp

print(a)





11. Write a Python Program to Check if a String is a Palindrome or Not?



string=input("Enter String : ")

if (string==string[::-1]):

    print("Palindrome")

else:

    print("Not Palindrome")







12. Write a Python Program to Count the Number of Vowels in a String?



str=input("Enter String : ")

vovels=0

for i in str:

    if(i=='a' or i=='e'or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):

        vovels=vovels+1

print("Number of vovels are: ",vovels)







13. Write a Python Program to Check Common Letters in Two Input Strings?



s1=input("Enter first string : ")

s2=input("Enter second string : ")

a=list(set(s1)&set(s2))

for i in a:

    print(i)





14. Print second name



name = "Santosh Bayas"

for index in range(0,len(name)):

     if name[index] == " ":

         temp = index

for i in range(temp+1, len(name)):

    print(name[i], end=", ")





15. Print the Fibonici number - [0,1,1,2,3,5,8]



Answer:- 1. Using while loop



n1=0

n2=1

num=int(input("Enter number for fibbonici : "))

count=0

while count < num:

    print(n1)

    sum=n1+n2

    n1=n2

    n2=sum

    count = count + 1



Answer:- 1. Using foor loop



n1=0

n2=1

num=int(input("Enter number for fibbonici : "))

for i in range(0,num):

    print(n1)

    add=n1+n2

    n1=n2

    n2=add



16. Python Program to find sum of array



  == with while loop



a = []

count = 0

while count < 5:

    print(count+1,end="")

    b = int(input(". Enter number : "))

    a.append(b)

    count = count + 1

print("Added numbers are : ",a)

a = list(a)

count = 0

for i in range(0,len(a)):

    count = count + a[i]

print("Sum of the array is : ",count)



 == with for loop



a = []

for i in range(5):

    print(i+1,end="")

    b = int(input(". Enter number : "))

    a.append(b)

    

print("Added numbers are : ",a)

a = list(a)

count = 0

for i in range(0,len(a)):

    count = count + a[i]

print("Sum of the array is : ",count)





17. Python Program for array rotation



def rotateArray(a, n, d):

    print("Elements are : ",a)

    # first store first d elements in temp array

    temp = []

    for i in range(d):

        temp.append(a[i])

    print("temp elements are : ",temp)

    # Now add other elements in data array

    data = []

    for i in range(d,n):

        data.append(a[i])

    #print("data elements are : ",data)

    # Now extend data array with temp array

    for i in range(d):

        data.append(temp[i])

    print("Now, elements after rotation are ; ",data)



a = [4,2,31,1,321,645]

a.sort()

n = len(a)

d = 2



rotateArray(a,n,d)





18. Python Program for Find remainder of array multiplication divided by n



a = [100,10,5,25,35,14]

count = 1

n = 11

for i in range(len(a)):

    count = count * a[i]

print(count%n)





19. Reversing a List in Python



a = [23, 65, 19, 90]

# Reversing a list using the slicing technique

print(a[::-1])

b = []

# Reversing a list using the insert() function

for i in a:

    b.insert(0,i)

print(b)

        



20. Python program to find sum of elements in list





a = [12, 15, 3, 10]

#Output: 40

total = 0

for i in range(0,len(a)):

    total = total + a[i]

print(total)



21. Python | Multiply all numbers in the list



a = [12, 15, 3, 10]



def mul(list):

    result = 1

    for i in range(len(list)):

        #print(list[i])

        result = result * list[i]

    print(result)

    

mul(a)



22. Python program to find N largest elements from a list



l = [1000,298,3579,100,200,-45,900]

n = 4

l.sort() 

print(l)

print(l[-n:])



23. Python program to print even numbers in a list



a = [12, 14, 95, 3]

#Output: [2, 64, 14]

b = []

for i in range(len(a)):

    if a[i] % 2 == 0:

        b.append(a[i])

print(b)





24. Python program to print odd numbers in a List



a = [12, 14, 95, 3]

#Output: [2, 64, 14]

b = []

for i in range(len(a)):

    if a[i] % 2 != 0:

        b.append(a[i])

print(b)



25. Python program to print all even numbers in a range



# Input: start = 4, end = 15

# Output: 4, 6, 8, 10, 12, 14

b = []

for i in range(4,15):

    if i % 2 == 0:

        b.append(i)

print(b)



26. Python program to print positive numbers in a list



a = [12, -7, 5, 64, -14]

# Output: 12, 5, 64

b = []

for i in range(len(a)):

    if a[i] >= 0:

        b.append(a[i])

print(b)



27. Python program to print all positive numbers in a range



for i in range(-4,6):

    if i >= 0:

        print(i)



Method: Using the list comprehension 

x = [i for i in range(-4,6) if i >= 0]

print(x)



28.delete each element in the list which is divisible by 2 or all the even numbers. 



a = [11, 5, 17, 18, 23, 50]

# Output: [11, 5, 17, 23]

for i in range(0,len(a)-1):

    if a[i] % 2 == 0:

        a.remove(a[i])

print(a)



29. Remove multiple elements from a list in Python

a = [12, 15, 3, 10]

# Output: Remove = [12, 3], New_List = [15, 10]



for i in range(len(a)-1):

    if a[i] == 12:

        a.remove(a[i])

for i in range(len(a)-1):

    if a[i] == 3:

        a.remove(a[i])

print(a)



30. Python – Remove empty List from List



a = [5, 6, [], 3, [], [], 9]

x = [i for i in a if i != []]

print(x)





# TUPLES

--> tuples are immutable(non-changeble) whereas lists are mutable(changeble)

--> tuples consume less memory whereas lists consume more memory



1. Find the size of a Tuple in Python



import sys



t1 = ("A",1,"B",2,"C",3)

print("Size of Tuple1 : "+str(sys.getsizeof(t1))+" bytes")





2. Python program to create a list of tuples from given list having number and its cube in each tuple



a = [1, 2, 3]

# Output: [(1, 1), (2, 8), (3, 27)]



x = [(i,pow(i,3)) for i in a]

print(x)





3. Python – Adding Tuple to List and vice – versa



# list

a = [5, 6, 7]

# tuples

b = (9, 10)

# Adding Tuple to List and vice - versa

# Using += operator (list + tuple)

a +=  b

print(a)





Q) What is output of below program ?

class test:

    def __init__(self):

        print("Hello World")

    def __init__(self):

        print("Bye World")

obj=test()



--> Bye World



4. # Input - l = [[1,2,3],[4,5,6]]

# Output - l = [1,2,3,4,5,6]



b = l[0]+l[1]

print(b)





5. Write a Python program - first reverse the string, then convert lower char to upper and upper char to lower



a = "Write Python 3 code in this online editor and run it."

b = a[::-1]

print("Original string : ",a)

print("Reversed string : ",b)

data = ""

for char in b:

    if (char.islower()) == True:

        data += (char.upper())

    elif (char.isupper()) == True:

        data += (char.lower())

    elif (char.isspace()) == True:

        data += char

    else:

        data += char

print("converted string as : ",data)





6. Python | Count occurrences of an element in a list



a = [15, 6, 7, 10, 12, 20, 10, 28, 10]

x = 10

#Output: 3

count = 0

for i in range(len(a)):

    if a[i] == x:

        count +=1

print(count)



== Using list comprehension

a = [15, 6, 7, 10, 12, 20, 10, 28, 10]

x = 10

#Output: 3

count = 0

b = [i for i in range(len(a)) if a[i] == x]

print(len(b))





7. Python | Program to print duplicates from a list of integers

--> using count method

-- 



a = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

b = []

for i in a:

    n = a.count(i)

    if n > 1:

        if b.count(i) == 0:

            b.append(i)

print(b)





8. Python program to find Cumulative sum of a list



declare new empty list and count as 0, iterate a loop in list and for each iteration do a addition with the count

variable.. then for each iteration append that count variable in a new list



a = [10,20,30,40,50]

# Output : [10, 30, 60, 100, 150]

b =[]

count = 0

for i in range(len(a)):

    count += a[i]

    b.append(count)

print(b)





9. Kill the process 



pid = lsof -ni :1

a = [1,2,3,4,5]





for i in range(len(a)):

    if (a[i] % 2 != 0 ):

          pid = lsof -ni : a[i]

          sudo kill -9 pid





10. Write a python program to print the duplicate characters from a string and its count



str = "satellite"

a = []



for i in str:

    n = str.count(i)

    if n > 1:

        if a.count(i) == 0:

            a.append(i)

            print("character",i," is repeated ",n," times")

print(a)





character t  is repeated  2  times

character e  is repeated  2  times

character l  is repeated  2  times

['t', 'e', 'l']













1. What are key features of Python?

-- Python is free and open-source!

-- It is object-oriented language

-- Easy to learn due to clear syntax and readability

-- Easy to interpretm making debugging very easy

-- Easily integrated with other languages like C++, Java and more.



2. What are keywords in Python?

-- Keywords are reserved words which are used as identifiers, functions names and more

-- They help define the structure and syntax of the language.

-- There are 33 keywords in python 3.7

-- Keywords: False, None, True, and, break, continue, if, else, for, return, def etc.

-- You cannot variable has print





3. What are Literals in Python?

-- Literals in Python refer to the data is given in a variable or constant.

-- There are four types of literals:

  1. String literals - Sequence of characters enclosed in quotes

  2. Numeric lirerals - Integer, float and complex numbers

  3. Boolean literals - Represents TRUE or FALSE

  4. Special literasl - 'None' is a good example





4. How can you cancatenate two tuples?

-- consider two tuples:

   tup1=(1,"a",True)

   tup2=(4,5,6)



   print(tup1 + tup2)



--> (1,'a',True,4,5,6)





5. What are functions in Python?

-- Functions in Python refer to block that are organized, reusable pieces of code any number of time that perform single and related events.

-- Functions are important to create better modularity for applications which reuse high degree of coding.

-- Python has number of built-in functions like print() and allows of user-defined functions as well.

-- Smaller understandable chunks



  1. Built-in functions - print()

  2. User-defined fucntions - def





6. what are the memory-efficient way to add elements to a tuple?

-- THIS IS A TRICK QUESTION!

-- IMP - tuples are immutable datatypes in Python. --

-- means you cannot add elements to an existing tuple

-- A new one must be created if the values are to be changed!





7. What is dictionary in Python?

-- A python dictonary is fantastic data type in Python - its a collection of items whithout having any sort of order. (unordered collection of items)

-- Dictionaries are written in curly brackets with keys and values. one is gonna "key" and other one is "value" itself.

-- "Value" is gonna mapped with each different "keys"

-- "one key" - "one value", "another key" - "another value"

-- They are optimized to retrieve value for known keys.

-- Example: d={"a":1,"b":2}







8. What is the use of a classifer?

-- A classifier is used to predict the class of any data point.

-- A classifier classifies data





9. How do you convert a string into lowercase using Python?

-- All the upper cases in a string can be converted into lowercase by using the method:

string.lower()





10. How do you convert a string into uppercase using Python?

-- All the lower cases in a string can be converted into uppercase by using the method:

string.upper()





11. How do you get a list of all the keys in a dictionary?

--> dict.keys()







12. How can you capitalize the first letter if a string?

--> we can use the "capitalize()" fucntion to capitalize the first character of a string.

--  If the first character is already in capital then it returns the original string.





13. How can you insert an element at a given index in Python?

-- Python has an inbuilt function called the "insert()" function.



list = [0,1,2,3,4,5,6,7]

list.insert(6,10)  # Insert 10 at 6th index





output - [0,1,2,3,4,5,10,6,7]





SET - Collection of unique elements







14. How will you remove duplicate elements from a list?

-- There are various methods to remove duolicate elements from a list.

--> The easiest way is to convert the list into a set by using the set() function and using the using the list() function to convert it back to a list, if required. 



my_list = ['x','y','z','z','s']

my_lsit = list(dict.fromkeys(my_list))



output - ['x','y','z','s']





15. What is recursion?

--> Recursion is a function calling itself one or more times in it body.

--> IMP - You have to terminate the recursion by giving a condition or manually terminating it

-- if you do not terminate recursion then function calling itself keeps going back and forth, it will go in infinite times.. in infinite loop







16. What is Python List Comprehenstion?

--> List comprehensions are used for transforming one list into another list.

-- Elements can be conditionally included in the new list and each element can be transformed as needed.



list = [i for i in range(1000)]

print(list)



-- transforming for loop in a list





17. What is the use of bytes() function?

-- The bytes() funtion returns a simple bytes object.

-- It is used to convert objects into bytes objects, or create empty bytes object of the specified size.





18. What are different types of operators in Python?

-- Arithmetic : +, -, *, % (modulus operator - returns remindor)

-- Relational : <,>,<+,>=,==,!=

-- Assignment : =,+=,-=,/=,*=,%=

-- Logical : and, or, not

-- Others : Membership, Identity and Bitwise Operators





19. What is "with statement" used for in Python?

-- The 'with' statement in python is used in "exception handling"

--IMP - A file can be opened and closed while executing a block if code, containing the 'with' statement 

without using 'close()' function.





20. What is a 'map()' functions in Python?

--> The "map()" function in Python is used for applying a function on all elements of a specified iterable.

-- It consists of two parameters, function and iterable.





21. What is __init__ in Python?

--> The __init_ method is reserved method in Python. also known as a contructor

-- When an object is created from a class, then __init__ methodology is called to access the class attributes.







22. What is a Module?

--> Consider a module to be the same as a code library.

-- A file containing a set of functions you want to include in your application.

-- To create a module just save the code you want in a file with the file extension .py:



Save this code in a file named mymodule.py

	

def greeting(name):

  print("Hello, " + name)



Use a Module

Now we can use the module we just created, by using the import statement:



import mymodule



mymodule.greeting("Jonathan")



-- Hello, Jonathan





Variables in Module



person1 = {

  "name": "John",

  "age": 36,

  "country": "Norway"

}





import mymodule



a = mymodule.person1["age"]

print(a)



-- 36





*** Built-in Modules ***





import platform



x = platform.system()

print(x)



-- Linux





import datetime



x = datetime.datetime.now()

print(x)





*** Built-in Math Functions ***

x = min(5, 10, 25)

y = max(5, 10, 25)



print(x)

print(y)



x = abs(-7.25)



print(x)



x = pow(4, 3)



print(x)





import math



x = math.sqrt(64)



print(x)







#Import math library

import math



#Round a number upward to its nearest integer

x = math.ceil(1.4)



#Round a number downward to its nearest integer

y = math.floor(1.4)



print(x)

print(y)



#Import math library

import math



#Round a number upward to its nearest integer

x = math.ceil(1.4)



#Round a number downward to its nearest integer

y = math.floor(1.4)



print(x)

print(y)



#Import math library

import math

​

#Round a number upward to its nearest integer

x = math.ceil(1.4)

​

#Round a number downward to its nearest integer

y = math.floor(1.4)

​

print(x)

print(y)

​

2

1



import math



x = math.pi



print(x)







*** Python JSON ***

JSON is a syntax for storing and exchanging data.



JSON is text, written with JavaScript object notation.



****** Parse JSON - Convert from JSON to Python ==== .loads(x)



import json



# some JSON:

x = '{ "name":"John", "age":30, "city":"New York"}'



# parse x:

y = json.loads(x)



# the result is a Python dictionary:

print(y["age"])



30



****** Convert from Python to JSON ==== .dumps(x)



import json



# a Python object (dict):

x = {

  "name": "John",

  "age": 30,

  "city": "New York"

}



# convert into JSON:

y = json.dumps(x)



# the result is a JSON string:

print(y)





*** Python File Open ***

File Handling



f = open("demofile.txt", "rt")







f = open("demofile.txt", "r")



print(f.read())







f = open("demofile.txt", "r")

for x in f:

  print(x)





f = open("demofile3.txt", "w")

f.write("Woops! I have deleted the content!")

f.close()



#open and read the file after the appending:

f = open("demofile3.txt", "r")

print(f.read())





*** Check if File exist: ***



import os

if os.path.exists("demofile.txt"):

  os.remove("demofile.txt")

else:

  print("The file does not exist")





*** Delete Folder ***

import os

os.rmdir("myfolder")





SELECT * FROM Customers

WHERE City LIKE 'ber%';





What are the different types of variables in the Robot Framework?



There are 3 types of variables:

Scalar Variable. $

List Variable. &

Dictionary Variable. @





mytest

     =  set variable  Sky

    Run Keyword If  '' == 'Sky'  log to console  \nexecuted with single condition

    Run Keyword If  '' == 'Sky' or '' == 'Bird' or '' == 'Pink'  log to console  \nexecuted with multiple or







*** Change Tuple Values ***



Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.



But there is a "workaround". You can convert the tuple into a list, change the list, and convert the list back into a tuple.





x = ("apple", "banana", "cherry")

y = list(x)

y[1] = "kiwi"

x = tuple(y)



print(x)





*** Add Items ***

1. Convert into a list:

2. Add tuple to a tuple:



Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.





*** Remove Items ***

Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:





*** Unpacking a Tuple ***

fruits = ("apple", "banana", "cherry")



(green, yellow, red) = fruits



print(green)

print(yellow)

print(red)





*** Set Items *** Duplicates Not Allowed ***



*** Dictionary Items *** Duplicates Not Allowed



thisdict = {

  "brand": "Ford",

  "model": "Mustang",

  "year": 1964,

  "year": 2020

}

print(thisdict)



--> {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}





*** Else in For Loop ***

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:



for x in range(6):

  print(x)

else:

  print("Finally finished!")







*** Nested Loops ***



A nested loop is a loop inside a loop.



The "inner loop" will be executed one time for each iteration of the "outer loop":



adj = ["red", "big", "tasty"]

fruits = ["apple", "banana", "cherry"]



for x in adj:

  for y in fruits:

    print(x, y)





--> red apple

red banana

red cherry

big apple

big banana

big cherry

tasty apple

tasty banana

tasty cherry





*** Arbitrary Arguments, *args ***

def my_function(*kids):

  print("The youngest child is " + kids[2])



my_function("Emil", "Tobias", "Linus")



--> The youngest child is Linus



 

*** Keyword Arguments *** (kwargs)

def my_function(child3, child2, child1):

  print("The youngest child is " + child3)



my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



--> The youngest child is Linus





*** Arbitrary Keyword Arguments, **kwargs





*** Default Parameter Value *** 

If we call the function without argument, it uses the default value:



def my_function(country = "Norway"):

  print("I am from " + country)



my_function("Sweden")

my_function("India")

my_function()

my_function("Brazil")



I am from Sweden

I am from India

I am from Norway

I am from Brazil





*** Passing a List as an Argument ***

def my_function(food):

  for x in food:

    print(x)



fruits = ["apple", "banana", "cherry"]



my_function(fruits)





*** Return Values ***

def my_function(x):

  return 5 * x



print(my_function(3))

print(my_function(5))

print(my_function(9))





*** The pass Statement *** 

function definitions cannot be empty, but if you for some reason

 have a function definition with no content, put in the pass statement to avoid getting an error.



def myfunction():

  pass







*** Recursion ***

Python also accepts function recursion, which means a defined function can call itself.



Recursion is a common mathematical and programming concept. It means that a function calls itself.

 This has the benefit of meaning that you can loop through data to reach a result.





def tri_recursion(k):

  if(k > 0):

    result = k + tri_recursion(k - 1)

    print(result)

  else:

    result = 0

  return result



print("\n\nRecursion Example Results")

tri_recursion(6)





*** Python Lambda ***

A lambda function is a small anonymous function.



A lambda function can take any number of arguments, but can only have one expression.



lambda arguments : expression



x = lambda a : a + 10

print(x(5))



--> 15



x = lambda a, b : a * b

print(x(5, 6))



--> 30





*** Why Use Lambda Functions? ***

The power of lambda is better shown when you use them as an anonymous function inside another function.



Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:



def myfunc(n):

  return lambda a : a * n



mydoubler = myfunc(2)



print(mydoubler(11))



--> 22



(Use lambda functions when an anonymous function is required for a short period of time.)







*** Python Arrays ***

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

Arrays are used to store multiple values in one single variable:





*** Python Classes/Objects ***

A Class is like an object constructor, or a "blueprint" for creating objects.



class Person:

  def __init__(self, name, age):

    self.name = name

    self.age = age



p1 = Person("John", 36)



print(p1.name)

print(p1.age)







*** Python Inheritance ***

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.



Child class is the class that inherits from another class, also called derived class.



class Person:

  def __init__(self, fname, lname):

    self.firstname = fname

    self.lastname = lname



  def printname(self):

    print(self.firstname, self.lastname)



class Student(Person):

  pass



x = Student("Mike", "Olsen")

x.printname()





*** Use the super() Function ***



class Person:

  def __init__(self, fname, lname):

    self.firstname = fname

    self.lastname = lname



  def printname(self):

    print(self.firstname, self.lastname)



class Student(Person):

  def __init__(self, fname, lname):

    super().__init__(fname, lname)



x = Student("Mike", "Olsen")

x.printname()



--> Mike Olsen





*** Python Iterators ***

An iterator is an object that contains a countable number of values.



An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.



Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.



All these objects have a "iter()" method which is used to get an iterator:



mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)



print(next(myit))

print(next(myit))

print(next(myit))



--> apple

--> banana

--> cherry



































