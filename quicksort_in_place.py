import random

def partition(data, start, end):

    pivot = data[end]   # take last number as a pivot

    i = start - 1

    for j in range(start, end): # sorting loop

        if data[j] <= pivot: # how comparison in place happens
            i += 1
            data[i], data[j] = data[j], data[i] # switch

    data[i + 1], data[end] = data[end], data[i + 1]

    return i + 1

    
def quicksort_deterministic(data, start, end):  #quicksort function recursively calling quicksort on partitions

    if start < end:
        part = partition(data, start, end)
        quicksort_deterministic(data, start, part - 1)
        quicksort_deterministic(data, part + 1, end)

def partition_random(data, start, end):    #creating quicksort partition with a random pivot

    randnum = random.randint(start, end)

    data[end], data[randnum] = data[randnum], data[end]

    return partition(data, start, end)


def quicksort_random(data, start, end): #quicksort function recursively calling quicksort random on partitions

    if start < end:
        part = partition_random(data, start, end)
        quicksort_random(data, start, part - 1)
        quicksort_random(data, part + 1, end)


