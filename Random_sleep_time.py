import random
import time
from time import sleep
def random():
    for x in range(10):
         x= random.randint(1,101)
start_time=time.time()
numbers = random()
print (numbers)
sleep (0.5)
end_time = time.time()
diff = start_time-end_time
total_excution_time = diff - 0.5
print (total_excution_time)
