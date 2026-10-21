Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"pooja","year":2026,"month":9}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 9}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['pooja', 2026, 9])
a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 9)])
a={"name":"pooja","city":"vja"}
a["name"]
'pooja'
a.get("pooja")
a
{'name': 'pooja', 'city': 'vja'}
#pop
a={"city":"vij","state":"ap","country":"india"}
a.pop("state")
'ap'
a
{'city': 'vij', 'country': 'india'}
a.popitem()
('country', 'india')
a
{'city': 'vij'}
#update
a={"course":"python","duration":100}
a
{'course': 'python', 'duration': 100}
a.update({"month":"sep"},{"date":30})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.update({"month":"sep"},{"date":30})
TypeError: update expected at most 1 argument, got 2
a.update({"month":"sep","date":30})
a
{'course': 'python', 'duration': 100, 'month': 'sep', 'date': 30}
a={"data":30"time":11}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a={"data":30,"time":11}
a.setdefault("hour",11)
11
>>> a
{'data': 30, 'time': 11, 'hour': 11}
>>> a.setdefault(11,"hour")
'hour'
>>> a
{'data': 30, 'time': 11, 'hour': 11, 11: 'hour'}
>>> #copy
>>> a={"colour":"white","food":"biryani"}
>>> a.copy()
{'colour': 'white', 'food': 'biryani'}
>>> len(a)
2
>>> a={"name":"pooja","city":"vij","name":"pooja"}
>>> print(a)
{'name': 'pooja', 'city': 'vij'}
>>> a={"name":"pooja","city":"vij","name"}
SyntaxError: ':' expected after dictionary key
>>> a={"idnos":10,20,30}
SyntaxError: ':' expected after dictionary key
>>> a={"idnos":[10,20,30],"names":["ambica","anush","pooja"]
...  print(a)
...    
SyntaxError: '{' was never closed
>>> type(a)
...    
<class 'dict'>
>>> a.key()
...    
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> a.keys()
...    
dict_keys(['name', 'city'])
>>> a.values()
...    
dict_values(['pooja', 'vij'])
