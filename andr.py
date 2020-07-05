# # А Ане рекомендуется спать
# a = int(input()) 
# # В нельзя спать больше
# b = int(input())
# # H спит сейчас
# h = int(input())
# if (h >= a) and (h <= b):
#     print('Это нормально')
# elif h < a:
#     print('Недосып')
# elif h > b:
#     print('Пересып')


a = int(input()) 
if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
    print('Високосный')
else: 
    print('Обычный')


# a = int(input()) 
# if (a % 4 == 0) and (a % 100 != 0):
#     print('Високосный')
# else: 
#     if a % 400 == 0: 
#         print('Високосный')
#     else:
#         print('Обычный')



