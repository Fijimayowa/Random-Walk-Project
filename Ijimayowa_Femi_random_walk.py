import random

starting_grid=[[0,0,0,0,0],
               [0,0,0,0,0]]
starting_grid[1][1]=1
starting_grid=[[0 for x in range(15)] for x in range(15)]


i,j=6,6

c=100

while c>0:
    var=random.randint(1,20)
    c-=1
    if var>=1 and var<=5:
        if i-1>0:
            i=i-1
            starting_grid[i][j]+=1
    if var>=6 and var<=10:
        if i+1<=14:
            i+=1
            starting_grid[i][j]+=1
    if var>=11 and var<=15:
        if j-1>0:
            j=j-1
            starting_grid[i][j]+=1
    if var>=16 and var<=20:
        if j+1<=14:
            j+=1
            starting_grid[i][j]+=1
        
for i in range(15):
    print(starting_grid[i])