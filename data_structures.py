class Array:
    def __init__(self, capacity):       

        self.itemcnt = [None] * capacity
        self.size = 0

    def get(self, index):               # access element by index

        if index < 0 or index >= self.size:
            print("The index out of range")
            return
        
        return self.itemcnt[index]

    def insert(self, index, value):     # insert a value at index's place

        if self.size == len(self.itemcnt):
            print(" The array is full")
            return
        
        if index < 0 or index > self.size:
            print("THe index out of range")
            return

        for i in range(self.size, index, -1):   # loop to shift the numbers to the right
            self.itemcnt[i] = self.itemcnt[i - 1]

        self.itemcnt[index] = value
        self.size += 1

    def delete(self, index):            # remove the value at index
        if index < 0 or index >= self.size:
            print("The index out of range")
            return
        
        value = self.itemcnt[index]

        for i in range(index, self.size - 1):   # loop to shift the numbers to the left
            self.itemcnt[i] = self.itemcnt[i + 1]

        self.itemcnt[self.size - 1] = None
        self.size -= 1

        return value




class Matrix:

    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns
        self.itemcnt = [0] * (rows * columns)

    def getelem(self, i, j):

        return self.itemcnt[i * self.columns + j]

    def setelem(self, i, j, value):
        self.itemcnt[i * self.columns + j] = value

    def delrow(self, i):        #delete rows

        start = i * self.columns
        self.itemcnt = self.itemcnt[:start] + self.itemcnt[start + self.columns:]
        self.rows -= 1

    def insrow(self, i, value):  #insert rows

        start = i * self.columns
        self.itemcnt = self.itemcnt[:start] + value + self.itemcnt[start:]
        self.rows += 1



class Stack:            # stack on a fixed-size array

    def __init__(self, size):

        self.itemcnt = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, value):          #add value in the end 

        if self.top == len(self.itemcnt) - 1:
            print("The stack is full")
            return

        self.top += 1
        self.itemcnt[self.top] = value

    def pop(self):                      #remove and return the last value

        if self.is_empty():
            print("The stack is empty")
            return

        value = self.itemcnt[self.top]

        self.itemcnt[self.top] = None
        self.top -= 1

        return value
        


class Queue:            #circular queue

    def __init__(self, size):

        self.itemcnt = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0


    def enqueue(self, value):       #ad value to the queue at the tail

        if self.count == len(self.itemcnt):
            print("The queue is full")
            return

        self.itemcnt[self.tail] = value
        self.tail = (self.tail + 1) % len(self.itemcnt) #return to 0 after the last place

        self.count += 1


    def dequeue(self):               # remove and return the value that waited the longest

        self.check = self.is_empty()

        if self.check == True:
            print("The queuee is empty")
            return

        value = self.itemcnt[self.head]

        self.itemcnt[self.head] = None
        self.head = (self.head + 1) % len(self.itemcnt)
        self.count -=1

        return value

    


    def is_empty(self):

        if self.count == 0:
            return True
        
        elif self.count > 0: 
            return
        
        else:
            print("Error")
            return



class Node:
    def __init__(self, value):          # one element of the linked list

        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):                 # head is the first node
        self.head = None

    def insert(self, value):            # new node becomes the first one

        node = Node(value)
        node.next = self.head
        self.head = node

    def delete(self, value):            # find the node before it and skip over it

        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head

        while current.next.value != value:  # loop to find the node before the one we delete
            current = current.next


        current.next = current.next.next

    def traverse(self):                 # go through the nodes one by one

        values = []
        current = self.head


        while current is not None:
            values.append(current.value)
            current = current.next


        return values