#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lcseque(str1,str2):
    length1 = len(str1)
    length2 = len(str2)
    m = [[0 for i in range(length2+1)] for j in range(length1+1)]
    mmax = 0
    res = []
    for i in range(length1):
        for j in range(length2):
            if(str1[i]==str2[j]):
                m[i+1][j+1] = m[i][j] + 1
                if(m[i+1][j+1]>mmax):
                    mmax = m[i+1][j+1]
                    res.append(str1[i])
            else:
                if(m[i+1][j]>m[i][j+1]):
                    m[i+1][j+1] = m[i+1][j]
                else:
                    m[i+1][j+1] = m[i][j+1]
    result_str = ''.join(res)
    return mmax,result_str




if __name__ == '__main__':
    mmax, res = lcseque("abcde","ace")
    print(mmax)
    print(res)