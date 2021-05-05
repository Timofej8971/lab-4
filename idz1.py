'''Дано целое число С такое, что С . Вывести это число в словесной форме, учитывая его
знак
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input("Введите число: "))

if x < 0:
    minus = "минус "
else:
    minus = ""

mas = ["один", "два", "три", "четыри", "пять", "шесть", "семь", "восемь", "девять"]
chislo = mas[abs(x)-1]

otvet = minus + chislo
print(otvet)
