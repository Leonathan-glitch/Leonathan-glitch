Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1
>>> b=4
>>> c=95
>>> print
<built-in function print>
>>> print('my nane is david\n i att')
my nane is david
 i att
>>> print(a\n,b\n,c\n)
SyntaxError: unexpected character after line continuation character
>>> print(a\n,b\n,c\n)
SyntaxError: unexpected character after line continuation character
>>> 
>>> print(a'\n',b['\n','c\n')
      
SyntaxError: invalid syntax
>>> ')print(a'\n',b['\n','c\n')
SyntaxError: unexpected character after line continuation character
>>> print(a'\n',b'\n','c\n')
SyntaxError: invalid syntax
>>> print(a'\n',b'\n',c'\n')
SyntaxError: invalid syntax
>>> print(a'\n',b,'\n',c'\n')
SyntaxError: invalid syntax
>>> print(a,'\n',b,'\n',c'\n')
SyntaxError: invalid syntax
>>> print(a,'\n',b,'\n',c,'\n')
1 
 4 
 95 

>>> print('my name is leon\n I am 45 years old')
my name is leon
 I am 45 years old
>>> 