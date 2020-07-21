#!/usr/bin/env python
# -*- coding: utf-8 -*-

def findMAX(list):
    length = len(list)
    max = list[0]
    i = 1
    index = 0
    while(i<length):
        if(max<list[i]):
            max = list[i]
            index = i
        i = i + 1
    return index


def selectionsort(prelist):
    afterlist = []
    length = len(prelist)
    print(length)
    i = 0
    while(i<length):
        index = findMAX(prelist)
        afterlist.append(prelist[index])
        prelist.pop(index)
        i = i + 1
    return afterlist


if __name__ == '__main__':
    prelist = [1,6,3,2,4,8,10,56,12]
    afterlist = selectionsort(prelist) # from big to small
    print(afterlist)