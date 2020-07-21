#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prior = None

class DoubleList:
    def __init__(self):
        self.head = Node(0)
        self.prior = None
        self.next = None
        self.length = 0
    # print list
    def printList(self):
        p = self.head.next
        while(p!=None):
            print(p.data)
            p = p.next
    # add node at head
    def addAtHead(self, val:int):
        new = Node(val)
        if(self.length==0):
            new.prior = self.head
            self.head.next = new
            self.length = self.length + 1
        else:
            self.head.next.prior = new
            new.prior = self.head
            new.next = self.head.next
            self.head.next = new
            self.length = self.length + 1
    # add node at tail
    def addAtTail(self, val:int):
        new = Node(val)
        p = self.head
        while(p.next!=None):
            p = p.next
        p.next = new
        new.prior = p
        self.length = self.length + 1
    # add node at index
    def addAtIndex(self, val:int, index:int):
        if((index<0)or(self.length<index)):
            return
        if(index==0):
            self.addAtHead(val)
        if(index==self.length):
            self.addAtTail(val)
        if((index>0)and(index<self.length)):
            new = Node(val)
            p = self.head
            for i in range(index):
                p = p.next
            new.prior = p
            new.next = p.next
            p.next.prior = new
            p.next = new
            self.length = self.length + 1
    # delete item from list
    def deleteAtIndex(self, index:int):
        if((index<0)or(index>self.length)):
            return
        if(index == self.length):
            p = self.head
            for i in range(self.length):
                p = p.next
            p.prior.next = None
            p.prior = None
            self.length = self.length -1
        else:
            p = self.head
            for i in range(index):
                p = p.next
            p.next = p.next.next
            p.next.next.prior = p
            self.length = self.length - 1

if __name__ == '__main__':
    doublelist = DoubleList()
    doublelist.addAtHead(1)
    doublelist.addAtHead(2)
    doublelist.addAtHead(3)
    doublelist.addAtTail(4)
    doublelist.addAtTail(5)
    doublelist.addAtTail(6)
    doublelist.addAtIndex(9,0)
    doublelist.addAtIndex(11,4)
    doublelist.printList()
    print("---------------")
    doublelist.deleteAtIndex(0)
    doublelist.printList()
    print("---------------")
    doublelist.deleteAtIndex(doublelist.length)
    doublelist.printList()
    print("---------------")
    doublelist.deleteAtIndex(3)
    doublelist.printList()
    print("---------------")