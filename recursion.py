#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum(list):
    if(list==[]):
        return 0
    else:
        return list[0] + sum(list[1:])

def count(list):
    if(list==[]):
        return 0
    else:
        return 1 + count(list[1:])

def multiply(list):
    if(list==[]):
        return 1
    else:
        return list[0]*multiply(list[1:])

def findMAX(list):
    if(list==[]):
        return 0
    if(len(list)==1):
        return list[0]
    else:
        if(list[0]>findMAX(list[1:])):
            return list[0]
        else:
            return findMAX(list[1:])


if __name__ == '__main__':
    list = [2,3,4,7,5,6]
    result = sum(list)
    result = count(list)
    result = multiply(list)
    result = findMAX(list)
    print(result)