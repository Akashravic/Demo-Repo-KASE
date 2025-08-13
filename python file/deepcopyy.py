import copy as c
L3=[10,[1,2,3],30]
L4=c.deepcopy(L3)
L3[0]=100
print("L3=",L3)
print("L4=",L4)
L3[1][0]=100
print("L3=",L3)
print("L4=",L4)