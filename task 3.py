# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk



Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в  нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми шли три цифры. 
После того как все возможные номера были использованы, формат был 
изменен на четыре цифры, предшествующие трем заглавным буквам.
Напишите программу, запрашивающую у пользователя номерной знак 
машины и оповещающую о том, для какого формата подходит данная последовательность символов: для старого или нового. Если введенная последовательность не соответствует ни одному из двух форматов, укажите 
это в сообщении
"""

car_number = str(input())
if(len(car_number) == 6 and car_number[0:3] == car_number[0:3].upper() and car_number[0:3].isalpha() and car_number[3:].isnumeric):
    print('Номер старого формата')
elif(len(car_number) == 7 and car_number[0:4].isnumeric and car_number[4:] == car_number[4:].upper() and car_number[4:].isalpha()):
    print('Номер нового формата')
else:
    print('Некорректный номер')