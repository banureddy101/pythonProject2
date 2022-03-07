# def log(func):
#     def wrapper(*args,**kwargs):
#         print("in decorator function")
#         func(*args, **kwargs)
#     return wrapper
# @log
# def display():
#     print("in display")
# display()

# import time
# def delay(func):
#     def wrapper(*args,**kwargs):
#         time.sleep(2)
#         return func(*args,**kwargs)
#     return wrapper
# @delay
# def display():
#     return "in display"
# print(display())

# def string(func):
#     def wrapper(*args,**kwargs):
#         print("python")
#         func(*args, **kwargs)
#     return wrapper
# @string
# def display():
#     print("python"*3)
# display()

# import time
# def outer_(n):
#     def delay(func):
#         def wrapper(*args,**kwargs):
#             time.sleep(n)
#             func(*args,**kwargs)
#         return wrapper
#     return delay
# @outer_(3)
# def add(a,b):
#     print(a+b)
# add(1,2)
#
# @outer_(2)
# def sub(a,b):
#     print(a-b)
# sub(10,4)
#
# import time
# def outer_(n):
#     def delay(func):
#         def wrapper(*args,**kwargs):
#             start = time.time()
#             time.sleep(n)
#             func(*args,**kwargs)
#             end = time.time()
#             print(f"time of execution {end-start}")
#         return wrapper
#     return delay
# @outer_(3)
# def add(a,b):
#     print(a+b)
# add(1,2)
#
# @outer_(2)
# def sub(a,b):
#     print(a-b)
# sub(10,4)
#
#
# import time
# def outer_(n):
#     def delay(func):
#         def wrapper(*args,**kwargs):
#             start = time.time()
#             time.sleep(n)
#             func(*args,**kwargs)
#             end = time.time()
#             print(f"time of execution {end-start}")
#         return wrapper
#     return delay
# @outer_(3)
# def add(a,b):
#     print(a+b)
# add(1,2)
#
# @outer_(2)
# def sub(a,b):
#     print(a-b)
# sub(10,4)

# def count(func):
#     def wrapper(*args, **kwargs):
#         print("the no of args are", len(args)+len(kwargs))
#         return func(*args, **kwargs)
#     return wrapper
#
# @count
# def add(*args, **kwargs):
#     #print(a+b+c+d)
#     return "executed"
# print(add(1, 2, 3, 4, a=6))
#
#
# a='banu'
# b='prathap'
# a+=b
# print(b)

#
# def reverse(func):
#     def wrapper(*args,**kwargs):
#         result= func(*args,*kwargs)
#         if isinstance(result,str):
#             return result[::-1]
#         return result
#     return wrapper
# @reverse
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# @reverse
# def greet():
#     return 'hello'
# print(greet())
#
#
#
# def positive(func):
#     def wrapper(*args,**kwargs):
#         result= func(*args,*kwargs)
#         if isinstance(result,(float,int)):
#             return abs(result)
#         return result
#     return wrapper
# @positive
# def add(a,b):
#     return a-b
# print(add(8,20))
#
# @positive
# def greet():
#     return 'hello'
# print(greet())


# def spam(func):
#     def wrapper(*args,**kwargs):
#         print('the no of arguments',len(args)+len(kwargs))
#         return func(*args,**kwargs)
#     return wrapper
#
#
# @spam
# def add(a,b):
#     return (a+b)
# print(add(1,3))
#
# @spam
# def sub(a,b):
#     return (a-b)
# print(sub(1,3))
#
#
# def log_(func):
#     def wrapper(*args,**kwargs):
#         print('hello world')
#         return func(*args,**kwargs)
#     return wrapper
#
# @log_
# def display():
#     return ('display')
# print(display())


# def spam_(func):
#     def wrapper(*args,**kwargs):
#         print('HELLOWORLD')
#         return func(*args,**kwargs)
#     return wrapper
#
# @spam_
# def function_():
#     return ('HELLOWORLD'*3)
# print(function_())

# def _outer(n):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             for i in range(n):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return outer
#
# @_outer(3)
# def add(a,b):
#     print(a+b)
# add(1,2)



def cache(func):
    _cache={ }
    def wrapper(*args,**kwargs):
        if args not in _cache:
            result=func(*args,**kwargs)
            _cache[args] = result
            return result
        print('returning cached result')
        return _cache[args]
    return wrapper

@cache
def add(a,b):
    sleep(2)
    return a+b
print(add(5,5))


# def count_(func):
#     func.count=0
#     def wrapper(*args,**kwargs):
#         func.count=+1
#         print(f'function {func.__name__} was called { func.count}')
#         return func(*args,**kwargs)
#     return wrapper
#
# @count_
# def add(a,b):
#     return a+b
# print(add(4,6))

#
# def log(func):
#     def wrapper(*args,**kwargs):
#         print("in decorator function")
#         func(*args, **kwargs)
#     return wrapper
class Bankaccount:
    interest_rate = 0.04
    def __init__(self,name,balance):


class Salary(Bankaccount):
    def __init__(self,name):
        self.is_first.month_salary = True
        self.max.draft_amount = 1000
        self.draft_ampunt_taken = 0.00
        super().__init__(name,0.00)