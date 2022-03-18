'''normal func'''

# a=[1,2,3,4]
# res = []
# for i in a:
#     res.append(i**2)
# print(res)

'''generator func'''
def spam(args):
    for i in args:
        yield i ** 2
res=spam(1,2,3)
print(res)

