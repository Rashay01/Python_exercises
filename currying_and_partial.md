# What is currying and partial?

### What is a currying?

Curying is a functional programing tequnique. Currying is the practice of simplifying the execution of a function that takes multiple arguments into executing sequential single-argument functions

In other words, it is the process of taking a function that has multiple aguments, and converts that to be executed one after the other as single agument functions.

An example  is  taking `f(a, b, c)` and making it `F(a)(b)(c)`

The example of curring below converts Rands to Pounds. We have the exchange rate from Rand to Dollar and exchange rate of Dollar to Pound. This nested function requires the result of another function which is the conversion of rand to dolar.

```Python
def currying( g , f ):
  def h(x):
      return g(f(x))
  return h


def rand_to_dollar(ammount):  
  return ammount*0.052  

def dollar_to_pound(ammount):   
  return ammount * 0.76


convert_Rand_Pound = currying(rand_to_dollar,dollar_to_pound )
print(convert_Rand_Pound(100))
```

### What is a partial function?

It enables one to create a new function by making certain aruments fixed. It is like a factory for creating new functions.


In the example below: `g` create a new partial function of `h` with the values of `a=3` and `b=1` fixed. So when the function `g` is called, it only takes on an argument for `c`.

```python 
from functools import partial

def h(a, b, c):
    return 100*a + 10*b + c

g = partial(h, 3, 1)

print(g(5))
```