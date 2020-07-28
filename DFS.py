#!/usr/bin/env python
# -*- coding: utf-8 -*-

graph = {}
graph["s"] = {}
graph["s"]["a"] = 5
graph["s"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 2
graph["a"]["d"] = 4
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["c"] = 7
graph["c"] = {}
graph["c"]["e"] = 1
graph["d"] = {}
graph["d"]["c"] = 6
graph["d"]["e"] = 3
graph["e"] = {}

processed = []

def find_low_cost_node(costs):
    lowest_node_value = float("inf") #无穷大
    lowest_node = None
    for node in costs:
        if((lowest_node_value>costs[node])and (node not in processed)):
            lowest_node_value = costs[node]
            lowest_node = node
    return lowest_node

costs = {}
parents = {}

def init_cost_parent_list():
    infinity = float("inf")
    costs["a"] = 5
    costs["b"] = 2
    costs["c"] = infinity
    costs["d"] = infinity
    costs["e"] = infinity
    parents["s"] = None
    parents["a"] = "s"
    parents["b"] = "s"
    parents["c"] = None
    parents["d"] = None
    parents["e"] = None


def DFS():
    init_cost_parent_list()
    node = find_low_cost_node(costs)
    while(node!=None):
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if(new_cost<costs[n]):
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_low_cost_node(costs)

def print_result(endpoint):
    # print result
    print(costs[endpoint])
    route = []
    node = endpoint
    while(node!=None):
        route.append(node)
        node = parents[node]
    length = len(route)
    for i in range(length):
        if(i<(length-1)):
            print(route.pop(),end='->')
        else:
            print(route.pop())

if __name__ == '__main__':
    DFS()
    print_result("a")
    print_result("b")
    print_result("c")
    print_result("d")
    print_result("e")

