import numpy as np
from scipy.optimize import linprog
import time
import re
#c = [3,6,5,4,9,2,3,6,2]
#a = [58,60,40]
#b = [30,50,20]

def open_file_and_read(name_of_file):
    with open(name_of_file,'r') as f:
        nums = f.read().splitlines()
    return nums

def create_main_lists():
    main_list = open_file_and_read('numbers.txt')
    c = (main_list[0])
    c = [x for x in c if x != ' ']
    c = list(map(int,c))
    a = (main_list[1])
    a = list(map(int,re.findall(r'(\w+)', a)))
    b = (main_list[2])
    b = list(map(int,re.findall(r'(\w+)', b)))
    return c,a,b

c,a,b = create_main_lists()
start=time.time()

A_1=[[1,1,1,0,0,0,0,0,0],
     [0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,1,1,1]]
b_1=a
A_2=[[1,0,0,1,0,0,1,0,0],
     [0,1,0,0,1,0,0,1,0],
     [0,0,1,0,0,1,0,0,1]]
b_2=b

res=linprog(c,A_1,b_1,A_2,b_2)
P=np.dot(res.x,c)
P1=np.dot(c,res.x)
stop=time.time()

print("Time:", stop-start)
print(res)
print("Check of sum",int(P),int(P1))
print(open_file_and_read('numbers.txt'))