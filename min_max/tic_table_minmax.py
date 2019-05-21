import pickle
fileobject=open("./values_minmax",'rb')
actions=[" ","X","O"]
a=pickle.load(fileobject)
count=0
numb=0
for i1 in actions:
  for i2 in actions:
     for i3 in actions:
        for i4 in actions:
           for i5 in actions:
              for i6 in actions:
                 for i7 in actions:
                    for i8 in actions:
                       for i9 in actions:
                          if len(a[count])!=0:
                            print(count,a[count])
                            numb+=1
                          count+=1 
fileobject.close()                          
print(len(a),numb,a[127])