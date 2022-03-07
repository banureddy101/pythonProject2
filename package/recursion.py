# a=1234
# b=str(a)
# sum=0
# for d in b:
#     sum+=int(d)
# print(sum)


# def dig_(no,sum=0):
#     if no > 0:
#         last = no % 10
#         sum += last
#         no = no // 10
#         return +dig_(no,sum)
#     else:
#         return sum
#
# print(dig_(123))


#
# def dig_(no,sum=0):
#     if no > 0:
#         sum +=no
#         return +dig_(no-1,sum)
#     else:
#         return sum
#
# print(dig_(5))

# def fact_(no,fact=1):
#     if no > 0:
#         fact *=no
#         return fact_(no-1,fact)

#     else:
#         return fact
#
# print(fact_(5))

# def str_reverse(str_i=0):
#     if i<len(str_):
#         return str_[::-1]
# print(str_reverse('banu'))


#
# even=lambda n:n % 2 == 0
# print(even(4))

# mul =lambda n1,n2:n1*n2
# print(mul(3,6))

# seq = lambda s : s[3]
# print(seq((1,2,3,4)))

# pali= lambda seq : seq==seq[::-1]
# print(pali('banu'))


# even_odd=lambda n:n if n % 2 == 0 else "it is odd"
# print(even_odd(5))

# l=[1,2,3,4,5]
# even_odd=lambda n: if n % 2 == 0 else "it is odd"
# res=map(even_odd,l)
# print(list(res))
l=[1,2,3,4,5]
# even_odd=lambda l : f"{l} is a even no" if l % 2 == 0 else f"{l} is an odd"
# res=map(even_odd,l)
# print(list(res))

# e=['apple','gmail','yahoo','filp']
# start_vowel=lambda e : e[0].lower() in 'aeiou'
# res=map(start_vowel,e)
# print(list(res))


##print the no 1 to 10####

def count_up(start,end):
    if start>end:
        return
    print(start)
    count_up(start+1,end)
count_up(1,10)

##print the no 10 to 1####

def count_down(start,end):
    if start<end:
        return
    print(start)
    count_down(start-1,end)
count_down(10,1)

add the digits of num#

def sum_(num,sum=0):
    if num>0:
        last=num%10
        sum+=last
        num=num//10
        return sum_(num,sum)
    else:
        return sum
print(sum_(123))

sum of the first n no#

def sum_(n,sum=0):
    if n>0:
        sum+=n
        return sum_(n-1,sum)
    else:
        return sum
print(sum_(5))

factorial no#

def fact_(n,fact=1):
    if n>0:
        fact*=n
        return fact_(n-1,fact)
    else:
        return fact
print(fact_(5))

#count the no of digits in a number#

def count_(n,count=0):
    if n>0:
        count+=1
        return count_(n//10,count)
    else:
        return count
print(count_(1222))


reverse string#


def reverse_string(string,i=0,res=""):
    if i<len(string):
        res=string[i]+res
        return reverse_string(string, i+1, res)
    else:
        return res
print(reverse_string('hello')

def reverse_string(args):
    return args[::-1]
print(reverse_string("hai"))



