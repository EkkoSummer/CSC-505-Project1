from copy import deepcopy
from email import header
from datetime import datetime
from posixpath import sep
import time
from tokenize import Ignore
from warnings import catch_warnings
import pandas as pd
import os
from torch import cat
import matplotlib.pyplot as plt
import gzip
import numpy as np


###############
#Insertion Sort
###############
def insertion_sort1(l):
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

#insert sort 2: move the elements while searching
def insertion_sort(l):
    for c in range(1, len(l)):
        cur = c
        insertNum = l[c]

        while insertNum < l[cur-1] and cur > 0:
            l[cur] = l[cur-1]
            cur -= 1
        l[cur] = insertNum
    return l


###############
  #mergeSort
###############
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

###############
    #timSort
###############


#step1: function to get the run
MIN = 64
def minRun(n):
    r = 0
    while n > MIN:
        r |= (n&1)
        n >>= 1

    return r+n


def tim_sort1(l, run):
    n = len(l)
    #print(listLen)
    # run = minRun(n)

    # if len of the list is shorter than 64, then we can directly use insertSort, cuz now insertSort is stable.
    if n < run:
        return insertion_sort1(l)

    #sort each run(interval)
    for start in range(0, n, run):
        end = min(start+run-1, n-1)
        l[start:end+1] = insertion_sort1(l[start:end+1])

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




def tim_sort(l):
    l.sort()
    return l



if __name__ == "__main__":
    
    
    current_path = os.getcwd()
    
    insertion_runtime = {}
    
    merge_runtime = {}
    
    tim_runtime = {}
    
    insertion_runtime['A'] = []
    insertion_runtime['B'] = []
    insertion_runtime['C'] = []
    
    merge_runtime['A'] = []
    merge_runtime['B'] = []
    merge_runtime['C'] = []
    
    tim_runtime['A'] = []
    tim_runtime['B'] = []
    tim_runtime['C'] = []
    
    X_Axis = []

    
    root_folders = os.listdir(current_path)
    # iterate root_folders, the 'folder' is goind to be 'A', 'B' and 'C' sequesntially
    
    temp_dir = sorted([fname for fname in os.listdir(current_path+'\\A') if fname.endswith('.log.gz')], key=lambda f: int(f.rsplit('.', -1)[0].rsplit(None,1)[-1]))
    
    for temp_file_name in temp_dir:
                
        X_Axis.append(int(temp_file_name.rsplit('.', -1)[0].rsplit(None,1)[-1]))
    
    for folder in root_folders:
        if os.path.isdir(folder) and folder != 'temp':
            
            
            data_path = current_path+'\\'+folder
            
            data_files = sorted([fname for fname in os.listdir(data_path) if fname.endswith('.log.gz')], key=lambda f: int(f.rsplit('.', -1)[0].rsplit(None,1)[-1]))
            
            
            
            for file_name in data_files:
                
                with gzip.open(data_path+'\\'+file_name, mode = 'rt', encoding='ISO-8859-1') as f:
                    
                    raw_datas = f.readlines()
                    
                    input_data = []
                    
                    for data in raw_datas:
                        if len(data) >=25:
                            try:
                                input_data.append( datetime.strptime(data[0:25], '%Y-%m-%dT%H:%M:%S%z'))
                            except:
                                continue
                    
                    data_copy = deepcopy(input_data)

                    time_I = 0
                    for i in range(0,7):
                        t_inj_start = time.time()
                        insertion_sort(data_copy)
                        t_inj_end = time.time()
                        if(i>=2):
                            time_I += t_inj_end-t_inj_start
                        #reset the input_data to its original order
                        data_copy = deepcopy(input_data)
                    
                    #store the runtime to corresponding array for plotting
                    insertion_runtime[folder].append(time_I/5)
                    
                    time_M = 0
                    for i in range(0,7):
                        t_mer_start = time.time()
                        merge_sort(data_copy)
                        t_mer_end = time.time()
                        if(i>=2):
                            time_M += t_mer_end-t_mer_start
                        #reset the input_data to its original order
                        data_copy = deepcopy(input_data)
                    
                    #store the runtime to corresponding array for plotting
                    merge_runtime[folder].append(time_M/5)
                    

                    time_T = 0
                    for i in range(0,7):
                        t_ada_start = time.time()
                        tim_sort(data_copy)
                        t_ada_end = time.time()
                        if(i>=2):
                            time_T += t_ada_end-t_ada_start
                        #reset the input_data to its original order
                        data_copy = deepcopy(input_data)
                    
                    #store the runtime to corresponding array for plotting
                    tim_runtime[folder].append(time_T/5)
                    
    
    
    # print(X_Axis)
    
    for key in insertion_runtime:
        arr = np.asarray(insertion_runtime[key])
        np.savetxt("insertion_runtime"+"_"+key+".csv",arr)
    
    for key in merge_runtime:
        arr = np.asarray(merge_runtime[key])
        np.savetxt("merge_runtime"+"_"+key+".csv",arr)
        
    for key in tim_runtime:
        arr = np.asarray(tim_runtime[key])
        np.savetxt("tim_runtime"+"_"+key+".csv",arr)
    
    # Plotting the comparing of runtime
    
    # Runtime of insertion sort with regard to Dataset A,B,C respectively
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, insertion_runtime['A'], X_Axis, insertion_runtime['B'], X_Axis, insertion_runtime['C'], lw=2)
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['A','B','C'])
    plt.title("Comparison of insertion Sort of Different Dataset")
    plt.savefig("1.png")
    plt.close()
    # plt.show()
    
    # Runtime of merge sort with regard to Dataset A,B,C respectively
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, merge_runtime['A'], X_Axis, merge_runtime['B'], X_Axis, merge_runtime['C'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['A','B','C'])
    plt.title("Comparison of Merge Sort of Different Dataset")
    plt.savefig("2.png")
    plt.close()
    # plt.show()
    
    # Runtime of tim sort with regard to Dataset A,B,C respectively
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, tim_runtime['A'], X_Axis, tim_runtime['B'], X_Axis, tim_runtime['C'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['A','B','C'])
    plt.title("Comparison of tim Sort of Different Dataset")
    plt.savefig("3.png")
    plt.close()
    # plt.show()
    
    
    # Comparison of Dataset A Runtime of Different Sorting Algorithm
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, insertion_runtime['A'], X_Axis, merge_runtime['A'], X_Axis, tim_runtime['A'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['insertion Sort','Merge Sort','tim Sort'])
    plt.title("Comparison of Dataset A Runtime of Different Sorting Algorithm")
    plt.savefig("4.png")
    plt.close()
    # plt.show()
    
    # Comparison of Dataset B Runtime of Different Sorting Algorithm
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, insertion_runtime['B'], X_Axis, merge_runtime['B'], X_Axis, tim_runtime['B'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['insertion Sort','Merge Sort','tim Sort'])
    plt.title("Comparison of Dataset B Runtime of Different Sorting Algorithm")
    plt.savefig("5.png")
    plt.close()
    # plt.show()
    
    # Comparison of Dataset C Runtime of Different Sorting Algorithm
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, insertion_runtime['C'], X_Axis, merge_runtime['C'], X_Axis, tim_runtime['C'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['insertion Sort','Merge Sort','tim Sort'])
    plt.title("Comparison of Dataset C Runtime of Different Sorting Algorithm")
    plt.savefig("6.png")
    plt.close()
    # plt.show()