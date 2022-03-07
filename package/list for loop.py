# l=['python',10,3,2,'selinium','java']
# # for char in l [::-1]:
#     print(char)

# l=['python',10,3,2,'selinium','java']
# for ele in reversed(l):
#     print(ele)

# l=['python',10,3,2,'selinium','java']
# for char in l [::2]:
#      print(char)

# l=['python',10,3.2,'selinium','java']
# for char in l [1:7:2]:
#      print(char)

# l = ['python', 10, 3.2, 'selinium', 'java']
# for char in range (len(l)):
#     if char % 2 == 1:
#          print(l[char],end=" ")


# l = ['python', 10, 3.2, 'selinium', 'java']
# for item in l:
#     if isinstance(item,int):
#         print(item)

# l = ['python', 10, 3.2, 'selinium', 'java']
# for item in l:
#     if isinstance(item,(int,complex,float)):
#         print(item)


#
# l = ['python', 'selinium', 'java']
# for i in l:
#     print(i,(len(l)))



# l = ['python', 'selinium', 'java','banu','mom']
# for i in l:
#     if len(i) % 2 == 0:
#          print(i)



# l = ['python', 'selinium', 'java','banu','mom']
# for i in l:
#     if not len(i) % 2 == 0:
#          print(i)

# l= ['python', 'selinium', 'java', 'banu', 'mom']
#
# l2=[]
# for i in l:
#      if len(i) % 2 == 0:
#          l2.append(i)
# print(l2)


#
# l = ['python', 'selinium', 'java','banu','mom','qspider']
# for i in l:
#     if len(i) % 2 == 0:
#         print(i)
#     else:
#         print(i[::-1])



# l = ['python', 'selinium', 'java','banu','mom','qspider']
# l2=[]
# for i in l:
#     if len(i) % 2 == 0:
#         l2.append(i)
#     else:
#         l2.append(i[::-1])

# l = ['python', 10, 10.0, 2+2j]
# str_=[]
# tup_=[]
# for i in l:
#     if isinstance(i, str):
#         str_.append(i[::-1])
# else:
#     str_.append(i)
# print(str_)

# files=["youtube.txt","amezon.pdf","apple.xls","flipcart.in"]
# lis_=[]
# for ele in files:
#     lis_.append(ele.split(".")[1])
# print(lis_)


# files=["youtube.txt","amezon.pdf","apple.xls","flipcart.in"]
# for ele in files:
#     a = ele.split(".")
#     if len(a[0]) % 2 == 0:
#         pass
#     else:
#         print(a[0])

#
# nums=['hi','helllo','ram',10,40,20,80,20,40,30]
# print(nums.index(40))



###prime nos

# for n in range(10):
#     if n>1:
#         for n in range(2,0):
#             if n % == 0:
#                 break
# else:
# print(n)




numbers=[10,20,40,20,30,50]
num=20
for n in numbers:
    if num % n == 0:
        break
print(num)







