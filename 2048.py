import os, random
from getkey import getkey, keys
from random import shuffle


def getch():
    key = getkey()
    if key == keys.UP or key == 'w':
        return 'up'
    elif key == keys.DOWN or key == 's':
        return 'down'
    elif key == keys.RIGHT or key == 'd':
        return 'right'
    elif key == keys.LEFT or key == 'a':
        return 'left'
    elif key == 'x' or key == 'X': return '1'
    else:
        return 'error'

def i2s(a):
    if a == 0: return ''
    else: return a

def drawScreen():
    os.system('cls' if os.name == 'nt' else 'clear')    
    st = mapa.copy()
    for i in range(3):
        print('|\t\t|\t\t|\t\t|')
        print('|\t'+
        str(i2s(st[i][0])) +'\t|\t'+
        str(i2s(st[i][1])) +'\t|\t'+
        str(i2s(st[i][2])) +'\t|')
        print('|\t\t|\t\t|\t\t|\n')

# pot^11 GAME

chanceInitial = 0.7
chanceGame = 0.7
pot = 2

# Generating a random numeric map
lose = False
mapa = []
mapch = []
for i in range(3):
    mapch.append([random.random(),random.random(),random.random()])
    mapa.append([pow(pot,random.randint(1, 2)), 
                pow(pot,random.randint(1, 2)), 
                pow(pot,random.randint(1, 2))])
    for j in range(3):
        if mapch[i][j]<chanceInitial: mapa[i][j] = 0
shuffle(mapa)
for i, sublist in enumerate(mapa): 
    shuffle(mapa[i])

# loop game
score = 0
flag = True
drawScreen()
while True:
    k = getch()
    for i in range(3):
        if k=='up':
            while(mapa[0][i]==0 and mapa[1][i]+mapa[2][i]!=0):
                mapa[0][i]=mapa[1][i]
                mapa[1][i]=mapa[2][i]
                mapa[2][i]=0
            while(mapa[1][i]==0 and mapa[2][i]!=0):
                mapa[1][i]=mapa[2][i]
                mapa[2][i] = 0
            if(mapa[0][i]==mapa[1][i]):
                mapa[0][i]+=mapa[1][i]
                score+=mapa[0][i]
                mapa[1][i] = mapa[2][i]
                mapa[2][i] = 0
            elif(mapa[1][i]==mapa[2][i]):
                mapa[1][i]+=mapa[2][i]
                score+=mapa[1][i]
                mapa[2][i] = 0
        if k=='down':
            while(mapa[2][i]==0 and mapa[0][i]+mapa[1][i]!=0):
                mapa[2][i] = mapa[1][i]
                mapa[1][i] = mapa[0][i]
                mapa[0][i] = 0
            while(mapa[1][i]==0 and mapa[0][i]!=0):
                mapa[1][i] = mapa[0][i]
                mapa[0][i] = 0
            if(mapa[2][i] == mapa[1][i]):
                mapa[2][i]+=mapa[1][i]
                score+=mapa[2][i]
                mapa[1][i] = mapa[0][i]
                mapa[0][i] = 0
            elif(mapa[1][i] == mapa[0][i]):
                mapa[1][i] += mapa[0][i]
                score+=mapa[1][i]
                mapa[0][i] = 0
        if k=='right':
            while(mapa[i][2]==0 and mapa[i][1]+mapa[i][0]!=0):
                mapa[i][2] = mapa[i][1]
                mapa[i][1] = mapa[i][0]
                mapa[i][0] = 0
            while(mapa[i][1]==0 and mapa[i][0]!=0):
                mapa[i][1] = mapa[i][0]
                mapa[i][0] = 0
            if(mapa[i][2] == mapa[i][1]):
                mapa[i][2]+=mapa[i][1]
                score+=mapa[i][2]
                mapa[i][1] = mapa[i][0]
                mapa[i][0] = 0
            elif(mapa[i][1] == mapa[i][0]):
                mapa[i][1] += mapa[i][0]
                score+=mapa[i][1]
                mapa[i][0] = 0
        if k=='left':
            while(mapa[i][0]==0 and mapa[i][1]+mapa[i][2]!=0):
                mapa[i][0] = mapa[i][1]
                mapa[i][1] = mapa[i][2]
                mapa[i][2] = 0
            while(mapa[i][1]==0 and mapa[i][2]!=0):
                mapa[i][1] = mapa[i][2]
                mapa[i][2] = 0
            if(mapa[i][0] == mapa[i][1]):
                mapa[i][0]+=mapa[i][1]
                score+=mapa[i][0]
                mapa[i][1] = mapa[i][2]
                mapa[i][2] = 0
            elif(mapa[i][1] == mapa[i][2]):
                mapa[i][1] += mapa[i][2]
                score+=mapa[i][1]
                mapa[i][2] = 0
    
    for i in range(3):
        mapch.append([random.random(),random.random(),random.random()])
        for j in range(3):
            if mapch[i][j]>chanceGame and mapa[i][j]==0: mapa[i][j] = pow(pot,random.randint(1, 2)) 

    if (mapa[0][0]!=mapa[0][1] and mapa[0][1]!=mapa[0][2] and 
        mapa[1][0]!=mapa[1][1] and mapa[1][1]!=mapa[1][2] and 
        mapa[2][0]!=mapa[2][1] and mapa[2][1]!=mapa[2][2] and 
        
        mapa[0][0]!=mapa[1][0] and mapa[1][0]!=mapa[2][0] and 
        mapa[0][1]!=mapa[1][1] and mapa[1][1]!=mapa[2][1] and 
        mapa[0][2]!=mapa[1][2] and mapa[1][2]!=mapa[2][2] and

        flag and

        mapa[0][0]*mapa[0][1]*mapa[0][2]*mapa[1][0]*mapa[1][1]*mapa[1][2]*mapa[2][0]*mapa[2][1]*mapa[2][2]!=0
        ):
        lose = True
        flag = False
        drawScreen()

    if(not lose): drawScreen()
    else: 
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('Game OVER')
        break
    # -------- DEBUG ------------
    print('DEBUG = ' + k)
    print('score = '+str(score))
    # ---------------------------
    if k=='1': break
