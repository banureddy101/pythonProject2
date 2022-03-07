# l=[1,2,3,4,5]
# list=[]
# list=[ item for item in l]
# print(list)
# l = ["python", 10, 3.2, "selenium", "Java"]

""" traversing through list """

# for item in l:
#     print(item, end=" ")
#
# print()
#
# for i in range(len(l)):
#     print(l[i], end=" ")

##list comprehensive
#
# op=(item for item in l)
# print(op)

""" print index and its corresponding item in the list """
# l = ["python", 10, 3.2, "selenium", "Java"]
#
# for i in range(len(l)):
#     print(l[i], i)


# for index, item in enumerate(l):
#     print(index, item)

##list comprehensive

# op=[(index,item) for index,item in enumerate(l)]
# print(op)

""" traversing through a list in reversed order """

# l = ["python", 10, 3.2, "selenium", "Java"]

# # using range
# for i in range(len(l)-1, -1, -1):
#     print(l[i], end=" ")
#
# print()
# # using slicing
# for i in l[::-1]:
#     print(i, end=" ")
#
# print()
# # using reversed()
# for i in reversed(l):
#     print(i, end=" ")

# op=[i for i in reversed(l)]
# print(op)

# op=[i for i in l[::-1]]
# print(op)
#
# op=[(i, l[i]) for i in range(len(l)-1,-1,-1)]
# print(op)

""" print even indexed elements in the list """

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# # using range
#
# for i in range(0, len(l), 2):
#     print(l[i], end=" ")
# print()
#
# # using slicing
# for i in l[::2]:
#     print(i, end=" ")
# print()
#
# # using condition
# for i in range(len(l)):
#     if i % 2 == 0:
#         print(l[i])
# op=[i for i in range(len(l)) if i % 2 == 0]
# print(op)

# op=[i for i in range(0,len(l),2)]
# print(op)
# op=[i for i in l[::2]]
# print(op)

""" print integers in a list """
#
# l = ["python", 10, 3.2, "selenium", "Java"]
#
# for item in l:
#     if isinstance(item, int):
#         print(item)

# op=[i for i in l if isinstance(i,int)]
# print(op)

""" print only numeric datatypes"""

# l = ["python", 10, 3.2, "selenium", "Java"]

# for i in l:
#     if isinstance(i, (int, float, complex)):
#         print(i)

# op=[i for i in l if isinstance(i,(int,complex,float))]
# print(op)

""" print length of each string in the list """

# l = ["python", "Node JS", "selenium", "Java"]

# for item in l:
# #     print((item, len(item)))
#
# op=[(i,len(i)) for i in l]
# print(op)

""" print the strings with even length """

l = ["python", "Node JS", "selenium", "Java"]
# res = []
# for item in l:
#     if len(item) % 2 == 0:
#         res.append(item)
#     else:
#         res.append(item[::-1])

# # print(res)
# op=[item[::-1] if len(item) % 2 == 0 else item for item in l]
# print(op)



""" reverse string elements or else keep it as it is"""

# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
# res = []
# for item in list_:
#     if isinstance(item, str):
#         res.append(item[::-1])
#     else:
#         res.append(item)

# print(res)

# op=[ item[::-1] if isinstance(item,str) else item for item in l]
# print(op)

""" print if the element is starting with vowel """

# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]

# for ele in files:
#     if ele[0].lower() in "aeiou":
#         print(ele)
#
# op=[item for item in files if item[0].lower() in 'aeiou']
# print(op)

""" print all the extensions in the following list """

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]

# for file in files:
#     a = file.split(".")
#     print(a[-1])

# op=[item.split('.')[-1]for item in files]
# print(op)

""" printing file name with odd length """
#
# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]

# for item in files:
#     a = item.split(".")
#     if len(a[0]) % 2 == 0:
#         pass
#     else:
#         print(a[0])


# op=[item if len(a[0]) % 2== 0 else item for item in files]
# print(op)
""" index of first occurrence of the given element in the list"""
#
numbers = [10, 40, 20, 80, 20, 40, 30]
num = 80
# #
# # for index, item in enumerate(numbers):
# #     if item == num:
# #         print(f"{num} is present at the index {index}")
# #         break
# #
# # # else:
# # #     print("element is not present")
# #
# op=[item if item == num  else item for index,item in enumerate(numbers)]

# op=[item,for item,index in enumerate(numbers) if index==num]
# print(op)


""" check if the number is a prime number """

# n=10

# for i in range(2, n):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")



# op=[i for i in range(10) i if n % i == 0]
# op=[i if n % i == 0  else i for i in range(2,n)]
# print(op)

""" to generate prime number series"""
# l = [1, 5, 8, 6, 3, 98, 12, 5]

# for n in range(10):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)

""" print the elements other than the given element"""
# numbers = [10, 40, 20, 80, 20, 40, 30]
# n = 20
# #
# # for num in numbers:
# #     if n == num:
# #         continue
# #     print(num)
#
#
#
# op=[item for item in numbers item if n == item]
# print(op)

# """ print the palindromes in the given list """
# l = ["python", "dad", "hai", "malayalam", "madam", "mom"]

# for element in l:
#     if element == element[::-1]:
#         print(element)

#
# op=[item for item in l if item == item[::-1]]
# print(op)










