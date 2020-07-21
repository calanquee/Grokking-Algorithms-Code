#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class NodeList:
    def __init__(self):
        self.head = Node(0)
    # add node at head
    def addAtHead(self,val:int):
        new = Node(val)
        new.next = self.head.next
        self.head.next = new
    # add node at tail
    def addAtTail(self,val:int):
        new = Node(val)
        p = self.head
        while(p.next!=None):
            p = p.next
        p.next = new
    # add index node
    def addAtIndex(self,val:int,index:int):
        new = Node(val)
        p = self.head
        for i in range(index):
            if(p==None):
                return
            p = p.next
        if(p!=None):
            new.next = p.next
            p.next = new
        else:
            p = new
    # print single list
    def printlist(self):
        p = self.head.next
        while(p!=None):
            print(p.data)
            p = p.next
    # delete item from list
    def deleteAtIndex(self,index:int):
        if(index<0):
            return
        else:
            p = self.head
            for i in range(index):
                if(p==None):
                    return
                p = p.next
            if(p.next!=None):
                p.next = p.next.next
    # get index's data
    def getDataAtIndex(self,index:int) -> int:
        if(index<0):
            return None
        else:
            p = self.head
            for i in range(index+1):
                p = p.next
                if(p==None):
                    return None
            return p.data



if __name__ == '__main__':
    singlelist = NodeList()
    singlelist.addAtHead(1)
    singlelist.addAtHead(2)
    singlelist.addAtHead(3)
    singlelist.addAtTail(4)
    singlelist.addAtTail(5)
    singlelist.addAtTail(6)
    singlelist.printlist()
    print("-----------")
    singlelist.deleteAtIndex(0)
    singlelist.addAtIndex(10,0)
    singlelist.printlist()
    print("-----------")
    print(singlelist.getDataAtIndex(0))