Assignment
# @property,  @balance.setter
## @property

It is a built in decorator in python. It enables a getter function to act like a normal attribute of a class. You are able to drop the `()` of the getter function name.

## @balance.setter

It works in conjunction with the @property decorator. It enables the setter function to take in a value without the function i.e `()`.One can alter the name `balance` to the name of the getter function. It allows one to assign a value to the function, in the same manner as a variable.

`@getter_function_name.setter`

### Example:
```python
class Athlete:
  company = 'test'
  def __init__(self,name,surname,id):
    self.name=name
    self.surname = surname
    self.id=id
    self.__balance = "bad"

  def showdetails(self):
    print(f"the name of employee:{self.id} is {self.name}")

  @property
  def email(self):
    return f"{self.name}.{self.surname}@{Athlete.company}.com"

  @property
  def balance(self):
    return self.__balance
    
  @balance.setter
  def balance(self,value):
    self.__balance = value

pt1 = Athlete("rohan","john",400)
print(pt1.email)
print(pt1.balance)
pt1.balance = "Great"
print(pt1.balance)
#            --> with @property | without @property
# pt1.email --> rohan.john@test.com | <bound method Athlete.email of <__main__.Athlete object at (memory location)>
# pt1.balance --> 'Yes' | <bound method Athlete.balance of <__main__.Athlete object at (memory location)>
```

In this example, the use of `@property` and `@balance.setter` is highlighted.This enables
one to get the athlete pt1's balance as `pt1.email` instead of calling it like a function `pt1.email()`. One is also able to set the new balance value using the assignment operator `=` instead of calling a setter function `pt1.balance("Great")`
 
# Creating you own decorator 

## Using function

To create a decorator in a function, one needs an outer function which takes a function as a parameter. It also requires an inner function which will wrap around the function passed. This will be executed. The outer function is a Higher Order Function (HOF). The inner function is able to access the function that is passed because it is a part of its lexical scope. Within the inner function, one is able to execute items to be done, before and/or after the passed function is called. One is able to use the outer function's name as the name of the decorator `@outer_function_name`. The `*args` allow any arguments of the function to be passed. The `**kwargs` allows any keyword aruments to passed to the function. The decorator imported from `functools` will prevent the declorator ffrom hiding the function they are placed on. This will make one is still able to read the documentation of the function (i.e. dunder variabe - __doc__).  

### Layout/ styntax:

```python
from functools import wraps

def outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """do things before function is eecuted"""
        func(*args, **kwargs)
        """do things after function is eecuted"""
    return inner

@outer
def func(values):
    pass

func()
```


## Using classes