from decorators.timer import timer
from decorators.debugger import debugger
from decorators.slow_down import slow_down
from decorators.register import *
from decorators.repeat import *
from decorators.count_calls import *
from decorators.singleton import *
from decorators.cache import *
from decorators.use_unit import *

#  the decorator syntax @my_decorator is just an easier way of saying func = my_decorator(func)

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

@debugger
def waste_debugger(radius=1, pi=22/7):
    area =radius*radius*pi
    print(f"Circle has {radius} radius")
    print(f"It has {area} sq. area")
    return f"{area:.4f}"

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

waste_some_time(10)
countdown(1)
waste_debugger(10)

print(PLUGINS)
print(randomly_greet("Alice"))


@repeat
def say_whee():
    print("Whee!")

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

say_whee()
greet("Brijesh")

# @count_calls
# def counter():
#     print("Whee!")

@CountCalls
def counter():
    print("Whee!")
counter()
counter()


@singleton
class TheOne:
    pass

firstObj = TheOne()
secondObj = TheOne()

print(firstObj)
print(secondObj)

@cache
@CountCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))
print(fibonacci(8))

# @functools.lru_cache(maxsize=4)
# def fibonacci(num):
#     print(f"Calculating fibonacci({num})")
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
# print(fibonacci.cache_info())

@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration

bolt = average_speed(100, 9.58)
print(bolt)
print(bolt.to("km per hour"))
