import pandas as pd

#" " means empty,"s" means solid(border),"b"means black,"w" means white
gBoard=pd.DataFrame(' ',columns=range(21),index=range(21))
gBoard.at[[0,20],:]=('s')
gBoard.at[:,[0,20]]=('s')

def FtEat(i,j):
    if ((gBoard.at[i-1,j]!=' ') & (gBoard.at[i-1,j]!=gBoard.at[i,j]) &
        (gBoard.at[i+1,j]!=' ') & (gBoard.at[i+1,j]!=gBoard.at[i,j]) &
        (gBoard.at[i,j-1]!=' ') & (gBoard.at[i,j-1]!=gBoard.at[i,j]) &
        (gBoard.at[i,j+1]!=' ') & (gBoard.at[i,j+1]!=gBoard.at[i,j])):
        gBoard.at[i,j]=" "
        
def w(i,j):
    if gBoard.at[i,j]!=" ":
        print('MoveFailed:This point is not empty!')
    else:
        gBoard.at[i,j]="w"
        FtEat(i,j)
        print("WHITE",",",i,",",j)
    
def b(i,j):
    if gBoard.at[i,j]!=" ":
        print('MoveFailed:This point is not empty!')
    else:
        gBoard.at[i,j]="b"
        FtEat(i,j)
        print("black",",",i,",",j)
