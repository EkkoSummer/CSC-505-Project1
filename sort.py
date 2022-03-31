import random
a = [1,3,2,8,5,3,1]

#insert sort 1: move the elements after searching: find the position, then move backward, then insert
#S1: find the insert position(the element which is lower than the cur element)
#S2: the elements from the position to the cur element, all of them move backward
#S3: insert

def insertSort1(l):
    for c in range(1, len(l)):
        cur1, cur2 = c, c
        insertNum = l[c]    #insertNum is the ele to insert
        #find the position to insert, the position is cur1
        while insertNum < l[cur1-1] and cur1 > 0:   #termination conditions: find the lower ele or move to the start
            cur1 -= 1
        #the elements from the insert position to the original position move backward
        while cur2 > cur1:
            l[cur2] = l[cur2-1]
            cur2 -= 1
        #insert the element
        l[cur1] = insertNum
    return l

# print(insertSort1(a))

#insert sort 2: move the elements while searching
def insertSort2(l):
    for c in range(1, len(l)):
        cur = c
        insertNum = l[c]

        while insertNum < l[cur-1] and cur > 0:
            l[cur] = l[cur-1]
            cur -= 1
        l[cur] = insertNum
    return l
#
# print(insertSort2(a))

#mergeSort
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c

def merge_sort(l):
    if len(l) <= 1:
        return l
    middle = len(l) // 2
    left = merge_sort(l[:middle])
    right = merge_sort(l[middle:])
    return merge(left, right)


# print(MS([5,4,6,3,9]))

# timSort

#step1: function to get the run
MIN = 64
def minRun(n):
    r = 0
    while n > MIN:
        r |= (n&1)
        n >>= 1

    return r+n

# print(minRun(300))

#get the run. the parameter l is the list to be tested
run = minRun(len(l))


def timSort1(l, run):
    n = len(l)
    #print(listLen)
    # run = minRun(n)

    # if len of the list is shorter than 64, then we can directly use insertSort, cuz now insertSort is stable.
    if n < run:
        return insertSort1(l)

    #sort each run(interval)
    for start in range(0, n, run):
        end = min(start+run-1, n-1)
        l[start:end+1] = insertSort1(l[start:end+1])

    #merge by size, the size is increasing by *2(two list -> one list)
    size = run
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(left+size-1, n-1)
            right = min(left+ 2*size -1, n-1)

            if mid < right:
               l[left: right+1] = merge(l[left:mid+1], l[mid:right+1])

        size *= 2

    for i in range(len(l)):
        if l[i] > l[i+1]:
            pos = i
            break




    return merge(l[:pos+1], l[pos+1:])




# q = []
# for i in range(100):
#     q.append(random.randint(0,500))
# print(timSort1(q, run))

#The built-in sort function of python is just timSort
def timSort2(l):
    l.sort()
    return l

# q = []
# for i in range(100):
#     q.append(random.randint(0,500))
# print(timSort2(q))