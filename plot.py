
import math
import os
from turtle import width
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


if __name__ == "__main__":
    
    injection_runtime = {}
    
    merge_runtime = {}
    
    adaptive_runtime = {}
        
    path = os.getcwd()
    data_files = sorted([fname for fname in os.listdir(path) if fname.endswith('.csv')])
    
    
    
    adaptive_runtime['A'] = np.array(pd.read_csv(data_files[0],header=None))
    adaptive_runtime['B'] = np.array(pd.read_csv(data_files[1],header=None))
    adaptive_runtime['C'] = np.array(pd.read_csv(data_files[2],header=None))
    
    injection_runtime['A'] = np.array(pd.read_csv(data_files[3],header=None))
    injection_runtime['B'] = np.array(pd.read_csv(data_files[4],header=None))
    injection_runtime['C'] = np.array(pd.read_csv(data_files[5],header=None))
    
    merge_runtime['A'] = np.array(pd.read_csv(data_files[6],header=None))
    merge_runtime['B'] = np.array(pd.read_csv(data_files[7],header=None))
    merge_runtime['C'] = np.array(pd.read_csv(data_files[8],header=None))
    
    
    X_Axis = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]
    
    # X_Axis = [math.log(x) for x in X_Axis]
    
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