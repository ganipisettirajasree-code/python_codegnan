#error handing
1.syntax error--- compile error
2.Run time error--- During executions
3.logical error---


#error handing
#syntax error
'''for i in range(10)
print(i)'''

#run_time error
'''a=int (input("a value"))
b=int (input("b value"))
print(a//b)''' #10//0-> zero division error

#logical error
'''a=10
b=20
print(a-b)'''

'''a=3
b=5
if a>b:
    print("true")'''

'''a=3
b=5
if a<b:
    print("true")'''


# Exception Handling

#try --- Instructions from which we are expectng the exception .
#except--- exception are raised in try block it will be handle by this block
#else--- (option) no-exceptions.
#finally------always

'''while True:
    a= int(input("a value"))
    b= int(input("b value"))
    try:
        c= a//b
        print(c)
     except:
         print("exception is raised")
      else:
          print("no exceptions")
       finally:
           print("always")'''
#File handling
#write()
"""
a = open("satya.txt","w")
a.write("python full stack")
a.close( )

a = open("satya.txt" , "w")
a.write("codegnan")
a.close( )
"""
#append( )
"""
a = open("satya.txt","a")
a.write("\tdata")
a.close ( )
"""

#runtime -- 2 methods
"""
a = open("satya.txt","a")
a.write(input( ))
a.close( )
"""
"""
a = open("satya.txt","w")
b = input( )
a.write(b)
a.close( )
"""

#readlines()
"""
a = open("satya.txt")

print(a.read( )) #it will display entire content
print(a.readline( )) # it will display first line
print(a . read(10)) #it will display 10- number of characters
print(a.readlines( )) #it will display with \n
"""
#writelines() it makes every object side by side
"""
a = open("python.txt","w")
b = ["satya","sri","noshad","shanab","kranthi"]
a.writelines("\n".join(b))
a.close( )
"""

#giving file path and opening files
"""
a = open("functions.py")
print(a.read( ))
"""
"""
a = open(r"C:\Users\ssury\OneDrive\Desktop\Codegnan_Python\patterns.py")
print(a.read( ))
"""












           


    



