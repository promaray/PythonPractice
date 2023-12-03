# sigmoid of vectors

import numpy as np

def sigmoid(x):

    import numpy as np
    s = 1 / (1 + np.exp(-x))
    return s

t_x = np.array([1, 2, 3])
s = sigmoid(t_x)
ds = np.multiply(s, (1-s))

#sigmoid of vector    s = 1 / (1 + np.exp(-x))
print("sigmoid(t_x) = " + str(sigmoid(t_x)))

# sigmoid gradient used for back propagation
# 𝑠𝑖𝑔𝑚𝑜𝑖𝑑_𝑑𝑒𝑟𝑖𝑣𝑎𝑡𝑖𝑣𝑒(𝑥)=𝜎′(𝑥)=𝜎(𝑥)(1−𝜎(𝑥))
print ("sigmoid_derivative(t_x) = " + str(ds))

 