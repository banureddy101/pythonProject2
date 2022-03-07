

""" WAP to print index and character in a string """

# def char(args):
#     for index,item in enumerate(args):
#         print(index,item)
#
# char('banu')

"""WAP traversing a string in reversed order """
# def trans(args):
#     for item in reversed(args):
#         print(item)
#
# trans('banu')


"""WAP count the number of characters in a string """

# def no(args):
#     count=0
#     for i in args:
#         count+=1
#     print(count)
#

# no('banu')

""" WAP to print even indexed characters in the string """

# def evenidex(args):
#     for item in range(0,len(args),2):
#         print(args[item])
#
#
# evenidex("banu")

"""WAP to print the digits in the string """

# def digits_(args):
#     count=0
#     for char in args:
#         if char.isdigit():
#             count+=1
#     print(count)
#
#
# digits_('banu1233')

"""""WAP to prin the Special symbols"""""

# def alpha_(args):
#     count=0
#     for char in args:
#         if not ("a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9"):
#             count+=1
#     print(count)
#
#
# print(alpha_('@#$%%!@#$hhhhjjj'))



""" capital & small letters """
 
 
# def (args):
#     cap_count = 0
#     small_count = 0
#
#     for char in args:
#         if "a" <= args <= "z":
#             small_count += 1
#         elif "A" <= args <= "Z":
#             cap_count += 1
#
# print(cap_count, small_count)






# s='ppytttthoonnn'
# d={}
# for char in s:
#     d[char]=s.count(char)
# print(d)


# s='banu'
# res=map(char,ord(char),s)
#
#
# print(list(res))


# a=[1,2,3,4]
# b=[5,6,7,8]
# def add_(item1,item2):
#  return item1+item2
# res=map(add_,a,b)
# print(list(res))

# l=['apple','rama','hello']
# def odd_(word):
#  if len(word) % 2 !=0:
#   return word
#
# odd_len=filter(odd_,l)
# print(list(odd_len))




#
# a=['python','java']
# res=map(list,a)
# print(list(res))

# a=[1,2,3,4,5,6,7,8,9,10]
# def seq_(args):
#     for index,item in enumerate(a):
#         return item ** 2
# res=filter(seq_,a)
# print(list(res))

#
# sentence='heelo python is easy'
# list_=sentence.split()
# def vowels_(args):
#     if args[0].lower() in 'aeiou':
#         return args
# res=filter(vowels_,list_)
# print(list(res))

















