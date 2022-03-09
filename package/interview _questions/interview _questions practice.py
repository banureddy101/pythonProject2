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
# names=['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

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
# a = [1, 2, 3, 4, 5]
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

'''40Write a program to update the tuple'''

# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
#
# t= t1 +t2
# print(t)

'''41Print all the numbers in the below list'''

# a = ['abc', '123', 'hello', '23']
# for i in a:
#     if i.isnumeric():
#         print(i)

'''42 write a Program to print the number of occurrences of characters in a String without using inbuilt functions.'''

s = 'helloworld'
# d={}
# for i in s:
#     d[i]=s.count(i)
# print(d)
#
# from collections import defaultdict
# d=defaultdict(int)
# for i in s:
#     d[i]+=1
# print(d)
#
# from collections import Counter
# c=Counter(s)
# print(c)

'''43Program to print only the repeated characters and count of the same.'''

# s = 'helloworld'
# d={}
# for i in s:
#     if s.count(i) == 1:
#         d[i]=s.count(i)
# print(d)

'''44Write a program to get alternate characters of a string in list format.'''
# s = 'hello world welcome to python'
# for i in s[::2]:
#     print(list(i),end='')

# l =[i for i in s[::2]]
# print(l)


'''45Write a program to get square of list of number's using lambda function '''
# a = [1, 2, 3, 4, 5]
# res=lambda n : n**2
# sqr = [res(i) for i in a]
# print(sqr)

'''46Grouping anagrams'''
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# from collections import defaultdict
# d= defaultdict(list)
# for i in words:
#     s=''.join(sorted(i))
#     d[s].append(i)
# print(d)

'''46 Write a list comprehension to get a list of even numbers from 1-50'''

# l=[i for i in range(1,51) if i % 2 == 0]
# print(l)


'''s = "This is a Programming language and Programming is fun"
# make dictionary with word and its length pair for only those words which are not repeated.'''

# s = "This is a Programming language and Programming is fun"
# l =s.split()
# d={}
# for i in l:
#     if s.count(i) == 1:
#         d[i]=len(i)
# print(d)

'''Write a program to find the duplicate elements in the list without using inbuilt functions'''

# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# uniq =set(names)
# count = 0
# for i in uniq:
#     if i == uniq:
#count+ = 1

'''_49 Write a program to count the number occurrences of each item in the list without using any inbuilt functions'''

# names =['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# d={}
# for i in names:
#     d[i]=names.count(i)
# print(list(d))

'''50Write a function to check if the number is Prime'''

# def prime_(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return 'not prime'
#         return 'prime'
# print(prime_(4))

'''51How to create a tuple using range function'''
# a=tuple(range(10))
# print(a)

'''52Write a program to find the largest number in the list without using any inbuilt functions'''
# numbers = [10, 20, 30, 40, 50]
# largest=0
# for i in numbers:
#     if i > largest:
#         largest == i
# print(i)

'''53Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.
'''
# def last_(n):
#     return str(n)[-1]
# print(last_(12345))

# def last_(n):
#     return n%10
# print(last_(1234))

'''54Write a program to find most common words in a given list.'''
# words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes','the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under']

from collections import Counter
# a=[]
# c=Counter(words)
# a.append(c)
# print(a)

# from collections import defaultdict
# d=defaultdict(int)
# for i in words:
#     d[i]+=1
# print(d)


'''55Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.'''
# def tail_(sequence,n):
#     return sequence,[-n]
# print(tail_('hello',2))

'''56Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.'''

# def sqr(n):
#     for i in range(n):
#         if i ** 2 == n:
#             return True
#         return False
# print(sqr(4))

'''57Write a program to get all the duplicate items and the number of times the item is repeated in the list.'''
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d={}
# for i in names:
#     if names.count(i)>1:
#         d[i]=names.count(i)
# print(d)

'''58Write a program to print all numeric values in a list'''

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
#
# for i in items:
#     if isinstance(i,(int,float)):
#         print(i)

'''59Triangle Patterns'''

# Left Justified Triangle

'''for i in range(1,6):
    print(f"{'*'*i:<5}")

 # Right Justified Triangle

for i in range(1,6):
    print(f"{'*'*i:>5}")

# Equilateral Triangle

for i in range(1,6):
    print(f"{'* '*i:^12}")

# Inverted Triangles (Left Justified)

for i in range(6,0,-1):
    print(f"{'*'*i:<6}")

# Inverted Triangles (Right Justified)

for i in range(6,0,-1):
    print(f"{'*'*i:>6}")

# Inverted Triangles(Centre)

for i in range(6,0,-1):
    print(f"{'* '*i:^12}")

'Number Pattern in triangle (Left Justified)'
pat=''
for i in range(1,6):
    pat+=str(i)
    print(f"{pat:<5}")
# Number Pattern in triangle (Right Justified)
pat=''
for i in range(1,6):
    pat+=str(i)
    print(f'{pat:>5}')

# Number Pattern in triangle (Centre)

pat=''
for i in range(1,6):
    pat=pat + ' ' + str(i)
print(f'{pat:^10}')'''


'''59Write a program to rotate items of the list'''
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# from collections import deque
# def rotate_(rotate,n):
#     d=deque(rotate)
#     d.rotate(n)
#     return list(d)
# print(rotate_(names,1))
# print(rotate_(names,2))

'''60Write a program to count the number of white spaces in a given string'''
# import re
#
# sentence = """Hello world welcome to Python Hi  How are you. Hi how are you"""
# ws=re.findall(f"\s",sentence)
# print(len(ws))

'''61 Write a program to print only non-repeated characters in a string'''
#
# s = 'helloworld'
# count=0
# for i in s:
#     if s.count(i) == 1:
#         count+=1
# print((count),end='')

'''62 Write a program to print all the consonants in a given string'''
#
# s = 'helloworld'
# for i in s:
#     if not i.lower() in 'aeiou':
#         print(i,end='')

'''63 Write a program to check if the year is leap year or not'''
# import calendar
# print(calendar.isleap(2016))

'''64 Write a program to count no of capital letters in a string'''
# import re
# sentence = "Hi How are You WelCome to PytHon"
# CL=re.findall(f'[A-z]',sentence)
# print(len(CL))

'''65 Write a program to get the below output'''
# for i in range(1,5):
#     print('* '*1)
#     j=i+1
#     print('* '*j)
# print(i)

'''66Write a program to get the below output'''
'''[1, 2]
    [3, 4]
    [5, 6]
    [7, 8]
    [9]'''

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0,len(a),2):
#     print(a[i:i+2])



'''67 Write a program to find the first repeating character in a string'''

# s = 'helloworld'
# for i in s:
#     if s.count(i)!=1:
#         print(i,end='')
#         break

'''68 Write a program to find the first non repeating character in a string'''

# s = 'helloworld'
# for i in s:
#     if s.count(i)==1:
#         print(i,end='')
#         break

'''69 Write a program to find the index of nth occurrence of a sub-string in a string'''
#
# sentence = "hello world welcome to python hello hi how are you hello there"
#
# l=sentence.split()
# for index,item,in enumerate(l):
#     print(index,item,end='')

'''70 Write a program to print prime numbers from 1 to 50'''
# for n in range(1,50):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#             else:
#                 print(n,end=',')


'''71 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers first and then even numbers in sorted order'''
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
#
# even_= [i for i in a if i % 2 == 0]
# odd_ = [i for i in a if i % 2 != 0]
# # print(odd_)
# # print(even_)
# c=[*odd_,*even_]
# print(c)
'op=[3, 1, 7, 9, 11, 4, 2, 12, 8, 6] '

'''72rite a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers should be in ascending order and even numbers should be in descending order'''

# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# even_=[i for i in a if i % 2 == 0]
# odd_ =[i for i in a if i % 2 != 0]
# # print(even_)
# s=even_.sort(reverse=True)
# print(s)
# print(odd_)
# a=odd_+s
# print(a)

'''73Write a program to count the number of occurrences of non-special characters in a given string'''

a = 'hello@world! welcome!!! Python$ hi how are you & where are you?'

# from collections import defaultdict
# d=defaultdict(int)
# for i in a:
#     if i.isalnum():
#         d[i] += 1
# print(d,end='')

# op=efaultdict(<class 'int'>, {'h': 5, 'e': 7, 'l': 4, 'o': 7, 'w': 4, 'r': 4, 'd': 1, 'c': 1, 'm': 1, 'P': 1, 'y': 3, 't': 1, 'n': 1, 'i': 1, 'a': 2, 'u': 2})
# Process finishe

'''74Grouping Flowers and Animals in the below list'''

# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

# from collections import defaultdict
# d=defaultdict(list)
# for item_ in items:
#     item_,group = item_.split('-')
#     d[group].append(item_)
# print(d)
# op=defaultdict(<class 'list'>, {'flower': ['lotus', 'lilly', 'sunflower'], 'animal': ['cat', 'dog']})

'''75 Grouping files with same extensions'''

# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
#
# for file in files:
#     a=file.split('.')
#     print(a[-1],end=',')
#
#     op=txt,pdf,pdf,txt,pdf,txt,pdf,


'''Filter only those characters except digits'''

# sen = '@hello12world34welcome!123'
import re
# op = re.findall(r'\D', sen)
# print(op)
#
# OP=['@', 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'w', 'e', 'l', 'c', 'o', 'm', 'e', '!']

'''Count number of words in a sentence. ignore special characters.'''

# sentence = "Hi there! How are you:) How are you doing today!"
# op = re.findall(r'\w+',sentence)
# print(op)
# from collections import defaultdict
# d = defaultdict(int)
# for i in op:
#     d[i] += 1
# print(d)
#
# op=['Hi', 'there', 'How', 'are', 'you', 'How', 'are', 'you', 'doing', 'today']
# defaultdict(<class 'int'>, {'Hi': 1, 'there': 1, 'How': 2, 'are': 2, 'you': 2, 'doing': 1, 'today': 1})


'''102 Grouping even and odd numbers'''
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# from collections import defaultdict
# d = defaultdict(list)
# for i in numbers:
#     if i % 2 == 0:
#         d[0].append(i)
#     else:
#         d[1].append(i)
# print(d)
#
# op=defaultdict(<class 'list'>, {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]})


''' Find all max numbers from the below list'''

# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
#
# mn = max(numbers)
# amn = [i for i in numbers if i == mn]
# print(amn)
#
# op = [4, 4, 4]

'''Can we override a static method in python?'''
#
# class parent():
#     @staticmethod
#     def spam():
#         print("running parent")
# class child(parent):
#     def spam():
#         print('running child')
#
# # c=child()
# a=c.spam()
# print(a)


'''Replace whitespaces with newline character in the below string'''

# sentence = "Hello world welcome to python"
# op = re.sub(r'\s','\n',sentence)
# print(op,end='')
#
# op=Hello
# world
# welcome
# to
# python

'''Replace all vowels with "*"'''
#
# sentence = "hello world welcome to python"
#
# op = re.sub(r'[aeiou]','*',sentence)
# print(op)
#
# op=h*ll* w*rld w*lc*m* t* pyth*n



'''Maximum sum of 3 numbers and Minimum sum of 3 numbers'''

# numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
#
# sn = sorted(numbers)
# print(sn)
# ms3=sorted(sn[-3:])
# print(ms3)
# mis3 = sorted(sn[:3])
# print(mis3)
#
# op= [10, 15, 15, 15, 20, 25, 30, 35, 40]
# [30, 35, 40]
# [10, 15, 15]

''' Write a program to get the output as below'''

# sen= "python@#$%pool"
# # o/p should be ['PYTHON', 'POOL']
#
# op = re.findall(r'\w+',sen)
# print(op)
# con_up = [i.upper() for i in op]
# print(con_up)
#
# op= ['python', 'pool']
# ['PYTHON', 'POOL']

'''Write a program to print all the number which are ending with 5'''
#
# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# for number in numbers:
#     op = re.findall(r'5$',number)
#     if op:
#         print(number)
#
#         op=12345
# 125
# 905
# 55
# 5
# 95655
# 55555

'''Write a program to print all the number which are starting with 8'''

# numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# for i in numbers:
#     op=re.findall(r'^8',i)
#     if op:
#         print(i)
#
#         op=857
# 8
# 888888
# 89

'''Write a program to get the indexes of each item in the below list'''

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# # output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
# from collections import defaultdict
# d = defaultdict(list)
# for index,item in enumerate(names):
#     d[item].append(index)
# print(d)
#
# op=defaultdict(<class 'list'>, {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]})


'''Write a program to print "Bangalore" 10 times without using "for" loop'''

# b=('Bangalore'*10)
# print(b)
#  op=BangaloreBangaloreBangaloreBangaloreBangaloreBangaloreBangaloreBangaloreBangaloreBangalore

''' Write a program to print all the words which starts with letter 'h' in the given string'''

# sen='hello world hi hello universe how are you happy birthday'
# op = re.findall( r'\bh\w+', sen)
# print(op)
#
# op=['hello', 'hi', 'hello', 'how', 'happy']


''' Write a program to sum all even numbers in the given string'''

# sentence = 'hello 123 world 567 welcome to 9724 python'
#
# op =re.findall(r'\d',sentence)
# print(op)
# a=[int(i)for i in op]
# print(a)
# even_=[i for i in a if i % 2 == 0]
# print(sum(even_))

# op=['1', '2', '3', '5', '6', '7', '9', '7', '2', '4']
# [1, 2, 3, 5, 6, 7, 9, 7, 2, 4]
# 14

'''Write a program to filter out even and odd numbers in the given string'''
# sentence = 'hello 123 world 456 welcome to python498675634'
# c = re.findall(r'\d',sentence)
# print(c)
# even_=[i for i in c if int(i) % 2 == 0]
# odd_=[i for i in c if int(i) % 2 != 0]
# print(even_)
# print(odd_)
#
# op=['1', '2', '3', '4', '5', '6', '4', '9', '8', '6', '7', '5', '6', '3', '4']
# ['2', '4', '6', '4', '8', '6', '6', '4']
# ['1', '3', '5', '9', '7', '5', '3']

'''Write a program to remove duplicates from the list without using set or empty list'''

# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# l2 = l1.copy()
# for i in l2:
#     if l1.count(i) > 1:
#         l1.remove(i)
# print(l1)
#
# u = []
# for i in l1:
#     if i not in u:
#         u.append(i)
#         print(i,end='')
#
# a = list(set(l1))
# print(a)


'''Print all the missing numbers from 1 to 10 in the below list'''
#
# numbers = [1, 3, 6, 8, 10]
# for i in range(1,11):
#     if not i in numbers:
#         print(i,end='')
# op=24579

'''Write a python program to get the below output'''
# i1 = [1, 2, 3]
# i2 = ['a', 'b', 'c']
# '''o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']'''
#
# RESULT = ["".join((str(x),y))for x in i1 for y in i2]
# print(RESULT)
#
# op=['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

'''What is the output of the below function call'''

# class demo():
#
#     def spam(self):
#         print('hello')
#     def spam(self):
#         print('python')
#
# d = demo()
# print(d.spam())

# op= python

'''In the list below, find all the number pairs which results in 10 either when added or subtracted'''
#
# a = [3, 5, -4, 8, 11, 1, -1, 6]
# for i1 in a:
#     for i2 in a:
#         if i1 != i2:
#             if i1 + i2 == 10:
#                 print((i1,i2))
# op=(11, -1)
# (-1, 11)

'''Write a decorator to prefix +91 to the original phone numbers'''

numbers = [1234567890, 123456790, 1234567890]


















