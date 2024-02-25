# Difference between Paramenters vs Arguments

### Paramenters:
Parameters are the names used in function definition. It is like a placeholder for the argments that will be passed to the functions.

E.g. Below the names `value1` and `value2` are the parameters.

```python
def multi (value1, value2):
    return value1 * value2
```

### Arguments

An arugument is the actual value that is passed to the function when it is called. They are placed within the parenthesis `()` when the function is callled. It can be a value, variable,class, or function that is passed.

E.g. The values `1` and `2` are arguments that are passsed to the funcion `multi`. The variables `a` and `b` are argumenst passed to the function.

```python
ans = multi(1,2)
ans1 = multi(a,b)
```



# What is currying and partial?

### What is a currying function?

Curying is a functional programing.

### What is a partial function?

It enables one to create a new function by making certain aruments fixed. It is a factory for creating new functions.


E.g: In the example below: `g` create a new partial function of `h` with the values of `a=3` and `b=1` fixed. So when the function `g` is called, it only takes in a argument for `c`.

```python 
from functools import partial

def h(a, b, c):
    return 100*a + 10*b + c

g = partial(h, 3, 1)

print(g(5))
```

