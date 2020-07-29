#!/usr/bin/env python
# -*- coding: utf-8 -*-

choices = {}
choices["A"] = set([1,2,3])
choices["B"] = set([4,5,6])
choices["C"] = set([1,2,3,4])
choices["D"] = set([6,7,8])
choices["E"] = set([7,8,9])

#近似算法：集合覆盖问题
def greedy(needed_list):
    choosed_list = []
    while(len(needed_list)!=0):
        best_list = []
        best_node = None
        for choice_node in choices:
            tmp_choose = choices[choice_node] & needed_list
            if(len(tmp_choose)>len(best_list)):
                best_list = tmp_choose
                best_node = choice_node
        needed_list = needed_list - best_list
        choosed_list.append(best_node)
    return choosed_list



if __name__ == '__main__':
    needed_list = set([1,2,3,4,5,6,7,8,9])
    choosed_list = greedy(needed_list)
    print(choosed_list)