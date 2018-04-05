import numpy as np
x = [1,6,3,4,8,9,4,2,5,7,60,10]
y = [i for i in x if np.mod(i,2)==0]
print y
