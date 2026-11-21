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



def partition_random(data, start, end):    #creating quicksort partition with a random pivot

    randnum = random.randint(start, end)

    data[end], data[randnum] = data[randnum], data[end]

    return partition(data, start, end)



def quickselect_random(data, start, end, k):

    while start < end:

        p = partition_random(data, start, end)

        if k == p:
            return data[p]
        elif k < p:
            end = p - 1
        elif k > p:
            start = p + 1

    return data[start]



def partition_around(data, start, end, pivot):     

    low = start         #smaller than the pivot
    i = start
    high = end          #bigger than the pivot

    while i <= high:    # loop to put each number into its part

        if data[i] < pivot:
            data[low], data[i] = data[i], data[low]
            low += 1
            i += 1

        elif data[i] > pivot:
            data[i], data[high] = data[high], data[i]
            high -= 1

        else:
            i += 1

    return low, high    # the numbers equal to the pivot go between low and high



def quickselect_deterministic(data, start, end, k):

    while end - start >= 5:

        medians = []        #create list for medians to go 

        for i in range(start, end + 1, 5):      #put each median into the list 
            five = sorted(data[i:min(i + 5, end + 1)]) 
    
            medians.append(five[len(five) // 2])

        pivot = quickselect_deterministic(medians, 0, len(medians) - 1, len(medians) // 2) #find medians of medians
        low, high = partition_around(data, start, end, pivot)

        if k < low:
            end = low - 1
        elif k > high:
            start = high + 1
        else:
            return pivot

    return sorted(data[start:end + 1])[k - start]    
