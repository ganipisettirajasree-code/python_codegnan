#functions---> is a block of organized, resuable code and that is used to perform a single or multiple task
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#functions
'''def calculate(a,b):
    a=10
    b=20
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''
 # ** % //
'''def calculate(a,b):
    a=10
    b=20
    print("the pow is",a**b)
    print("the mod is",a%b)
    print("the intdiv is",a//b)
calculate(10,20)
calculate(2,6)
calculate(4,2)'''

'''def add(a,b):
    c=a+b
    print(c)
add(4,5)'''

'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()  '''

'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+ " "+lname).title())
fullname()'''

#print v/s return---> print just shows the human users output in the console
# return --> return is uded to terminates the function and gives back value from the function
'''def sub(a,b):
    print(a-b)
sub(4,10)  '''

'''def sub(a,b):
    return a-b
print(sub(3,12))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4) '''

'''def cal(a,b):
       c=a+b
       d=a-b
       e=a*b
       #return c
       #return d
       #return e
       return c,d,e
print(cal(2,3))'''

#task
'''def cal():
    a=int(input("a value"))
    b=int(input("b valuae"))
    option=int(input( choose the option 
                                  1.add     
                                  2.sub                                
                                  3.mul))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
cal()'''

''''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))     
    option=int(input(choose the option 
                                  1.add     
                                  2.sub                                
                                  3.mul))
    if option==1:
         add()
    elif option==2:
          sum()
    elif option==3:
          mul()'''

#arguments
#-----------------key-word and positional aruguments------------------
'''def Details (id,name,mailid) :
    id=10
    name="pooja"
    mailid="pooja@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid) :
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="revathi",mailid="r@gmai.com")
Details(id=30,name="mastan Bee",mailid="m@gmail.com")
Details(30,"Venkat","v@gmail.com")
Details("Gowtham","g@gmail.com",40)
Details(name="Gowtham",mailid="g@gamil.com",id=50)'''

#task
'''def details(id,name,mailid,salary,designation):
    print(id,name,mailid,salary,designation)
details(id="id",name="name",mailid="mailid",salary="salary",designation="designation")
details(id=1,name="revathi",mailid="r@gmail.com",salary=12000,designation="Maths teacher")
details(id=2,name="mastanbee",mailid="m@gmail.com",salary=80000,designation="Principal")
details(3,"venkat","v@gmail.com",30000,"science teacher")
details("gowtham","g@gamil.com","telugu teacher",45000,4)
details(name="gowtham",mailid="g@gamil.com",designation="telugu teacher",salary=45000,id=4)'''

#----------------default arguments-----------------------
'''def grocery (item,price) :
    print("item is %s", %item)
    print("Price is %.2f",%price)
grocery("rice",2000)'''

'''def grocery(item="sugar",price=100):
    print("items is %s", %item)
    print("price is %.2f", %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("Price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="ghee",price) : #error --> non-default arg must not follow default argument
    print("item is %s", %item)
    print("price is %.2", %price)
print(500)'''


#task
'''def cake(cakename,price,qty) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d kgs" %qty)
cake("choclate",600,1)'''

'''def cake(cakename,price,qty=1.5) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d kgs" %qty)
cake("red valvet",600)'''

'''def cake(cakename,price=900,qty=0.5) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d kgs" %qty)
cake("almonds")'''

'''def cake(cakename="choco crunch",price=1000,qty=5) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cake()'''

#task
'''def splitbill(persons,amount) :
    print("The amount paid by each person is %.2f" %(amount/persons))
    print(f"the amount paid by each person is {(amount/persons)}")
    print("The amount paid by each person is {}".format(amount/persons))
p=int(input())
amount=int(input())
splitbill(p,amount)'''

#star arguments
#-------------------* argumenst--> * is used to unpack the elements-------------------------

'''a=[3,4,5,6,7,8,9]
print(a)
print(*a)'''

'''a=(4,5,6,7,8)
print(a)
print(*a)'''

'''a={6,7,8,9,10}
print(a)
print(*a)'''

'''a={"year":2026,"month":10}
print(a)
print(*a) # print only keys
print(a.values())'''

#* is also used to add the multiple elements to a single variable
'''a,b,c=3,4,5,6,7,8,9,20
print(a)
print(b)
print(c)''' # this program raises error

'''a,b,c=3,4,5
print(a)
print(b)
print(c)'''

'''a,b,*c=1,2,3,4,5,6,7,8,9,10
print(a) # prints 1
print(b) #prints 2
print(*c)''' # prints 3,4,5,6,7,8,9,10

'''a,*b,*c=1,2,3,4,5,6,7,8,9,10
print(a) 
print(*b) 
print(*c)''' # this program raises error beacouse there must not be used two * in one statements

'''a="codegnan"
print(a)
print(*a)''' # error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''*a,b,c="codegnan"
print(*a) # prints codegna
print(b) # prints a
print(c) '''#prints n

#---------------------varaible length arguments--> these automatically stores in tuple and we use star argument--------------

'''def check(*a) :
    print(a)
    print(type(a))
check()
b=[2,3,4,5,6,7,8]
check(*b)
c=(5,6,7,8,9)
check(*c)
d={5,6,7,8,9}
check(*d)
e={"city":"vij"}
check(*e)'''

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a :
        if type(i) is not str :
            d=d+i
        else :
            d=str(d)+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4.2,5.3)
check1(1,2,3,5,2.3,4.2,"pooja")'''

#task
#railway ticket
'''while True:
    def ticket(name,gender,age):
        if gender=="male" and age >= 60 :
            print("Male senior citizen")
            tickam=1000-(0.3*1000)
        elif gender=="female" and age >=60 :
            print("Female senior citizen")
            tickam=1000-(0.5*1000)
        elif gender=="female" and age<60 :
            print("female citizen")
            tickam=1000
        elif gender=="male" and age<60 :
            print("male citizen")
            tickam=1000
        print("The total amount to be paid:",tickam)
name=input()
gender=input()
age=int(input())
ticket(name,gender,age)'''

#-------------kwags(**) --> it stores everything in dictionary. only dict has to be used other datatypes are not allowed. but in * aruguments every datatype is allowed and stores in tuples.
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":['ajay','venkat','prasad'],
         "status":["p","a","p"]}
check(**details)'''

'''def check(**a):
    print(a)
    print(type(a))
    for i in a :
        print(i) # to return key without using the dictionary methods
    for i in a.keys() :
        print(i)#to return key with using the dict methods
    for i in a:
        print(a[i]) # to return thr values without using the dict methods
    for i in a.values() :
        print(i) # to return the values using dict methods
    for i in a :
        print(i,a[i]) # to return the items without using the dict methods
    for i in a.items() :
        print(i) # to return the items with using the dict methods, returns in tuple
check()
details={"idnos":[10,20,30],
         "names":['ajay','venkat','prasad'],
         "status":["p","a","p"]}
check(**details)'''

'''def check(*a,**b) :
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    d=2
    for i in a :
        if type(i) in (float,int) :
            d=d+i
            print(d)
    for i in b :
        print(i) # to return key without using the dictionary methods
    for i in b.keys() :
        print(i)#to return key with using the dict methods
    for i in b:
        print(b[i]) # to return thr values without using the dict methods
    for i in b.values() :
        print(i) # to return the values using dict methods
    for i in b :
        print(i,b[i]) # to return the items without using the dict methods
    for i in b.items() :
        print(i)
    for i,j in b.items():
        print(i,j)
check()
a=(1,2,3,4,5,6,7,8,"massu")
b={"names":["massu","mastanbee"],
   "id":[1,2]}
check(*a,**b)'''

#ASCII--> american standard code information interchange
#chr()---> to get the value for the given number
'''print(chr(90))
print(chr(65))
print(chr(91))'''

#ord()
'''print(ord("a"))
print(ord("z"))'''

'''print(ord(97))#error
print(chr("a"))'''#error

'''for i in range(65,91):
    print(chr(i),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")'''
'''n=input()
for i in n:
    print(i,ord(i))'''

#----------------scope of the variables-------------
#global & local--> a variable is inside and outside the function is called global and local variables
#global-->A variable is defined above the function and is accessable to the entire global space is called a global variable
# local--> a varibale is defined inside the function is called local variables

#First case of global variable
'''a=4
def check() :
    print("inside value is",a)
check()
print("Outside value is",a)'''

#second case of global variable
'''a=2
def check2() :
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of using both local and global variable
'''a=3
def check3() :
    a=4
    print("inside val is",a)
    a=5
    print("updated val is",a+5)
    b=15 # local variable
    b=b+a
    print("Inside b val is",b)
check3()
print("Outside a val is",a)
print("Outside b val is",b)''' # error b is not defined

#usage of global key word
#global def--> when user wants to create a varibale inside the function directly and carry forward the updated value we need to use global keyword
'''a=6
def final() :
    global a
    print("inside a val is",a)
    a=7
    print("updated val is",a)
    global b
    b=15
    b=b+a
    print("inside b val is",b)
final()
print("Outside a val is",a) # here it prints 7 becouse the updated value of a is carry forward becouse we used the global keyword
print("outside b val is",b)''' # here the b val prints becouse the val is determined with global variable

#---------------------------------------Genetators--------------------------------------------------
#genrator ---> no tuple comphresion in above cases if we remove thouse braces and keep parenthesis then the outcome is generator
#a=[exp for variable in range/collection] --> list comphesion syntax

# a=(exp for variable in range/collection)--> generator syntax

'''a=[i for i in range(16)]
print(a)
type(a)'''

'''a=(i for i in range(21))
print(a) # does not prints anything becouse we have to * or data types for printing
print(*a)
print(type(a))'''

'''print(list(a))
print(tuple(a))
print(set(a))
print(set(*a))'''# raises an error becouse we cannot use * and data type at a time, while printing the data using datatype we have to use only one data type

#generators--> a generator is also a function which can be used as an iterator(loop) by producing group of values where we can use yield keyword.

#yield vs return ---> return will terminate the function where as yield can pass the function and go on with every successive iteration.

'''a,b=[int(x) for x in input("enter:").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

#return
'''a,b=[int(x) for x in input("enter:").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(*check(a,b))'''# raises error becouse * must not be used for return if value in return is one only

'''a,b=[int(x) for x in input("enter:").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a # prints 3 only for 2,9
    #return a # prints 9 for 2,9
print(check(a,b))'''

#return v/s yield

'''def mygen() :
    #return "vij"
    #return "hyd"
    #return "vzg" # if i use 3 returns it only prints first return 
    return "vij","hyd","vzg" # for this we have to * to print in unpack
print(*mygen())'''

'''def mygen() :
    yield "apple"
    yield "manago"
    yield "grapes"
print(*mygen())

#next() --> used to print the next elements used in place of for loop
d=mygen()
print(next(d)) # prints apple
print(next(d)) # prints mango
print(next(d)) # prints grapes
print(next(d))'''# prints error becouse the there are no elements only 3 elements are there

#task --> BMI
w=float(input("Enter:"))
h=float(input("Enter:"))
bmi=w/(h)**2
if bmi <= 18.5 :
    print("Under weight")
elif bmi >18.5 and bmi <=24.5 :
    print("Normal weight")
elif bmi >24.5 and bmi <=29.5 :
    print("Over weight")
elif bmi >=30.0 :
    print("obesity")










