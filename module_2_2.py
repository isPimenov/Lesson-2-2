a = input('Введите число 1:')
b = input('Введите число 2:')
c = input('Введите число 3:')
if a==b==c:
    print('Результат: ',3)
elif (a==b!=c) or (a!=b==c) or (a==c!=b):
    print('Результат: ',2)
else:
    print('Результат: ',0)