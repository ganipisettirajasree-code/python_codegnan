"""
import modules 
modules.greetings("Pooja")
"""

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
    






                  

                




