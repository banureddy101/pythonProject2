# s="hello"
# print(sorted(s))
# l=[5,3,6,8,2,3,5,9]
# print(sorted(l))


# l=['hi','hello','banu']
# print(sorted(l,key=len))
#
# sentence="python is a prgrammimg language"
# string=sentence.split()
# shortest, *rest, longest =sorted(string,key=len)
# print(longest,shortest)


# sentence="python is a prgrammimg language"
# string=sentence.split()
# shortest, *rest, longest =sorted(string,key=len)
# print(longest,len(longest),shortest,len(shortest))


# # l=['pytho','java','c','ruby','perl']
# print(sorted(l,key = lambda item : item[-1]))

#
# d={'gmail':5,'wallmart':7,'applez':3,'flipcart':8}
# print(sorted(d.items(),key=lambda item : item[0] [-1]))
#
#
# d={'gmail':5,'wallmart':7,'applez':3,'flipcart':8}
# print(dict(sorted(d.items(),key=lambda item : item[-1])))

#
# d={'gmail':5,'wallmart':7,'applez':3,'flipcart':8}
# print(dict(sorted(d.items(),key=lambda item : item[-1])))
# # print(sorted(d.values()))


#
# t=[('delhi',32),('mumbai',27),('kolkata',30),('chennai',35)]
# print(sorted(t,key=lambda item:item[-1]))
#
# s='hi how are you how is ur health'
# word=s.split()
# d={item: len(item) for item in word}
# res=sorted(d.items(),key=lambda item:item[-1])
# print(res[-1])


# s='hi how are you how is ur health health'
# word=s.split()
# d={item: len(item) for item in word if word.count(item)==1}
# res=sorted(d.items(),key=lambda item:item[-1])
# print(res[-1])
#
# a=map(lambda x:x%2 == 0, [1,2,3,4],[0,1,2,3])
# print(list(a))

a,_,b =(1,2,3)
print(a,_,b)

# a=map(lambda x:x%2 == 0,a)
# print(a(10))