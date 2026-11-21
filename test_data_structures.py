from data_structures import *

def test_structures():
    array = Array(5)
    array.insert(0, 10)
    array.insert(1, 30)
    array.insert(1, 20)                 # insert values into array

    array.delete(0)                     # remove values from the array

    print("array:", array.itemcnt[:array.size], "/ index 1:", array.get(1))



    matrix = Matrix(2, 3)
    matrix.setelem(1, 2, 7)

    print("matrix [1][2]:", matrix.getelem(1, 2), "/ stored as:", matrix.itemcnt)

    stack = Stack(3)

    for value in [1, 2, 3]:
        stack.push(value)

    print("stack pops:", stack.pop(), stack.pop(), stack.pop())




    queue = Queue(3)

    for value in [1, 2, 3]:
        queue.enqueue(value)

    first = queue.dequeue()
    queue.enqueue(4)                    # goes into the free place at the start


    print("queue dequeues:", first, queue.dequeue(), queue.dequeue(), queue.dequeue())


    

    linked = LinkedList()

    for value in [3, 2, 1]:
        linked.insert(value)

    linked.delete(2)
    print("linked list:", linked.traverse())