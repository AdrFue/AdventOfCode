import os
dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

history=open(dir + file_name[1]).readlines()

from math import comb
def Lagrange1(nums):
    n=len(nums)
    res=0
    for i,x in enumerate(nums):
        res+=x*comb(n,i)*(-1)**(n-1-i)
    return res

def Lagrange2(nums):
    n=len(nums)
    res=0
    for i,x in enumerate(nums):
        res+=x*comb(n,i+1)*(-1)**(i)
    return res

res1,res2=0,0
for line in history:
    nums=list(map(int,line.strip().split()))
    res1+=Lagrange1(nums)
    res2+=Lagrange2(nums)
print(res2)