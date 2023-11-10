points = int(input('Балл'))
if(points >= 90 ):
    print(f'Отлично')
elif(points >= 70):
    print(f'Хорошо')
elif(points >= 50):
    print(f'Удовлетворительно')
elif(points <= 49):
    print(f'Отчислен')