# 1Write a program to find the length of the string without using inbuilt function (len)#


# def _len(itrable):
#     count=0
#     for item in itrable:
#         count+=1
#     return count
#print(_len('hello'))

#2Write a program to reverse a string without using any inbuilt functions.#

# s='hello pyhton'
#for item in range(len(s)-1,-1,-1):
 #   print(s[item],end='')

# for item in reversed(s):
#     print(item,end="")

# for item in s[::-1]:
#     print(item,end='')

# def _reverse(_args):
#     res = []
#     for item in range(len(_args)-1,-1,-1):
#         res.append(_args[item])
#         return ''.join(res)
# print(_reverse('hello world'))
#
# def reverse(any_string):
#     temp = []
#     for i in range(len(any_string)-1, -1, -1):
#         temp.append(any_string[i])
#     return ''.join(temp)
# print(reverse('Hello world'))


#3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".#
#
# s="Hello world "
# a=s.replace('world','Universe')
# print(a)

#4. How to convert a string to a list and vice-versa.#

# def con_to_str(any_list):
#     return "".join(any_list)
# print(con_to_str(['1','2','3','4']))
#
# def con_to_list(any_str):
#     return any_str.split()
# print(con_to_list('hello'))

#5. Covert the string "Hello welcome to Python" to a comma separated string.#

# str_="hello welcome to python"
# res=str_.split()
# print(res)

# #6Write a program to print alternate characters in a string.#
#
# s='hello python'
# print(s[::2])

#7Write a Program to print ascii values of the characters present in a string.
#
# s='hello pyhton'
# for i in s:
#     print(ord(i),end=" ")

#8write program to convert upper case to lower case and vice-versa without using inbuilt method.#

# char='HELLO WORLD'
#
# for item in char:
#     if 'a'<=item<='z':
#         print(f'{char} is lower char',end='')
#     elif 'A'<=item<='Z':
#         print(f'{char} is upper char',end='')


#9. Write program to swap two numbers without using 3rd variable.#
# a=10
# b=20
# b,a=a,b
# print(a)
# print(b)

#10. Write program to merge two different lists.#

# a=[1,2,3]
# b=[4,5,6]
# c=[*a,*b]
# print(c)
# print(a+b)

#11 Write a program to check if the given string is Palindrome or not without using reversed method#
# def _palindrome(iterable):
#     rev_itr=iterable[::-1]
#     if iterable==rev_itr:
#         return True
#     else:
#         return False
# print(_palindrome("hiai"))

#12 Write a program to search for a character in a given string and return the corresponding index.#
#
# def search_char(string,key):
#     for index,item in enumerate(string):
#         if item == key:
#             return f'char is {item} at index is{index}'
# print(search_char('hello world','d'))

#13 Write a program to get the below output#
#
# sentence = "hello world welcome to python programming hi there"
# # d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# from collections import defaultdict
# d=defaultdict(list)
# s=sentence.split()
# for i in s:
#     d[i[0]].append(i)
# print(d)
#14 write a decorator that returns only positive values of subtraction#
# def Decorator_(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return abs(result)
#     return wrapper
# @Decorator_
# def add_(a,b):
#      return (a-b)
# print(add_(4,8))


#15 How to get the count of number of instances of a class that is being created.#

# class Login:
#     login_count = 0
#     def __init__(self):
#         Login.login_count+=1
#
# a1=Login()
# print(Login.login_count)
# a2= Login()
# print(Login.login_count)

#16Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer of float it should reverse it.

# s=['banu','hello',1,2,3,12.4,12,6,'123']
# for i in s:
#     if isinstance(i,str):
#         print(i)
#     else:
#         print(str(i)[::-1])

#17 Write a python program to get the below output#

# sentence = "Hi How are you"
# #o/p should be "iH woH era uoy"#
#
# s=sentence.split()
# a=[i[::-1]for i in s]
# print(a)

# 18Write a python program to get the below output#
# sentence = "Hi How are you"
# # o/p should be "ouy era woH iH"
# for item in range(len(sentence)-1,-1,-1):
#     print(sentence[item],end='')



#19 Write a lambda function to add two numbers (a, b)#


# res=lambda a,b:a+b
# print(res(1,2))



#20 What is the output of the following#

# a = [1, 2, 3]
# b = [4, 5, 6]
#
# print([a,b]) ###Tuple of list
# print((a,b)) ###List of List



#21How to remove duplicates from the list without using inbuilt functions
#
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# unique=[]
# for i in items:
#     if i not in unique:
#         unique.append(i)
# print(unique)


#22Find the longest word in the sentence#

# sentence = "Hello world welcome to Python"
# s=sentence.split()
# max (s,key=len)
# print(max)

#
# smallest,*rest,longest=sorted(s,key=len)
# op=(smallest)
# print(len(op))



#23 write a program to reverse the values in the dictionary if the value is of type String

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# for key,value in d.items():
#     if isinstance(value,str):
#         d[key]=value[::-1]
#         print(d)


#24How to get the elements that are in list b but not in list a

# a = [1, 2, 3] b = [1, 2, 3, 4]
# a=[1,2,3]
# b=[1,2,3,4]

# {1,2,3,4}-{1,2,3,4}
# a=set(a)
# b=set(b)
# print(b-a)


#25 A function takes variable number of positional arguments as input.
#howto check if the arguments that are passed are more than 5
# def spam(*args):
#     if len(*args)>5:
#         print(f'length of the arguments are passed greater than 5')
#     else:
#         print(f'length of the arguments are passed less than 5')
#
# print(spam('1,2,3,4,5,6'))

#26Write a function to reverse any iterable without using reverse function

# def reverse_(args):
#     for i in args[::-1]:
#         print(i,end='')
# reverse_('hello')

#27 Write a function to print the below output.

# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX#
#
# def spam(string,flag):
#     if flag:
#         return string[::2]
#     return string[1::2]
# print(spam("TRACXN", 0))
# print(spam("TRACXN", 1))

#28Sum all the numbers in the below string.

# import re
# total=0.00
# s = "Sony12India567Pvt2ltd"
# op=re.findall(r'[\d]',s)
# print(op)
# for i in op:
#     total+=int(i)
# print(total)


#29Write a program to sum all the numbers in below string.
# import re
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
# total=0.00
# op=re.findall(r'[\d]+', s)
# print(op)
# for i in op:
#     total+=int(i)
# print(total)

#30 Program to print the number of occurrences of characters in a String without using inbuilt functions.#
# s="hello world,pyhtpn"
# from collections import defaultdict
# d=defaultdict(int)
# for i in s:
#     d[i]+=1
# print(d)

#31Program to print only the repeated characters and count of the same.
# s = 'helloworld'
# from collections import defaultdict
# d=defaultdict(int)
# for i in s:
#     d[i]+=1
# print(d)


#32Write a program to get alternate characters of a string in list format.
# s = 'hello world welcome to python'

# for i in s[::2]:
#     print(list(i),end='')

# op=[i for i in s[::2]]############this is s correct in list format
# print(op)

# res=[]
# for i in range(0,len(s),2):
#     print(s[i],end='')


#33Write a program to get square of list of number's using lambda function .
# a = [1, 2, 3, 4, 5]
#
# res = lambda n : n**2
# sq=[res(i) for i in a]
# print(sq)

#34 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.
# def anagrams_(str1,str2):
#     if str1.upper() == str2.upper():
#         return False
#     a_str1 = sorted(str1.upper())
#     b_str2 = sorted(str2.upper())
#     if a_str1 == b_str2:
#         return True
#     else:
#         return False
# print(anagrams_('ate','eta'))
# print(anagrams_('file','elif'))
# print(anagrams_('helll','hhhe'))



#35 write a program to iterate through list and build a new list, only if the items of the list has even number of characters.
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# l = [i for i in names if len(i)%2 == 0]
# print(l)


# l = []
# for i in names:
#     if len(i) %2 ==0:
#         l.append(i)
# print(l,end='')

#36Write a program to iterate through list and build a new dictionary, only if the items of the list has even number of characters.
names=['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

# d = {}
# for i in names:
#     if len(i)%2 == 0:
#         d[i]=len(i)
#         # d.update(i)
# print(d,end='')


# d={i:len(i) for i in names if len(i)%2 == 0}
# print(d)

#37Squares of numbers using map
# map is used to map a function with a iterable
a = [1, 2, 3, 4, 5]
# def sqr(args):
#     return args ** 2
# res=map(sqr,a)
# for i in res:
#     print(i,end=' , ')

# m =map(lambda n : n**2, a)
# for i in m:
#     print(i)


#38#Write a Program to print the sum of entire list and sum of only internal list

# l = [[1,2,3],[4,5,6],[7,8,9]]
# sum_internal = [sum(i) for i in l]
# sum_ == sum(sum_internal)
# i=[[1,2,3],[4,5,6],[7,8,9]]
# print(i)

#39Write a program to reverse the list as below

# words = ["hi", "hello", "python"]
# #o/p ['nohtyp', 'olleh', 'ih']#
# for i in range(len(words)-1,-1,-1):
#     print(words[i][::-1],end=',')


# for i in words[::-1]:
#     print(list(i[::-1]))

'40Write a program to update the tuple'

# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
#
# t= t1 +t2
# print(t)