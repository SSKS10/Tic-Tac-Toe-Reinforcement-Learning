import pickle
fileobject=open("./values",'wb')
actions=[" ","X","O"]
a=[0]*10**6
for i in range(10**6):
  a[i]=[0]*10
  """
count=0;
for i1 in actions:
  for i2 in actions:
     for i3 in actions:
        for i4 in actions:
           for i5 in actions:
              for i6 in actions:
                 for i7 in actions:
                    for i8 in actions:
                       for i9 in actions:
                          #print(i1+i2+i3+i4+i5+i6+i7+i8+i9)
                          for j in range(0,10): 
                             a[count][j]=0
                          count+=1
                          """ 
pickle.dump(a,fileobject)
fileobject.close()