#np.arange(start, stop, step)
#np.linspace(start, stop, num)
	
import numpy as np
 
a = range(0, 5, 1)
print(a)
 
# a = range(0, 10, 0.1)
 
b = np.arange(0, 5, 0.1)
print(b)
 
d = np.linspace(0, 5, 10)
print(d)

#Срезы Slice
a = [4, 16, 10, 5, 7, 1, 8]
# slice = a[start, stop, step]
slice = a[2:5:1]
print(slice)

import numpy as np
 
a = [1, 5, 3, 6]
slice = a[0:2:1]
print(slice)
 
slice = a[3:0:-1]
print(slice)

 #Переворачивает список
slice = a[::-1]
print(slice)


b = np.array([a, np.array(a)*3])
print(b)

slice = b[::, 1]
print(slice)

slice = b[1,2:3:1]
print(slice)

slice = b[1,2::1]
print(slice)