import numpy as np
x = np.array([1,2,2,2,3], np.int32)
print ("Input Array Vales") #input values
print(x)
print ("Most frequent values in array")
print(np.bincount(x).argMax(1)) # 2 appears most frequent
