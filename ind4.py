#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input("Введите строку: ")
l = s.split()
print(min(l, key=len))
