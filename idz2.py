'''
Определить принадлежит ли точка кольцу определяемому окружностями
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a, b = map(float, input("").split())

if a * a+b*b >= 0.25 and a*a+b*b<=1:
    print("Точка принадлежит окружности")
else:
    print("Точка не принадлежит окружности")
