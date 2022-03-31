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


    
def injection_sort(input_data):
    #need implemention
    
    return

def merge_sort(input_data):
    #need implemention
    
    return

def adaptive_sort(input_data):
    #need implemention
    
    return



if __name__ == "__main__":
    
    
    current_path = os.getcwd()
    
    injection_runtime = {}
    
    merge_runtime = {}
    
    adaptive_runtime = {}
    
    injection_runtime['A'] = []
    injection_runtime['B'] = []
    injection_runtime['C'] = []
    
    merge_runtime['A'] = []
    merge_runtime['B'] = []
    merge_runtime['C'] = []
    
    adaptive_runtime['A'] = []
    adaptive_runtime['B'] = []
    adaptive_runtime['C'] = []
    
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
                    
                    buffer = deepcopy(input_data)
                    
                    t_inj_start = time.time()
                    # injection_sort(input_data)
                    np.sort(input_data,kind="quicksort")
                    t_inj_end = time.time()
                    
                    #reset the input_data to its original order
                    input_data = deepcopy(buffer)
                    
                    #store the runtime to corresponding array for plotting
                    injection_runtime[folder].append(t_inj_end-t_inj_start)
                    
                    
                    t_mer_start = time.time()
                    # merge_sort(input_data)
                    np.sort(input_data,kind="mergesort")
                    t_mer_end = time.time()
                    
                    #reset the input_data to its original order
                    input_data = deepcopy(buffer)
                    
                    #store the runtime to corresponding array for plotting
                    merge_runtime[folder].append(t_mer_end-t_mer_start)
                    
                    t_ada_start = time.time()
                    np.sort(input_data,kind="heapsort")
                    # adaptive_sort(input_data)
                    t_ada_end = time.time()
                    
                    #store the runtime to corresponding array for plotting
                    adaptive_runtime[folder].append(t_ada_end-t_ada_start)
                    
    
    
    print(X_Axis)
    
    for key in injection_runtime:
        arr = np.asarray(injection_runtime[key])
        np.savetxt("injection_runtime"+"_"+key+".csv",arr)
    
    for key in merge_runtime:
        arr = np.asarray(merge_runtime[key])
        np.savetxt("merge_runtime"+"_"+key+".csv",arr)
        
    for key in adaptive_runtime:
        arr = np.asarray(adaptive_runtime[key])
        np.savetxt("adaptive_runtime"+"_"+key+".csv",arr)
    
    # Plotting the comparing of runtime
    
    # Runtime of injection sort with regard to Dataset A,B,C respectively
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, injection_runtime['A'], X_Axis, injection_runtime['B'], X_Axis, injection_runtime['C'], lw=2)
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['A','B','C'])
    plt.title("Comparison of Injection Sort of Different Dataset")
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
    
    # Runtime of adaptive sort with regard to Dataset A,B,C respectively
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, adaptive_runtime['A'], X_Axis, adaptive_runtime['B'], X_Axis, adaptive_runtime['C'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['A','B','C'])
    plt.title("Comparison of Adaptive Sort of Different Dataset")
    plt.savefig("3.png")
    plt.close()
    # plt.show()
    
    
    # Comparison of Dataset A Runtime of Different Sorting Algorithm
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, injection_runtime['A'], X_Axis, merge_runtime['A'], X_Axis, adaptive_runtime['A'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['Injection Sort','Merge Sort','Adaptive Sort'])
    plt.title("Comparison of Dataset A Runtime of Different Sorting Algorithm")
    plt.savefig("4.png")
    plt.close()
    # plt.show()
    
    # Comparison of Dataset B Runtime of Different Sorting Algorithm
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, injection_runtime['B'], X_Axis, merge_runtime['B'], X_Axis, adaptive_runtime['B'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['Injection Sort','Merge Sort','Adaptive Sort'])
    plt.title("Comparison of Dataset B Runtime of Different Sorting Algorithm")
    plt.savefig("5.png")
    plt.close()
    # plt.show()
    
    # Comparison of Dataset C Runtime of Different Sorting Algorithm
    plt.figure(figsize=(30,10))
    plt.plot(X_Axis, injection_runtime['C'], X_Axis, merge_runtime['C'], X_Axis, adaptive_runtime['C'])
    plt.xticks(X_Axis,X_Axis)
    plt.xlabel("Data Size(n)")
    plt.ylabel("Runtime(sec)")
    plt.legend(['Injection Sort','Merge Sort','Adaptive Sort'])
    plt.title("Comparison of Dataset C Runtime of Different Sorting Algorithm")
    plt.savefig("6.png")
    plt.close()
    # plt.show()