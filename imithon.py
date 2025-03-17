# 1-misol
# info = {}

# for i in range(2):  
#     name = input(f"{i+1}-kishining ismini kiriting: ")
#     try:
#         age = int(input(f"{name}ning yoshini kiriting: "))
#         info[name] = age
#     except ValueError:
#         print(" yoshingizni kiriting kiriting!")
#         exit()

# boy = min(info, key=info.get)
# print(boy)
# 3-misol
# string = 'Muhammadqodir'
# another_string = []
# indeces = []
# for i in string.lower():
#     another_string.append(i)
#
# for j in another_string:
#     indeces.append(another_string.count(j))
#
# print(f'{another_string[indeces.index(max(indeces))]} harf {max(indeces)} marta yozilgan')

# 4-misol
# my_set = {6, 5, 17, 9, 2, 10}
# your_set = {1, 9, 10, 22, 17}
# my_lst = list(my_set.intersection(your_set))
#
# print(sorted(my_lst, reverse=True))