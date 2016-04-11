'''
Created on Apr 11, 2016

@author: echglig
'''

#exists
fout=open('oops.txt','wt')
line="This is just a test";
fout.write(line)
fout.close()

#exists()
import os 
print(os.path.exists('oops.txt'))
print(os.path.exists('old.txt'))
print(os.path.exists('.'))
print(os.path.exists('..'))

#idfile() isdir()
name='oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
#folder='C:\Users\echglig\Desktop\Python'
#print(os.path.isdir(folder))

#need to add r 
path=r'C:\Users\echglig\Desktop\Python'
print(os.path.isabs(path))


#copy()
#shutil
import shutil
shutil.copy('oops.txt','old.txt')

#os.rename
#os.rename('oops.txt', 'ohnew.txt')

#os.link('oops.txt','ohps.txt')
print(os.path.isfile('ohps.txt'))
print(os.path.islink('ohps.txt'))
#os.symlink('oops.txt','jeeper.txt')
print(os.path.islink('jeeper.txt'))

#chmod chown 
os.chmod('oops.txt',400)
#uid=5
#gid=20
#chown('opps.txt',uid,gid)

#abspath
print(os.path.abspath('oops.txt'))

#realpath
print(os.path.realpath('oops.txt'))

os.remove('old.txt')

#mkdir()
#os.mkdir('peoms')
#print(os.path.isdir('peoms'))
#os.rmdir('peoms')
#print(os.path.isdir('peoms'))


#if os.path.isdir('peoms'):
#    os.mkdir('peoms') 
    
    
#print(os.listdir(path='./peoms'))
#os.mkdir('peoms/newfolder')

#chdir 
#os.mkdir('peoms')
#os.mkdir('peoms/newfolder')
#os.chdir('peoms')

#glob.glob
import glob 
print(glob.glob('*'))

#getpid() & getcwd
print(os.getpid())
print(os.getcwd())
#print(os.getuid())
#print(os.getgid())

#import subprocess
#ret=subprocess.getoutput('date')
#ret=subprocess.getstatusoutput('date')
#print(ret)

import multiprocessing 
import os 

def do_this(what):
    whoami(what)
    
def whoami(what):
    print("Processing %s says: %s" %(os.getpid(),what))

#if __name__=="__main__":
#    whoami('Iam the main process')
#    for n in range(0,4):
#        p=multiprocessing.process(target=do_this,args=("Iam function %s" % n))
#        p.start

#p.terminate()
















