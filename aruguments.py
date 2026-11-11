Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#generators
#syntax
#a=[exp for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''


'''a=(i for i in range(21))
print(a)
print(*a)
print(type(a))'''

#print(list(a))
#print(type(a))
#print(tuple(a))
#print(set(*a))

# generators  a generators is also a function which can be use as iteralater(loop) by produceind group of values where we can use yield key word
#return /yield function
#retutn will termented the function  yield can pass the function and go on with every succesive function.
'''a,b=[int(x) for x in input ("enter the values")
.split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print (* check(a,b))'''

'''a,b=[int (x) for x in input ("enter the values")
     .split(",")]
def check (a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''


#yield v/s return
'''def mygen():
    #return "vij"
    #return "hyd"
    #return "vzg"
    return "vja","hyd","vzg"
print(* mygen ())'''


'''def mygen():
    yield "apple"
    yield "grapes"
    yield "mango"
print(*mygen())

#next()
d=mygen()
print (next(d))
print(next(d))
print(next(d))
print(next(d))'''

#task(bmi)
'''while True :
height=float(input("enter the value"))
weight= float(input("enter the value"))
BMI=weight/(hight)**2
print(BMI)
if  BMI <18.5:
    print("under weight")
elif BMI >18.5 and BMI <=24.5:
    print("normal weight")
elif BMI>24.5 and BMI <=29.5:
    print("over weight")
elif BMI>30:
    print("obesity")'''

# built in function

#from keys
'''a=codegnan
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))'''


'''b=dict.fromkeys(a)
print(b)'''

'''b=dict.fromkeys(a,"pooja")
print(b)'''

'''b["0"] ="priya"
print(b)'''


#Eval()
'''While True:
    a=int(input("a value"))
    b= int(input("b value"))
    print(a+b)'''


'''while True:
    a= float(input("a value"))
    b= float(input("b value"))
    print(a+b)'''

'''While True:
    a= input("a value"))
    b= input("b value"))
    print(a+b)'''


#zip () ->we can combine multiple collections into one collection.
'''a=[10,20,30,40,50]
names=["venkat","ajay","teja","harsha","prasad"]
print(a+names)


b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(anames))
print(d)

e= set(zip(a,names))
print(e)


f= dict(zip(a,names))
print(f)'''

#enumerate() -> we can give counter to the collection
names=["harshitha","vinuthna","kranthi","mastanbee","pooja"]
'''for i in range(len(names)):
    print(i,name[i])'''

'''b= list(enumerate(names,100))
print(b)'''

'''b=dict(enumerate(names,100))
print(b)'''

'''b=typle(enumerate(names,100))
print(b)'''

'''b= set(enumerate(names,100))
print(b)'''

#map ()-> each object from a collection and forms a new collection.


'''a=[2,5,7,9,10,12,15,20]
b=[1,3,6,8,17,25,40,60]
c=list(map(max,a,b))
print(c)

d=list(map(min,a,b))
print(d)

e= sum(a)
print(e)'''

# Annonymous functions or name less functions and we use a key word called as lambada to create annonymous function.
#write a function to calculate 2*x+5  where x=5
'''def cal(x):
    print(2*x+5)
cal(5)  '''


'''def cal():
    x= int(input("value"))
    print(2*x+5)
cal()'''

#syntax
#a= lambda arg:expr
'''a= lambda x:2*x+5
print(a(5))'''

'''a= int(intput("a value"))
b= lambda x:2*x+5
print(b(a))'''

a="python"
#PYTHON
'''b= lambda x:xupper
print(b(a))'''

a= hello word
#HELLO WORLD
'''b= lambda a:a.tittle()
print(b(a))'''

#fname+lname =fullname
'''a=int("fname")
b=int("lname")
c=lambda a,b:(a+" "+b).tittle()
print(c(a,b))'''

'''a,b=[x for x in input ("enter the names").split(",")
c= lambda a,b:(a+" "+b).tittle()
print(c(a,b)) '''

'''a=lambda x,y:x**y
print(a(2,4))'''

#filter()
a=[2,6,8,10,13,15,20,27,40,60,87,100]

'''if a%2==0:
      print(a)'''  #error

'''for i in a:
if i%2 ==0:
    print(I)''''

'''b= tuple (filter(lambda x:x%2==0,a))
print(b)'''

'''b= list(filter (lambda x:x%2==0 ,a))
print(b)'''

#[],(),{}

'''a=[]
print(type(a))''''

'''b=()
print(type(b))'''

'''c={}
print (type(c))'''

'''d={}
print (type(d))'''


      

      

















    



    




