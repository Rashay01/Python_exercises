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

To create a decorator in a function, one needs an outer function which takes a function as a parameter. It also requires an inner function which will wrap around the function passed. This will be executed. The outer function is a Higher Order Function (HOF). The inner function is able to access the function that is passed because it is a part of its lexical scope. Within the inner function, one is able to execute items to be done, before and/or after the passed function is called. One is able to use the outer function's name as the name of the decorator `@outer_function_name`. The `*args` allow any arguments of the function to be passed. The `**kwargs` allows any keyword aruments to passed to the function. The decorator imported from `functools` will prevent the declorator from hiding the functions details that they are placed on. This will allow one to able to read the documentation of the function (i.e. dunder variabe - __doc__).  

### Layout/ styntax:

```python
from functools import wraps

def outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """do things before function is executed"""
        func(*args, **kwargs)
        """do things after function is executed"""
    return inner

@outer
def func(values):
    pass

func()
```

#### Example:
```python 
import time
from functools import wraps

def time_taken(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to execute function:{(end - start)/1000}s")
    return inner


@time_taken
def adding_multiply(num):
    time.sleep(2)
    print(f"The ans is: {10*num+1000 *2}")

adding_multiply(10)
```
In this example we are using the decorator created in the `time_taken` function which takes the start time before the function executes. The end time once the function has finish executing. It passes the argument `10` to the parameter `*args`. It will display the answer to the function `adding_multiply` and then the time taken to execute the function.


## Using classes

To create a decorator in a class, one will pass the function as a parameter to the constructor (`__init_`) of the class. This will create an instance variable to store the passed function. One will need a `__call__` function declared in the class, where one will execute the things to be done before/or after the function is executed, in the `return`. The `*args, **kwargs` will take in the arguemnts and keyword-arguments respectively. The name of the class will be the name of the decorator `@ClassName`.

### Syntax/layout
```python
class ClassName:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        """do things before function is executed"""
        ans = self.func(*args, **kwargs)
        """do things before function is executed"""
        return ans


@ClassName
def func(values):
    pass

func()
```

#### example
```python
class N_Decorator:
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print("Before execution")
    ans =self.func(*args, **kwargs)
    print("After after execution")
    return ans


@N_Decorator
def display_hello_message(name):
  return f"Hello {name}, hope you hae a great day."

print(display_hello_message("James"))
```

In this example, one is executing `display_hello_message` function. The decorator `@N_Decorator` will print a message before and after the execution of the function `display_hello_message`. It will then return and print the hello message for `James`. 