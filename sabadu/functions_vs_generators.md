

```python
# Functions can `return` one or more values
# Functions use `return`
# Function `return` the final result

def add_up_function(lista):
    total = 0
    for item in lista:
        if type(item) == int:
            total = total + item
    return total
```


```python
my_list = [1, 3, 5,]
add_up_function(my_list)
```




    9




```python
# Generators are functions that you can loop though
# Generators use `yield`
# Generators 'yield' the result for each step

def add_up_generator(lista):
    total = 0
    for item in lista:
        if type(item) == int:
            total = total + item
            yield total
```


```python
my_list = [1, 3, 5,]
for loop in add_up_generator(my_list):
    print loop
```

    1
    4
    9



```python
my_list = [1, 3, 5,]
my_generator = add_up_generator(my_list)
```


```python
my_generator.next()
```




    1




```python
my_generator.next()
```




    4




```python
my_generator.next()
```




    9




```python
my_generator.next()
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-29-125f388bb61b> in <module>()
    ----> 1 my_generator.next()
    

    StopIteration: 
