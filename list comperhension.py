#list comprenension
every list comprehenstion can be rewritten in for loop and every for loop can not be rewritten as list comprehension.
#list  comprenension
a=["python","java","dsa"]
#["python","java","DSA"]

'''b=str(a)
print(b.upper())'''


'''for i in a:
    print(i.upper(),end=",")'''


#Syntax
#a=[expr for var in collection/range]


'''b=[i.upper() for i in a]
print(b)'''

a=["hyd","vja","vzg"]#["Hyd","Vja","Vzg"]

'''b=[i.capitalize()for i in a]
print(b)'''

a=[1,3,4,5,6,8,12,13]#[1,9,16,25,36,64,144,169]

'''b=[i*i () for i in a]
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
ptint(b)'''


'''a=[i for i in  range(21)]
print(a)'''


#if-usage in list compreshension
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i*i for i in range(16) if i%2==0]
print(a)'''

'''a=["apple","grapes","kiwi","mango","dragon","berry"]
b=[i for i in a  if "a" in i]
print(b)'''

'''b=[if "a" not in i]
print(b)'''

#no-elif usage in list comprehension

'''a=[i*i if i%2==0 else i*5 for i in range (31)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#output[6,6,6,6,6]
'''c=[a[i]+b[i] for i in range (5)]
c=[a[i]+b[i] for i in range (len (a))]
print(c)'''

#max(),min(),sum()
print(max(7,10,20,40,50,70))
print(min(7,10,20,40,50,70))

#print(sum(5,6))
'''a=3,4,5,6,7,8,9
print(sum(a))
print (sum(3,4,5,6,7,8,9))'''

#task
#Marks Analysis Report
student=int(input("no.of.students"))
num=int(input("Enter the student marks"))
print(max("no.of student")
print

              


   



