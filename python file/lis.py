L=[1,2,3]
L2=L
#L2=L.copy()  used for creating duplicate of a list.
L2[0]=10
L[-1]=30
print("L2=",L2)
print("L=",L)
print (id(L))
