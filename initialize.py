import pickle
fileobject=open("./values",'wb')
actions=[" ","X","O"]
a=[0]*10**6
for i in range(10**6):
  a[i]=[0]*10
pickle.dump(a,fileobject)
fileobject.close()
