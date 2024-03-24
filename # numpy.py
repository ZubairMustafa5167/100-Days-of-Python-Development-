# numpy 
import numpy as np 

# how to create  Array 
ar1=np.array(range(1,11,1))
print("range",ar1)
#  array creating in equal distance 
ar22=np.linspace(1,100,5)
print("linespace",ar22)
# array in equal distance in log 
ar33=np.logspace(1,4,5)
print("logspace",ar33)
#  how to split array
# split in equal arrays 
spt1=np.split(ar1,2)
print("split in equal arrays",spt1)
# split by itself
spt=np.array_split(ar1,3)
print("split by itself",spt)
# marging of arrays
# concatenation  axis=0 by colum and axis=1 by row , it marge in one array
aa=np.array([[1,2,3,4],[3,4,5,6]])
bb=np.array([[5,6,7,8],[9,9,9,9]])
cc=np.concatenate((aa,bb),axis=1)
print("concatenation in row",cc)
ff=np.concatenate((aa,bb),axis=0)
print("concatenation in colum",ff)
#  stack  axis=0 by colum and axis=1 by row, it marge by [ ] array 
dd=np.stack((aa,bb),axis=1)
print("stackin in row",dd)
ee=np.stack((aa,bb),axis=0)
print("stackin in colum",ee)
 