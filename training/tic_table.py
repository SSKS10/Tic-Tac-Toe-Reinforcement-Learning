import pickle
fileobject=open("./pickle/values",'rb')
a=pickle.load(fileobject)
fileobject.close()
count=0   
for i in range(3*10**4):
	for j in range(10):
		if type(a[i][j])!=int:
			print(i,a[i])
			count+=1  
			break	
print(count)                   