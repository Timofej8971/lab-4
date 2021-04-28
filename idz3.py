#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 10000
i = 0

while x < 15000:
    x += x / 10
    i += 1

print ("Нужно дней", i)
