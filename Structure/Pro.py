# spisok = [55,7,80,5,90]
# for element in spisok:
#     if(element > 50):
#         element + 100
#     else:
#         element * element
# print(spisok)

spisok = [55,7,80,5,90]
for i in range(0,5):
    if(spisok[i] > 50):
        spisok[i]+=100
    else:
        spisok[i] *= spisok[i]
print(spisok)