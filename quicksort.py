#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quicksort(list):
    if(len(list)<2):
        return list
    else:
        pivot = list[0]
        mid_list = []
        mid_list.append(pivot)
        pre_list = []
        after_list = []
        i = 1
        while(i<len(list)):
            if(list[i]<pivot):
                pre_list.append(list[i])
            else:
                after_list.append(list[i])
            i = i + 1
        return quicksort(pre_list) + mid_list + quicksort(after_list)


if __name__ == '__main__':
    list = [2,3,1,7,4,5,4,8,2,3]
    new_list = quicksort(list)
    print(new_list)