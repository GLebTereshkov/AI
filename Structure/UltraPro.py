spisok = []
for i in range(0,5):
    x = int(input('Введите значение '))
    spisok.append(x)
print(spisok)
sorted_list = sorted(spisok)
for i in range(0,5):
    if(sorted_list[i] > 50):
        sorted_list[i] += 100
    else:
        sorted_list[i] *= sorted_list[i]
print(sorted_list)