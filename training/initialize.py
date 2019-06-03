import pickle
fileobject=open("./pickle/values_storing_2",'wb')
actions=[" ","X","O"]
a=[]
for i in range(100):
  a.append([])
  for j in range(500):
    a[i].append([])
pickle.dump(a,fileobject)
fileobject.close()
fileobject=open("./pickle/values",'wb')
b=[0]*(4*10**4)
for i in range(4*10**4):
  b[i]=[0]*10
pickle.dump(b,fileobject)
fileobject.close()