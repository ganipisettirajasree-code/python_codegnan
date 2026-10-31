#--------------------------------------------------------------------------------------------29-10-26--------------------------------------------------------------------------------------------------------
#Difference between module,package and libraries.......................?
#Modules -
"""
  - It is a single python file, which consists python code.
  - It contains functions, variables, and classes.
  - Eg: math.py, random.py and mymodule.py
 """
#Package - 
"""
- One or more python modules known as packages
- Eg: numpy, pandas, matplotlib,reques
"""
#Libraries - 
"""
- A library can consists of both modules and packages
- Eg: numpy, pandas, django, matplotlib
"""

#-----NOTE ----
"""
Every python file is a module and import is a keyword and every python file is saved internally with variable name as __main__.
"""


"""
def greetings(name):
    print("Welcome",name)
"""
"""
a = 5
b = 6
print(a + b)
"""
"""
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
print(a + b)
"""
details = {"idnos" :[10,20,30], "names" :["pooja","anusha","ambica"], "marks" : [60,70,80]}
#import modules

#import modules # modules is a file name

'''import modules

b =  modules.details["idnos"]
c =  modules.details["names"]
print(b)
print(c)'''


'''if __name__ ==" __mani__":
    a=[10,20,30,40,50]
    #a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if__name__=="__mani__":
        print("this program is run as script")
     else:
         print("this program is run as module")
dummy() '''

#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.log(10))
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))
print(math.sqrt(2))
print(math.pow(2,4))
print(math.ceil(2.9))
print(math.floor(4.8))'''

'''from math import pi,sqrt,log
print(pi,sqrt(2),log(20))'''

#sys module
'''import sys
print(sys.path)

for i in sys.path:
    print(i)

print(sys.version)'''


#os module
import os
'''print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.mkdir("oct30"))
print(os.listdir())'''

'''print(os.chdir("c:\\users\\DELL\\Downloads"))
print(os.listdir())'''

#Random module:  to generate random numbers in python ,ranit (function is used ,this function is defined in random module)
#sample
'''import random
a=random.sample(range (20,50),5)
print(a)'''

#randint()
'''import random
a= random.randint(60,80)
print(a)'''

#choice()
'''import random
a=[3,4,5,6,7,8]
b= random.choice(a)
print(b)'''

#task(Dice code)
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(10,20)
    print(a)
    option = input("roll again ?(y/n)")
    if option=="Y":
        continue
    else:
        break'''

    

# calendar
'''import calendar
year=2027
month=11
print(calendar.month(year,month))'''

'''import calendar
year =2027
print(calendar.calendar(Year))'''

'''import calendar
a=int(input("enter the year"))
b=int(inpput("enter the month"))
print(calendar.month((a,b))'''


#date & time
'''from datetime import date
a=date.today()
print(a)'''


'''import datetime
a=datetime.datetime.now()
print(a)'''


'''import time
a= time.time()
print (a) # epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f" time is {b.tm_mhour}:{b.tm_mins}:{b.tm_secs}")
print(f" day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''









                  

                














