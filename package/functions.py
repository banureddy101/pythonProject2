# def add(val1,val2):
#     a=val1
#     b=val2
#     c=a+b
#     return c
#
#
# # # # print(add(1,2))
# # # print(add(val1=1,val2=2))
# # print((add(1,val2=2)))
#
#
# def fybo_(end,start=0):
#     a=0
#     b=1
#     i=0
#     while i < 10:
#         print(a)
#         c=a+b
#         a=b
#         b=c
#         i+=1
#     return a
#
#
# print(fybo_(5))


#
# def sum_(*args):
#     print(args)
#     print(sum(args))
#
#
# sum_(1,2,3)

# def function(*args):
#     # count=0
#     # for _ in args:
#     #     count+=1
#     #
#     # return count
#     return len(args)
#
#
# print(function(1,2,3,4))



# def int_(*args):
#     for item in args:
#         if isinstance(item,int):
#             print(item)
#
#
#
# int_(1,2,3,2.3,3.4)



# def str_(*args):
#     for item in args:
#         if isinstance(item,str):
#             print(item[::-1])
#
# str_(1,2,3,'hai','hello')



#
# def spam(*args):
#         if len(args)>5:
#             return "no of args>5"
#         else:
#             return "no of args <5"
#
#
# print(spam(1,2,3,4,))

# def display(a='hai every one'):
#     print(a)
#
# # display('hello')
# display()


# def prime_(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return 'is not prime'
#         return 'is prime'
#
# print(prime_(5))
#
# def last_(n):
#     return str(n)[-1]
# print(last_(12354))


# def is_perfect_square(num):
#     sq=int(num**0.5)
#     if sq*sq == num:
#         return True
#     return False
#
# # print(is_perfect_square(27))
#
# def fybo_(end,start=0):
#     a=0
#     b=1
#     i=0
#     while i < 10:
#         print(a)
#         c=a+b
#         a=b
#         b=c
#         i+=1
#     return a
#
#
# print(fybo_(5))


# def fyboo(n):
#     a = 0
#     b = 1
#     while a <= n:
#         if a == n:
#             return 'is fybbo no'
#             c = a+b
#             a = b
#             b = c
#     return 'is fybbo no'
#
# fyboo(5)
#
def var_(*args):
    for i in args:
        if isinstance(i,(str,tuple,list,dict,set)):
            print(list(i),len(i))

var_('banu',(1,2,3))
