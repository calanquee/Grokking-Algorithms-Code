#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 归并
def merge(left, right):
    result = []
    i = 0
    j = 0
    while((i<len(left))and(j<len(right))):
        if(left[i]<=right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# 分治
def mergesort(list):
    if(len(list)<2):
        return list
    else:
        mid = int(len(list)/2)
        left = mergesort(list[:mid])
        right = mergesort(list[mid:])
        result = merge(left, right)
        return result



if __name__ == '__main__':
    list = [2,3,1,4,5,6,2,4]
    newlist = mergesort(list)
    print(newlist)