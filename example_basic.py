# from https://pythonexamples.org/run.php?pgm=import+numpy+as+np%0A%0Aa+%3D+3+%0Ab+%3D+4%0Aoutput+%3D+np.dot%28a%2Cb%29%0Aprint%28output%29

'''
This file services as an example of liner operation

'''

import numpy as np
import torch

a = 3 
b = 4

#nncp np dot
output = np.dot(a,b)

c = 7

output1=np.dot(b,c)

#nncp array

val1=np.array([[1, 2], [3, 4]])

#nncp torch nn interpolate
val2=torch.nn.interpolate()

print(output)