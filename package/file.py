path = r"C:\Users\pc\PycharmProjects\pythonProject2\package\python file directroy\txt_log_files\sample.txt"
# with open(path) as file:
#     for line in file:
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         count+=1
#         print(count)
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         count+=1
#         print(count,line)


# with open(path) as file:
#     for line1,line in enumerate(file,start=1):
#         print(line1,line)

# with open(path) as file:
#     count=0
#     for line in file:
#         sp = line.split()
#         for line in sp:
#             count+=1
#     print(count)

# with open(path) as file:
#     count=0
#     for line in file:
#         sp = line.split()
#             count+=len(sp)
#     print(count)

#
# with open(path) as file:
#     for line in file:
#
#         res=reversed(list(file))
#         print(list(res))

#
# with open(path) as file:
#     count=0
#     for line in file:
#         sp = line.count(" ")
#         count+=sp
# print(count)

# with open(path) as file:
#     count=0
#     for line in file:
#         for word in line.split():
#              if word[0].lower() in 'aeiou':
#                 count+=1
#
#     print(count)

#
# with open(path) as file:
#     d={}
#     for line in file:
#         for word in line.split():
#             d[word]=line.count(word)
#     print(d)



# from collections import defaultdict
# dd=defaultdict(int)
# with open(path) as file:
#     for line in file:
#         for word in line.split():
#             dd[word]+=1
#     print(dd)

# path2 = r"C:\Users\pc\PycharmProjects\pythonProject2\package\python file directroy\txt_log_files\access-log.txt"

# with open(path2) as file:
#     res=[]
#     for line in file:
#         s=line.split()
#         res.append(s[0])
#     print(res)

# with open(path2) as file:
#     d={}
#     count=0
#     for line in file:
#         if line.strip():
#              s=line.split()
#         if s[0] not in d:
#             d[s[0]]=1
#         else:
#             d[s[0]]+=1
#     print(d)

# from collections import defaultdict,Counter
# with open(path2) as file:
#     res=[]
#     for line in file:
#         s=line.split()
#         res.append(s[0])
# ip_= Counter(res)
# print(ip_.most_common(2))





# n=3
# with open(path) as file:
#     for line1,line2 in enumerate(file,start=1):
#         if line1 == n:
#             print(line2)

# #islice
# from itertools import islice
# n=3
# with open(path) as file:
#     res=islice(file,0,n)
#     print(list(res))
# n=3
# with open(path) as file:
#     for line1,line2 in enumerate(file,start=1):
#         if line1<=n:
#     print(line2)
#
#
# from collections import deque
# n=4
# with open(path) as file:
#     line = deque (file,n)
#     print(list(line))
#
# path=r"C:\Users\pc\PycharmProjects\pythonProject2\package\python file directroy\txt_log_files\sample.txt"
#
# f_path=r"C:\Users\pc\PycharmProjects\pythonProject2\package\python file directroy\txt_log_files\sample.txt"
# with open(path,'r') as file read:
#     with open(f_path,'w') as file write:
#         for line in file read:
#             file write.write(line)

# with open(path) as file:
#     for line in file:
#         print(line,len(line))


path3 = r"C:\Users\pc\PycharmProjects\pythonProject2\package\python file directroy\txt_log_files\sample.log"
# with open(path3) as file:
#     for line in file:
#         if line.strip():
#             s = line.split()
#             print(s[2])



# from collections import Counter
# with open(path3) as file:
#     res = []
#     for line in file:
#         if line.strip():
#             s=line.split()
#             res.append(s[2])
# ip= Counter(res)
# print(ip)
#

# path4 = r"C:\Users\pc\PycharmProjects\pythonProject2\package\python file directroy\txt_log_files\football.txt"
# with open(path4,encoding="UTF-8") as file:
#     for line in file:
#         if line.strip():
#             s = line.split("\t")
#             print(s[1])

# from collections import Counter
# from collections import defaultdict
# d=defaultdict(int)
# with open(path) as file:
#     res=[]
#     for line in file:
#         if line.strip():
#             s=line.split()
#             for word in s:
#                 d[word]+=1
# print(d)
# c = Counter(d)
# most, *rest,least = c.most_common()
# print(most,least)

import csv
path5 = r"C:\Users\pc\PycharmProjects\pythonProject3\bpreddy\csv_files\sample.csv"
# with open(path5) as csv_file:
#     read_obj = csv.reader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)

# with open(path5) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)


# import sys
# sys.setrecursionlimit(10000)
# print(sys.setrecursionlimit())

#
# def test (i,j):
#     if i == 0:
#         return j
#     else:
#         return test(i-1,i+j)
# print(test(4,7))

# def recursive_func(string):
#
#     return recursive_func((string[1::]))
# recursive_func
# print("hai")
#
# import sys
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())


import re
items = ["python", 1.2, 9, 1 + 2j, [1, 2, 3], True]

# for item in items:
#     if isinstance(item, (int, float, complex)):
#         print(item)

op=re.findall(r'\d',str(items))
print(op)


