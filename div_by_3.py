import numpy as np
x=np.arange(1,101).reshape(10,10)
y=np.square(x)
print("Y=")
print (y)
z=y[y%3==0]
print ("Numbers divisible by 3")
print(z)
