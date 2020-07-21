#!/usr/bin/env python
# -*- coding: utf-8 -*-

def BiSearch(list,item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((high+low)/2)
        guess = list[mid]
        if(guess<item):
            low = mid + 1
        if(guess==item):
            return mid
        if(guess>item):
            high = mid - 1
    return None


if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,10,12,14,20]
    mid = BiSearch(my_list,2)
    print(mid)