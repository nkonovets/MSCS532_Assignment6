# Assignment 6 Report

## Part 1: Quick Select Algorithms

Quickselect is an algorithm that finds the k-th smallest number in a list without sorting it. It works quite similarly to quicksort, with its pivot dividing the list into partitions, where quickselect later finds the value it needs.

### Implementation

For this assignment, I have implemented quick select along with an elementary data structure inspired by the textbook’s example. For randomized selection, I have reused my partition function from previous assignments. A random pivot is swapped to the end, the partition puts it in its final sorted position p, and quickselect continues only on the side that contains k. For deterministic selection, I decided to use a list of medians, which would then also be used to find medians in that list: the range is split into groups of five, the median of each group is found, and the median of those medians becomes the pivot. At first, I decided to use the partition from my implementation of Assignment 5, but it became very slow when sorting repeated values, so I fixed it by using a three-way partition that groups smaller, equal, and larger values.

### Analysis

Randomized quickselect came out to be O(n) on average, because each partition removed about half of the remaining numbers, so the work added up to about 2n. In the worst case, a bad pivot removes just one number each round, which makes it O(n²), though a random pivot makes this very unlikely. The median of medians always picks a pivot that removes at least 30% of the numbers, so it remains O(n) even in the worst case. Both algorithms work in place and need very little extra memory, apart from the short list of medians.

**Table 1**

| Input      | n  | Randomized Time (ms) | Deterministic Time (ms) |
|----------------|-------:|-------------------------:|----------------------------:|
| Random         | 1,000  | 0.12                     | 0.34                        |
|                | 10,000 | 0.98                     | 3.07                        |
|                | 50,000 | 4.68                     | 18.25                       |
| Sorted         | 1,000  | 0.17                     | 0.28                        |
|                | 10,000 | 1.26                     | 2.96                        |
|                | 50,000 | 6.14                     | 14.91                       |
| Reverse-sorted | 1,000  | 0.13                     | 0.28                        |
|                | 10,000 | 1.24                     | 2.93                        |
|                | 50,000 | 4.74                     | 14.81                       |
| Repeated       | 1,000  | 0.28                     | 0.14                        |
|                | 10,000 | 0.73                     | 2.35                        |
|                | 50,000 | 24.42                    | 6.44                        |

Both algorithms almost always grew linearly when testing on various datasets. In assignment 5, deterministic quicksort struggled significantly with both sorted and reverse-sorted datasets. But quickselect was not affected by the sorting method, and while deterministic quicksort took almost a minute to sort an already sorted list, quickselect was nearly the same across all datasets except those with repeated values. On the repeated data, randomized quickselect was the slowest of all its runs (24.42 ms) because my Assignment 5 partition places all equal values on one side, whereas the three-way partition made the deterministic version faster (6.44 ms). On the other datasets, randomized quickselect was three to four times faster than median of medians, because median of medians does more work in each round to find its pivot.

## Part 2: Data Structures

For this assignment, I have also implemented the data structures from Chapter 10 of the textbook. First, I implemented the array with O(1) access time for every function except insertion and deletion. Insertion and deletion are different because, to do this, the array needs to shift all the elements to fill the gap left by the removed element or to create space for the inserted one, so insertion and deletion are O(n). The matrix works similarly: it is stored row by row in a single list, so element [i][j] is at index i × columns + j, and access is O(1).

I then used a fixed-size array to build the stack and the queue. In a stack, push and pop are O(1) because only the top index changes. The queue would normally need to shift elements when the first one leaves, but in my circular queue, the head and tail indexes simply wrap around to the start of the list, so enqueue and dequeue are also O(1). In the linked lists, I changed the approach and fixed the insertion time problem in the array because, in linked lists, nothing shifts when elements are added. Instead, a new node is simply linked in front of the head, so inserting at the beginning is O(1).

### Discussion

Both arrays and linked lists are fast and efficient in their own ways. In my opinion, it is the use case that will truly reveal their good and bad sides. An array is the fastest when you need to find something by its position, like opening page 50 of a book, but adding or removing something in the middle is slow because everything after it has to move. A linked list is the opposite: adding something at the front is instant, but finding an item means going through the list one by one. Even though it may seem like elementary data structures are too simple to be used anywhere nowadays, I think they are a really efficient and popular solution in places where simplicity is the goal due to hardware limitations. For example, microcontrollers such as the Arduino are really popular in robotics and simple embedded systems. These devices have very little memory, so fixed-size arrays, stacks, and circular queues are a good fit because they use a known amount of memory and can still hold and move a lot of data quickly.
