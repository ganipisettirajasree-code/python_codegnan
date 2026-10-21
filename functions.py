#function
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


#function
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is ",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#**,%,//
'''def calculate(a,b):
    print("the pow is",a**b)
    print("the mod is",a%b)
    print("the intdiv is",a//b)
calculate(10,20)
calculate(2,8)
calculate(4,7)''',

#addition
'''def add(a,b):
    c=a+b
    print(c)
add(4,5)'''

'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()'''


'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).tittle())
full name()'''


 #print v/s return
'''def sub (a,b):
    print(a-b)
sub(4,10)'''

'''def sub (a,b):
    return a-b
print(sub(3,12))'''

'''def cal(a,b):
    c=a+b
    c=a-b
    c=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''


'''def cal (a,b):
    c=a+b
    c=a-b
    c=a*b
    #return c
    #return d
    #reture e
    returne c,d,e
print(cal(2,3))'''


#task
'''avalue=5
b value=10
option 1.add,2.sub.3.multiple
def calculate():
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(choose the option
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

#another way (multiple times)
'''def add():
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
        sub()
    elif option==3:
        mul()'''

#marks analysis report
'''student=int(input("enter the total no.of students"))
data=[]
for i in range (1,students+1):
    marks =int(input(f"enter the marks of student{i}"))
    data.append(marks)
print("marks analysis report.......")
print("total no.of students",students)
print("highest marks",max(data))
print("lowest marks",min (data))
print("total marks",sum(data))
print("average is",sum(data)/students)'''


#Arguments
#keysword and positional arguments
'''def Details (id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="revathi",mailid="r@gmail.com")
Details(id=24,name="pandu",mailid="p@gmai.com")
Details(30,"venkat","v@gmail.com")
Details("gowtham,"g@gamil.com",40)
Details(name="uday",mailid="u2gmail.com",id=50)'''        


#task(employees details)
'''def Details(id,name,mailid,salary,designation):
    print(id,name,mailid,designation)
Details(id="id",name="name",mailid="mailid", salary="salary",designation="designation")
Details(id=10,name="pandu",mailid="p@gmail.com", salary="100000",designation="H.R")
Details(id=20,name="sudha",mailid="s@gmail.com", salary="10000" ,designation="worker")
Details(id=30,name="surya",mailid="suryagmail.com", salary="20000",designation="Team Lead")'''


#default aruguments
'''def Grocery(items,prices):
    print("items is %s" %item)
    print("price is %.2f" %price)
Grocery()'''


'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''


'''def Geocery (item="ghee",price):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("price is %2." %price)
print(500)'''

'''def Grocery(item="salt",price,qty):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
Grocery(30,2)'''

#cakename,price,qty
'''def cake(cake="redcake",price="200", qut="2kg"):
    print("cake is %s",cake)
    print("price is %.2f",%price)
    print("qut is %s" %qty)
cake("redcake",200,2kg)'''

#arguments->  * is used to unpack the elements
'''a=[3,4,5,6,7,8,9]
print(a)
print(*a)'''

'''a=(4,5,6,7,8)
print(a)
print(*a)'''

'''a={3,6,7,8,9,4}
print(a)
print(*a)'''

'''a={"year":2026,"month":10}
print(a)
print(*a)'''

'''a,b,c=2,5,7,8,9,5,4,11
print=(a)
print=(b)
print=(c)'''

'''a,b,c=3,4,5
print(a)
print(b)
print(c)'''

'''a,b,*c =3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(*c)'''

'''a= codegnan
print(a)
print(*a)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

#variable length arguments :it is automatically stored in tuple and we can used star(*)arguments

'''def check (*a):
    print(a)
    print(type(a))
check()
b=[1,2,3,4,5]
check(*b)
c=(4,5,6,7)
check(*c)
d={5,6,4,7,8,10}
check(*d)
e={"city":"vja"}
check(*e)'''

'''def check1 (*a):
    d=2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type (i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4.2,5.3)
check1(1,2,3,5,2.3,4.2,"pooja")'''

'''#splitbill()
def splitibill():
    a=int(input("enter the total members"))
    b=int(input("enter the total amount"))
    print("perhead bill is",b//a))
splitibill()

def splitibill():
    a=int(intput("enter the total members"))
    b=int(intput("enter the total amount"))
    print(f"perhead bill is{b//a}")
    print("perhead bill is{}".format(b//a))
splitibill()    


def splitbill():
    a=int(intput("enter the  total members"))
    b=int(intput("enter the total amount))
    print(f" perhead bill is {b//a}")
    print("perhead bill is{}".format(b//a))'''


splitibill()                 


