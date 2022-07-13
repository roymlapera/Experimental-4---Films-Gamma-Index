##Create the following array (1 line)

#Use the array object to get the number of elements, rows and columns
#
#Get the mean of the rows and columns
#
#What do you get when you do this?
#
#>>> a[4,:]
#[extra] If you have time you can get familiar try
#np.log(a)
#np.cumsum(a)
#np.rank(a)
#np.power(a,2)
#[extra] How do you create a vector that has exactly 50 points and spans the range 11 to 23


import numpy as np

a = np.arange(1,101).reshape(10,10)

print a

print np.power(a,2)

x = np.linspace(11,23,50)

print x

b = np.arange(1,4)
c = np.arange(4,7)

print b,c
print np.hstack([b,c])
print np.vstack([b,c])