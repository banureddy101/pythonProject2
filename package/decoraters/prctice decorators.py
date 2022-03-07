##add 2 nos###

# def add_(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
# @add_
# def add(a,b):
#     print(a+b)
# add(1,2)
# @add_
# def sub(a,b):
#     print(a-b)
# # sub(3,1)
#
# ##len of arguments##
#
# def spam(func):
#     def wrapper(*args,**kwargs):
#         print('no of args:',len(args)+len(kwargs))
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
#
# @spam
# def add(a,b,c):
#     print(a+b+c)
# add(3,2,5)
#
# ##log decorator###
#
# def log(func):
#     def wrapper(*args,**kwargs):
#         print('python')
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
# @log
# def display():
#     return 'hai'
# print(display())
#
#
# ##delay befor excuting##
#
# import time
#
# def add(func):
#     def wrapper(*args,**kwargs):
#         time.sleep(2)
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
# @add
# def add(a,b):
#     print(a+b)
# add(1,2)
#
#
# ###string reverse###
#
#
# def reverse(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return result[::-1]
#     return wrapper
# @reverse
# def display(string):
#     return string
# print(display('ammu'))
#
# ###function for 3 times###
#
# def repeat(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
# @repeat
# def display():
#     return ('hello'*3)
# print(display())
#
# ###parameterized excutes n times###
#
# def _outer(n):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             for i in range(n):
#                 result=func(*args,**kwargs)
#             return result
#         return wrapper
#     return outer
# @_outer(3)
# def add(a,b):
#     print(a+b)
# add(1,2)
#
#
# import time
# def _delay(n):
#     def delay(func):
#         def wrapper(*args,**kwargs):
#             for i in range(n):
#                 time.sleep(2)
#                 result=func(*args,**kwargs)
#             return result
#         return wrapper
#     return delay
# @_delay(2)
# def add(a,b):
#     print(a+b)
# add(1,2)
#
#
# import time
# def delay(func):
#     start=time.time()
#     time.sleep(1)
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(f'{end-start}')
#         return result
#     return wrapper
# @delay
# def add(a,b):
#     print(a+b)
# add(1,2)