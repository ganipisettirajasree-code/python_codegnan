          Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
a.cunt("l")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.cunt("l")
AttributeError: 'str' object has no attribute 'cunt'. Did you mean: 'count'?
a.count("l")
4
b="hello"
b.find("l")
2
b[2:4]
'll'
#escape sequences
#/n-new line
#/t-tab space
a="name/nmobileno/tcollege/nmailid/tbranch'
SyntaxError: unterminated string literal (detected at line 1)
a="name/nmobileno/tcollege/nmailid/tbranch"
print(a)
name/nmobileno/tcollege/nmailid/tbranch
b="name:pooja\nmobileno:1234567897\tcollege:urce\nmailid:ganipisettirajasree@gmail.com\tbranch:case"
print(b)
name:pooja
mobileno:1234567897	college:urce
mailid:ganipisettirajasree@gmail.com	branch:case
#replace()
a="wait untill you succeed"
a.replace("wait","work")
'work untill you succeed'
b="python c"
b.replace("c","dsa")
'python dsa'
#upper()
a="code"
a.u#upper()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.u#upper()
AttributeError: 'str' object has no attribute 'u'
p
a.
SyntaxError: invalid syntax
























 #upper()
c[o]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    c[o]
NameError: name 'o' is not defined
c.[o].upper()
SyntaxError: invalid syntax
c.capitalize()
''
d="Python course"
d.title()
'Python Course'
e="i am in class "
e.title()
'I Am In Class '
a="java"
a.isupper()
False
a.islower()
True
b="PYTHON"
b.isdigit()
False
e=6789
e.isditgit()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    e.isditgit()
AttributeError: 'int' object has no attribute 'isditgit'
f="6789"
f.isdigit()
True
e.isdigit()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    e.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="pooja123"
e.isalunum()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    e.isalunum()
AttributeError: 'str' object has no attribute 'isalunum'. Did you mean: 'isalnum'?
f="pooja@123"
f.isalnum()
False
type(f)
<class 'str'>
#strip()
#lstrip(),rstrip()
a="    pooja    "
a.strip()
'pooja'
a.rstrip()
'    pooja'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="coure"
print(a+b)
pythoncoure
print(a+"     ")
python     
fname="pooja"
lname="ch"
print(frame+lname)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(frame+lname)
NameError: name 'frame' is not defined. Did you mean: 'fname'?
print(fname+lname)
poojach
print(fname+     lname)
poojach
#split()
a="c c++ python java"
a.split()
['c', 'c++', 'python', 'java']
b="i am learning python full stack"
b.split()
['i', 'am', 'learning', 'python', 'full', 'stack']
#join()
a="apple","banana","grapes"
"".join(a)
'applebananagrapes'
" ".join(a)
'apple banana grapes'
"l".join(a)
'applelbananalgrapes'
d="apple"
"l".join(d)
'alplpllle'
#formatting
a=3
b=6
print(a+b)
9
print("the sum is",a+b)
the sum is 9
city="vija"
print("city is",city)
city is vija
#format method()
a="motu"
b="pathlu"
print("hello{}{}".format(a,b))
hellomotupathlu
print("hello{} {}".format(a,b))
hellomotu pathlu
print("hello {} hello{}.format(a,b))
      
SyntaxError: unterminated string literal (detected at line 1)
print(("hello {} hello {}".format(a,b)).title())
      
Hello Motu Hello Pathlu
#fstring
      
a="pooja"
      
b="ch"
      
print(f"hello {a} {b}")
      
hello pooja ch
print(f"hello {a} hello {b}")
      
hello pooja hello ch
print((f"hello {a}{b}").tittle())
      
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print((f"hello {a}{b}").tittle())
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
>>> print((f"hello {a} {b}").title())
...       
Hello Pooja Ch
>>> #format method ()
...       
>>> a="8"
...       
>>> b="7"
...       
>>> print("multiplication{}".format(a*b))
...       
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    print("multiplication{}".format(a*b))
TypeError: can't multiply sequence by non-int of type 'str'
>>> print("multipliaction {]".format(a*b))
...       
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    print("multipliaction {]".format(a*b))
TypeError: can't multiply sequence by non-int of type 'str'
>>> print("the product is {}". format(c))
...       
the product is 
>>> a=5
...       
>>> b=6
...       
>>> print("the product is {}".format(c))
...       
the product is 
>>> c=a*b
...       
>>> print("the product is {}".format(c))
...       
the product is 30
