#!/usr/bin/python

#folder manipulate

import os

path='/home/itk/echglig'
if not os.path.exists(path+'/newdir'):
	print('There is no dir newdir , i will create it ')
	os.mkdir('path/newdir')
#if os.path.isdir('/home/itk/echglig/newdir'):
#	print('There is a dir ,ok')
	#os.rmdir('/home/itk/echglig/newdir')


#path='/home/itk/echglig/newdir'
peom='''When you are young 
you can do anything
just go ahead
'''
if not os.path.exists(path+'/newdir'):
	os.mkdir(path)
os.chdir(path+'/newdir')
fout=open('peom','wt')
fout.write(peom)
fout.close()

files=os.listdir(path+'/newdir')
print(files)
for file in files:
	print(file)


import glob
os.chdir(path+'/newdir') 
newfiles=glob.glob('*')
print(newfiles)

print('The files are :')
for file in newfiles:
	print(file)















