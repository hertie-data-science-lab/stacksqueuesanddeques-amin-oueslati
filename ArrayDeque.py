# -*- coding: utf-8 -*-
"""
Submitted on 19th March 2022

@author: Oskar Krafft | Paul Sharratt | Fabian Mertz | Amin Oueslati
"""

### Assumptions:

# In line with the book, whenever the queue is full and at max capacity, appending on either side will pop (= overwrite) an entry from the opposite side.
# 

class Empty(Exception): pass

class ArrayDequeMaxlen(): 
    
    DEFAULT_CAPACITY = 10
        
    def __init__(self, max_len):
        self._data = [None] * ArrayDequeMaxlen.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self.max_len = max_len

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        first = self._data[self._front] 
        return first

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        last = self._data[((self._front + self._size) - 1) % len(self._data)]
        return last

    def dequeue_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = [None]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def dequeue_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self.last()
        self._data[((self._front + self._size) - 1) % len(self._data)] = [None]
        self._size -= 1
        return answer

    def enqueue_first(self, e):
        if self._size == len(self._data):
            self._resize(min(2 * len(self._data), self.max_len))
        avail = (self._front - 1) % len(self._data)
        self._data[avail] = e
        self._front = (self._front - 1) % len(self._data)
        if self._size != len(self._data):
            self._size += 1

    def enqueue_last(self, e):
        if self._size == len(self._data):
            self._resize(min(2 * len(self._data), self.max_len))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        if self._size == len(self._data):
            self._front = (self._front + 1) % len(self._data)
        if self._size != len(self._data):
            self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0