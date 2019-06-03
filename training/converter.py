import numpy, scipy.io
import pickle, sys
f=open("./pickle/values_storing_2", "rb" )
a=pickle.load(f)
f.close()
scipy.io.savemat('convert', mdict={'pickle_data': a[:]})