import pickle
fp=open("picklefile.txt","wb")
cricket=["virat","dhoni"]
pickle.dump(cricket,fp)
fp.close()