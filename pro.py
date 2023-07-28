import numpy as np

b=np.array([[1,2,3],[6,7,8]])
print(b[1,2])
c=b.reshape(3,2)
print(c)
print(b)
a=np.ones([5,6])
print(a)
#d=np.twos([5,6]) this is wronge only for 0 and 1 
#print(d)
e=np.arange(5)
print(e)
f=np.full((3,5),8)
print(f)


g=np.eye(9)#identity matrix
print(g)
w=np.random.random((4,5))
print(w)
q=np.full((5,5),1)
print(q)
#for u in range(2 , 4):
    #for v in range(2 , 4 ):
p=q[1:3,1:3]
print(p)
q[1:4,1:4]=0
print(q)
q[2:3,2:3]=9
print(q)
g=np.array([[1,2,3,4,5],[6,7,8,9,10]])
t=g[-1,-4:-1]
print(t)
y=g.copy()
y[0,0]=8
print(g)
print(y)
sum=np.add(g,y)#direct addition of marices element wise 
diff=np.subtract(g,y)#element wise subsraction
mul=np.multiply(g,y)#element wise multiplication 
div=np.divide(g,y)#element wise division 
sq=np.sqrt(g)
print(sq)
print(diff)
print(mul) 
print(sum)
print(y.T)#tarnspose of matrix y 
print(np.sum(y))
print(np.sum(y,axis=0))#sum of column wise entries
print(np.sum(y,axis=1))#sum of row wise entries


