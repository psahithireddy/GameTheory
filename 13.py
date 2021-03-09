import numpy as np
#import sys, os
#import math
import copy
import itertools

def check(array,target,forstrat,util_matrix):
    #get values from allpermut, check for comparison in target, if this val itself is max return 1 ,else return 0
    tf=0
    getindex=[]
    for i in range(len(array)):
        getindex.append(allpermut[array[i]])
    #print(getindex)
    for i in range(len(getindex)):
        #print(tuple(getindex[i]),util_matrix[tuple(getindex[i])][target],"hi",i)
        if util_matrix[tuple(getindex[i])][target]<=util_matrix[tuple(forstrat)][target]:
            tf+=1
    if tf==len(array):        
        return 1
    else:
        return 0



def psnegen(allpermut,util_matrix):
    global psnelist
    psnelist=[]   
    final=allpermut.copy()
    for i in range(len(allpermut)):#take each state 
        flag=0
        for j in range(len(allpermut[i])): #which is same as player_count
            #for each j , check the whole array and get what are similar other than 
            comparisonarray=[]
            for l in range(len(allpermut)):
                matchflag=0
                for k in range(len(allpermut[i])):
                    if(allpermut[l][k]==allpermut[i][k]): #for all others match them
                        matchflag+=1
                    elif j==k and l!=i:#hardupdate current one
                        matchflag+=1
                if matchflag==player_count:
                    comparisonarray.append(l)
            #print(comparisonarray,j)
            #call check and check if thats true
            flag+=check(comparisonarray,j,allpermut[i],util_matrix)                        
        if(flag==player_count):#max for all players
           psnelist.append(allpermut[i])    
    #print(psnelist)        
                  

def weakly_dominated_strategies(allpermut,util_matrix):
    global finalarray
    finalarray=[[]for i in range(player_count)] #which(just number) and how many
    for i in range(player_count):
        comparray=[[]for j in range(strategy[i])]
        for j in range(strategy[i]):
            indexes=[]
            for k in range(len(allpermut)):
                if allpermut[k][i]==j:
                    indexes.append(allpermut[k])
            for l in range(len(indexes)):              
                comparray[j].append(util_matrix[tuple(indexes[l])][i])
        #print(comparray,i)
        for m in range(len(comparray)): #for an array , check if thats greater or equals than others
            howmany=0
            for n in range(len(comparray)):
                forall=0
                for o in range(len(comparray[m])):
                    if comparray[m][o]>=comparray[n][o]:
                        forall+=1
                if forall==len(comparray[m]):        
                    howmany+=1
            if howmany==len(comparray):
                finalarray[i].append(m)
    



#please verify input length

# try:
player_count = int(input())

strategy = list(map(int,input().strip().split()))[:player_count]
    
new = np.prod(strategy)*player_count
util_list =  list(map(int,input().strip().split()))[:new]
# tup_list = [(util_list[i], util_list[i+1]) for i in range(0, len(util_list), 2)]
#print(len(util_list))
tup_list = []
for i in range(0, len(util_list), player_count):
    temp_list =  []
    for j in range(player_count):
        temp_list.append(util_list[i+j])

    tup_list.append(tuple(temp_list))
    
#print(tup_list)
temp_str = "float"
temp_str2 = ",float"*(player_count-1)
string = temp_str+temp_str2

dt = np.dtype(string)
data = np.array(tup_list, dtype=dt)
#print(data)
tup = tuple(x for x in strategy)
util_matrix = data.reshape(tup[::-1])
util_matrix = np.transpose(util_matrix)
#print(util_matrix)

#print(util_matrix.ndim)
#test=(0,0,0)
#print(util_matrix[0,0,0][0],"test")
#psne(util_matrix, player_count)
#psnegen(util_matrix,player_count)
# except:
#     print("Error in input")
#print(strategy)

 

#func(player_count-1)
somelists=[]
temp=[[]  for i in range(player_count)] 
for k in range(player_count):
    temp[k]=[i for i in range(strategy[k])]
    somelists.append(temp[k])

allpermut=list(itertools.product(*somelists))#generates all the possible states
for i in range(len(allpermut)):
    allpermut[i]=list(allpermut[i])

dummypermut=allpermut.copy()
#print(allpermut)    
psnegen(dummypermut,util_matrix)
#print(allpermut)permut
dummy2permut=allpermut.copy()
weakly_dominated_strategies(dummy2permut,util_matrix)
#check([0,2],0,0,util_matrix)

print(len(psnelist))
#just printing BT F
for i in range(len(psnelist)):
    tempro=psnelist[i]
    for j in range(len(tempro)):
        tempro[j]+=1
    ok=str(tempro)    
    tempro1=ok.strip("[]")
    print(tempro1.replace(",",""))

#print(util_matrix)

#printing dominant
for i in range(player_count):
    tfa=finalarray[i]
    for j in range(len(tfa)):
        tfa[j]+=1
    tfc=str(tfa)
    tfb=tfc.strip("[]")
    print(len(finalarray[i]),tfb.replace(",",""))

'''
print(util_matrix[0,0,1],"001")
print(util_matrix[0,1,0],"010")
print(util_matrix[0,1,1],"011")
'''