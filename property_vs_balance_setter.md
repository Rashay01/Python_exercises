Assignment
1. @property,  @balance.setter
# @property

It is a built in decorator in python. It enables a getter function to act like a normal attribute of a class. You are able to drop the `()` of the getter function name.

# @balance.setter

It works in conjunction with the @property decorator. It enables the setter function to take in a value without the function i.e `()`.One can alter the name `balance` to the name of the getter function. It allows one to assign a value to the function, in the same mannor as a variable.

`@getter_function_name.setter`

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

In this example, one is able to get the athlete pt1's balance as `pt1.email` instad of calling it like a function `pt1.email()`. One is also able to set the new balance value using the assignment operator `=` instaed of calling a setter function `pt1.balance("Great")`
 
2. Creating you own decorator 
Using function
Using classes