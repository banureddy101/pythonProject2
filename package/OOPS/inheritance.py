# class parent:
#     def __init__(self,value):
#         self.value = value
#
#     def google(self):
#         print(f'excuting parent google  {self.value}')
#
#     def apple(self):
#         print('excuting parent apple')
#         self.google()
#
# class child1(parent):
#     def demo
#
# p=parent(10)
#
# print(p.google())
# print(p.apple())

class count:
    def __init__(self, func):
        self.func = func
        self.count=0
    def __call__ (self, *args, **kwargs):
        self.count+=1
        return self.func(*args, **kwargs)

@count
def add(a,b):
    return a+b
# print(add(1,2))

# @count
# def sub(a,b):
#     return a-b
# print(sub(5,9))