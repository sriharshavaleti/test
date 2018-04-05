import numpy as np
x = [1,6,3,4,8,9,4,2,5,7,60,10]
y = [i for i in x if np.mod(i,2)==0] or [i for i in x if i%2==0] # we can use both the methods
print y
