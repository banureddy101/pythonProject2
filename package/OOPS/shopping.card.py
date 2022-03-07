# class shoppingCart:
#     products={'i6':5,'imac':9,'ipad':6,'iwatch':8}
#     prices = {'i6': 800, 'imac': 4500, 'ipad': 5000, 'iwatch': 3000}
#     def __init__(self):
#         self.cart = []
#
#     def add_item(self,name,quantity):
#         if name not in self.__class__.products:
#             raise Exception('invalid product')
#         elif quantity <= self.__class__.products[name]:
#             self.cart.append({'name':name,'quantity':quantity,'prices':self.__class__.prices[name]})
#             self.__class__.products[name] -= quantity
#         else:
#             raise ValueError('products out of stack')
#
#     def total_cost(self):
#         total=0.00
#         for item in self.cart:
#             total = total+(item['quantity'] * item['prices'])
#         return total
#
#
#     def remove_items(self,name):
#         for item in self.cart:
#             if item['name'] == name:
#                 if item['quantity'] >1:
#                     item ['quantity'] -=1
#                 else:
#                     self.cart.remove(item)
#
#
#
# c1 = shoppingCart()
# c2 = shoppingCart()
# c3 = shoppingCart()
#
# # print(c1.__dict__)
#
#
# print(c1.add_item('i6',1))
# print(c1.add_item('imac',1))
# print(c1.add_item('ipad',2))
# print(c1.add_item('iwatch',2))
# print(c1.__dict__)
# # print(c1.remove_items('i6'))
# # print(c1.cart)
#
# print(shoppingCart.products)


