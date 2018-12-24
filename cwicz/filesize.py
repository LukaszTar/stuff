import os, glob
allsizes = []
files = os.listdir(os.getcwd())
for fil in files:
	size = os.path.getsize(os.getcwd()+os.sep+fil)
	allsizes.append((size, fil))
allsizes.sort()
print(allsizes[-1])
