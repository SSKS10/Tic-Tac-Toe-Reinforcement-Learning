import pickle
values=[]
for i in range(10**6):
  values.append([])
fileobject=open("./values_minmax",'wb')   
pickle.dump(values,fileobject)
fileobject.close()