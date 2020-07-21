#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class CircularList:
    def __init__(self):
        self.head = Node(0)
        self.next = None
        self.length = 0
    # print single list
    def printlist(self):
        p = self.head.next
        for i in range(8):
            print(p.data)
            p = p.next
    # add node at head
    def addAtHead(self, val:int):
        new = Node(val)
        if(self.length == 0):
            self.head.next = new
            new.next = new
            self.length = self.length +1
        else:
            p = self.head
            p = p.next
            while(p.next!=self.head.next):
                p = p.next
            p.next = new
            new.next = self.head.next
            self.head.next = new
            self.length = self.length + 1
    # add node at tail
    def addAtTail(self, val:int):
        if(self.length==0):
            self.addAtHead(val)
        else:
            new = Node(val)
            p = self.head
            for i in range(self.length):
                p = p.next
            p.next = new
            new.next = self.head.next
            self.length = self.length + 1
    # add node at index
    def addAtIndex(self, val:int, index:int):
        if((index<0)or(index>self.length)):
            return
        if(index==0):
            self.addAtHead(val)
        if(index==self.length):
            self.addAtTail(val)
        else:
            new = Node(val)
            p = self.head
            for i in range(index):
                p = p.next
            new.next = p.next
            p.next = new
            self.length = self.length + 1
    # delete node from list
    def deleteAtIndex(self, index:int):
        if((index<0)or(index>=self.length)):
            return
        if(index==0):
            self.head.next = self.head.next.next
            p = self.head
            for i in range((self.length-1)):
                p = p.next
            p.next = self.head.next
            self.length = self.length - 1
        else:
            p = self.head
            for i in range(index):
                p = p.next
            p.next = p.next.next
            self.length = self.length - 1


if __name__ == '__main__':
    circularList = CircularList()
    circularList.addAtHead(1)
    circularList.addAtHead(2)
    circularList.addAtTail(4)
    circularList.addAtIndex(10,2)
    circularList.printlist()
    print("---------")
    circularList.deleteAtIndex(0)
    circularList.printlist()
    print("---------")
    circularList.deleteAtIndex((circularList.length-1))
    circularList.printlist()
    print("---------")
    circularList.deleteAtIndex(1)
    circularList.printlist()
    print("---------")
