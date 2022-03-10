# s='python'
# s.split(s)
# print(s)



# a='555'
# if 'a'<=a<='z':
#     print(a, 'is lower case')
# elif 'A'<=a<='Z':
#     print(a,'is upeer')
# else:
#     print("none")

#
# iterable={1,2,3}
# if bool(iterable):
#     print('iterable')
# elif bool(set_):
#     print('not iterable')

# iterable=:{'a':1,'b':2.'c'=3}
# if len(iterable)>0:
#     print("the iterable not empt")
# else:
#     print('the iterable is empty')
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

a=10
# b=15
# c=30
# if a>b and a>c:
#     print('a greater')
# elif b>c:
#     print('b greater')
# else:
#     print('c greater')


# char='f'
# if char.lower() in 'aeiou':
#     print('vowel')
# elif char.lower() not in 'aeiou':
#     print('not vowel')

# n=10
# while n>0:
#     print(n,end="")
#     n-=1

# n=-1
# # while n>=-10:
# #     print(n,end="")
# #     n-=1
#
# n=-10
# while n<0:
#     print(n,end="")
#     n+=1
#
#


# n=0
# while n<=50:
#     print(n,end='')
#     n+


# n ='banu'
# i=0
# while i<len(n):
#     print(n[i],end="")
#     i+=1



# a='banu'
# while n<=u:
#     print(n)
#     a+=b

# l=[1,2,3,4,5]
# op=(item**2 for item in l)
# print(list(op))

# a='banu'
# for char in range(len(a)-1,-1,-1):
#     print(a[char])
# for char in a[::-1]:
#     print(char)

# for char in reversed('banu'):
#     print(char)


#wagf to yiled even nos in the range1 to 50##
#
# def even_():
#     for item in range(1,51):
#         if item %2 == 0:
#             yield item
# even_no=even_()
# print(list(even_no))
#
# op=(item for item in range(1,51) if item %2 == 0)
# print(list(op))

#WAGF and expression to yield the names starting with voweils in the given list##
names=['johns','hello','apple']
# def even_():
#     for item in names:
#         if item[0].lower() in 'aeiou':
#             yield item
# even_n=even_()
# print(list(even_n))

# op=(item for item in names if item[0].lower() in 'aeiou')
# print(list(op))

##wagF to yield length of each line in a file only if the line is not empty##

# path=r''
# def len_file():
#     with open(path) as file:
#         for line in file:
#             if line.strip():
#                 yield line
# lines=len_file()
# print(lines)

from selenium import webdriver
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self,driver):
#         result=super().__call__(driver)
#         if isinstance(result,WebElement):
#             return result.is_enabled()
#         else:
#             return False
#
# def wait(func):
#     def wrapper(*args,**kwargs):
#         locator = args[0]
#         wait = WebdriverWait(driver,20)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args,**kwargs)
#     return wrapper
#
# @Wait
# def click_text(locator):
#     driver.find_element(*locator).click()
#
# @wait
# def enter_element(locator,value):
#     driver.find_element(*locator).send_keys(value)
#
# @wait
# def select_item(locator,item)
# element=driver.find_element(locator)
# s=Select(element)
# if isinstance(item,str)
#     s.select_by_visible_text(item)
#     if isinstance(item,int):
#         s.select _visibility_of_element_index(select_item)
#     else:
#         raise TypeError


