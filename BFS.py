#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

graph = {}
graph["S"] = ["A","C","D"]
graph["A"] = ["B","C"]
graph["B"] = ["F"]
graph["C"] = ["D","E"]
graph["D"] = ["F"]
graph["E"] = ["F"]
graph["F"] = []

# if str in/not in the graph
def BFS(str):
    search_queue = deque()
    search_queue += graph["S"]
    searched_node = []
    while(search_queue!=None):
        if(len(search_queue)==0):
            return False
        pre_search_node = search_queue.popleft()
        if not pre_search_node in searched_node:
            if(pre_search_node==str):
                return True
            else:
                search_queue += graph[pre_search_node]
                searched_node.append(pre_search_node)
    return False


if __name__ == '__main__':
    if(BFS("C")==True):
        print("In the graph")
    else:
        print("Not in the graph")