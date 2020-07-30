#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lcsubstr(str1, str2):
    # i 为列 j 为行
    m = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    mmax = 0
    p = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if(str1[i]==str2[j]):
                m[i+1][j+1] = m[i][j] + 1
                if(m[i+1][j+1]>mmax):
                    mmax = m[i+1][j+1]
                    p = i + 1
    return str1[(p-mmax):p], mmax

if __name__ == '__main__':
    result_list, result = lcsubstr("python","thin")
    print(result_list)
    print(result)