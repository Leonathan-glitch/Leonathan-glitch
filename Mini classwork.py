Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name='David'
>>> message="%s 's %s"
>>> print(message % name)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(message % name)
TypeError: not enough arguments for format string
>>> message="%s is %s"
>>> print(message % name)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(message % name)
TypeError: not enough arguments for format string
>>> message='%s is %s'
>>> name='David, My'
>>> print(message % name)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(message % name)
TypeError: not enough arguments for format string
>>> name='David,good'
>>> message='%s is %s'
>>> print(message % name)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(message % name)
TypeError: not enough arguments for format string
>>> 
>>> name='David','good'
>>> message='%s is %s'
>>> print(message % name)
David is good
>>> \


  
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
>>> message="what did numhber %s say to %s"
>>> print(message % (0,8))
what did numhber 0 say to 8
>>> print(message % (0,8))
what did numhber 0 say to 8
>>> message="David %s is %s"
>>> message="David is %s"
>>> print(message % (tall))
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    print(message % (tall))
NameError: name 'tall' is not defined
>>> print(message % ("tall"))
David is tall
>>> message=%s is
SyntaxError: invalid syntax
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> message="%s is %s"
>>> print(message % ("David, tall"))
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    print(message % ("David, tall"))
TypeError: not enough arguments for format string
>>> print(message % ("David", "tall"))
David is tall
>>> #
>>> #="Hello"
>>> 
	