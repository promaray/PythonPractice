import numpy as np
import time
k = np.array ([1,2,3,4])
print(k)

a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Vectorized Version 
tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("Vectorized Time:" +  str(1000*(toc-tic)) + "ms")

# Non Vectorized Version
c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()

print(c)
print("Non Vectorized Time:" + str(1000*(toc-tic)) + "ms")