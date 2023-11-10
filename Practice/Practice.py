##29.09.23


#Задача 3
# x = int(input('Введите кол-во элементов = '))
# spisok = []
# i = 0
# while(i < x):
#     y = int(input('Введите элемент = '))
#     spisok.append(y)
#     i+=1
# sorted_list = sorted(spisok)
# print(sorted_list)

##05.10.23

##Задача 3

#Lite

# x = 0
# my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78 ,23, 89, 23, 36]
# for element in my_list:
#     x += element
# print(x)

##Задача 4

# my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78 ,23, 89, 23, 36]
# x = 0
# for element in my_list:
#     if(element > x):
#         x = element
# print(x)

##Задача 5

# sweets = {'Наташа': 2,'Алина': 3,'Марат': 15,'Лев': 1,'Валера':0 ,'Рома':4}
# my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78 ,23, 89, 23, 36]
# x = 0
# for element in my_list:
#     if(element > x):
#         x = element
# sweets['Рома'] = x
# print(sweets)

#Pro

#Задача 1
# x = '@ '
# for i in range(6):
#     print(i*x)

#Задача 2
# x = 0
# y = 0
# for i in range(1,10):
#     y+=1
#     if(y < 6):
#         x+=1
#     elif(y > 5):
#         x-=1
#     print(x * f'{i}')

#Задача 4

# d1 = int(input('Введите значение первого кубика'))
# d2 = int(input('ВВедите значение второго кубика'))
# if 0<d1<7:
#     if 0 < d2 < 7:
#         if d1 + d2 == 7 or d1 + d2 == 11:
#             print(f'Я выиграл')
#         elif d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 == 12:
#             print(f'Я проиграл')
#         else:
#             print(f"Сумма = {d1 + d2}")
#
#     else:
#         print('error 2')
# else:
#     print('error 1')

#ULTRAPRO

#Задача 1

Spisok = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# x = 0
# for i in range(1,21):
#     x+=i
# print(x)

# i=0
# x=0
# while(i<20):
#     x+=Spisok[i]
#     i+=1
#
# print(x)

# x = sum(Spisok)
# print(x)

# x = 0
# for element in Spisok:
#     x+=element
# print(x)

# i = 0
# x = 0
# while(i < len(Spisok)):
#     x += Spisok[i]
#     i+=1
# print(x)


#Задача 2

# sample_list = ["мандаринки", "киви", "лимон"]
# new_sample_list = []
# x = int(input('Введите n'))
# y = 1
# for element in sample_list:
#     for i in range(0,3):
#         new_sample_list.append(element + f"_{y}")
#     y+=1
#     if(y > x):
#         break
# print(new_sample_list)

#Задача 3
# i=0
# Spisok = [3, "котики", 0.45,5,{'котики': 2,'слоники':9},"слоники", 34]
# for element in Spisok:
#     if (type(element) == dict):
#         break
#     i+=1
# print(i)

#Задача 4

# dict = {}
# for  i in range(1,21):
#     dict[f'{i}'] = i*i
# print(dict)

#Задача 5

string = '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]'
string = string[1:-1]
spisok = []
print(string)
string = string.replace(' ', '')
for element in string:
    if (element == ','):
        element = ''
    element = int(element)
    spisok.append(element)
print(element)