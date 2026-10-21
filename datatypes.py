Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
b=7.7
type(b)
<class 'float'>
c="Python"
type(c)
<class 'str'>
d='codegnan'
type(d)
<class 'str'>
f=2
f=2+5j
type(f)
<class 'complex'>
g=4j
type(g)
<class 'complex'>
h=True
type(h)
<class 'bool'>
j=False
type(j)
<class 'bool'>
k=false
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    k=false
NameError: name 'false' is not defined. Did you mean: 'False'?
l=j
type(j)
<class 'bool'>
l=j
type(l)
<class 'bool'>
del jl=j
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    l=j
NameError: name 'j' is not defined

# Datatype conversions
# int
int(7)
7
int(2.9)
2
int("python")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(5+9j)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(5+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

 
# float
float(1)
1.0
float(9.6)
9.6
float("Python")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float("Python")
ValueError: could not convert string to float:float(4+7j)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(4+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

# String
str(1)
'1'
str(2.9)
... '2.9'
... str("pyton")
... 'pyton'
... str(4+8j)
... '(4+8j)'
... str(True)
... 'True'
... str(False)
... 'False'
... 
... # complex
... complex(1)
... (1+0j)
... complex(3.9)
... (3.9+0j)
... complex("Name")
... Traceback (most recent call last):
...   File "<pyshell#55>", line 1, in <module>
...     complex("Name")    complex("Name")
... ValueError: complex() arg is a malformed string
... complex(8+9j)
... (8+9j)
... complex(True)
... (1+0j)
... complex(False)
... 0j
... 
... # Boolean
... bool(8)
... True
... bool(9.8)
... True
... bool("Python")
... True
... bool(9+8j)
... True
... bool(True)
... True
... bool(False)
