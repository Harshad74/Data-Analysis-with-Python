import sys
import numpy as np
import time

np.array([1,2,3,4])
print(np.array([1,2,3,4]))

a=np.array([1,2,3,4])
b=np.array([0,0.5,1,1.5,2])

print(type(a))
print(a[0:])
print(a[1:3])
print(a[::2])
print(b[[0,2,-1]])

print(a,a.dtype)
m=np.array([1,2,3,4],dtype=np.float64)
print(m)

c=np.array(['a','b','c'])
print(c.dtype)

d=np.array([{'a':1},sys])
print(d.dtype)

A=np.array([[1,2,3],[4,5,6]])
print(A)
print(A.shape)
print(A.ndim)
print(A.size)

c=np.array([
    [
        [12,11,10],
        [9,8,7],
    ],
    [  
        [6,5,4]
    ]
])

print(c.dtype)
print(c.shape)
print(c.size)
print(c[0])
print(type(c[0]))

A = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]  
])

print(A[1,0])
print(A[:2,2:])

A[1]=np.array([10,10,10])
A[2]=99

print(A)

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(type(A))
print(A.sum())
print(A.mean())
print(A.std())
print(A.sum(axis=0))
print(A.sum(axis=1))

a=np.arange(4)
print(a)
print(a*10)
print(a)
a+=100
print(a)

e=np.arange(4)
print(e[[0,-1]])
print(e[[True,False,False,True]])
print(a>=2)
print(a[a>=2])

k=np.random.randint(100,size=(3,3))
print(k>30)
print(k[k>30])

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [6, 5],
    [4, 3],
    [2, 1]
])

print(A.dot(B))
print(A@B)
print(B.T)
print(B.T@A)

print(sys.getsizeof(1))
print(np.dtype(int).itemsize)
print(np.dtype(np.int8).itemsize)
print(np.array([1]).nbytes)

l=list(range(20))
n=np.arange(20)

t=time.time()
m=np.sum(n**2)
t1=time.time()

print(t1-t,m)

t=time.time()
s=sum([x**2 for x in l])
t1=time.time()

print(t1-t,s)

print(np.random.normal(size=2))
print(np.random.rand(2, 4))

print(np.arange(0, 1, .1))
print(np.arange(10).reshape(2, 5))

print(np.linspace(0, 1, 5))
print(np.linspace(0, 1, 20,False))

print(np.zeros((3, 3), dtype=np.int))
print(np.identity(3))
print(np.eye(8, 4, k=1))
print("Hello World"[7])


print(np.nan)
print(3+np.nan)
a=np.array([1,2,3,np.nan,np.nan])
print(a.mean())
print(np.inf)
b=np.array([1,2,3,np.nan,np.inf])
print(b.mean())

print(np.isnan(a))
print(a[~np.isnan(a)])
print(a[np.isfinite(a)])