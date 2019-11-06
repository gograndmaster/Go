# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:06:20 2019

@author: user
"""

import pandas as pd

class gPoint():
    def __init__(self,state,across,endlong):
        self.state = state
        self.across = across
        self.endlong = endlong

gBoard=pd.DataFrame()

for i in range(1,20):
    for j in range(1,20):
        gBoard.at[i,j]=gPoint('EMPTY',i,j)
        
def gCheck(i,j):
    print(gBoard.at[i,j].state,",",
          gBoard.at[i,j].across,",",
          gBoard.at[i,j].endlong)

def w(gpAcross,gpEdnlong):
    if gBoard.at[gpAcross,gpEdnlong].state!="EMPTY":
        print('MoveFailed:This point is not empty!')
    else:
        gBoard.at[gpAcross,gpEdnlong].state="WHITE"
        gCheck(gpAcross,gpEdnlong)
    
def b(gpAcross,gpEdnlong):
    if gBoard.at[gpAcross,gpEdnlong].state!="EMPTY":
        print('MoveFailed:This point is not empty!')
    else:
        gBoard.at[gpAcross,gpEdnlong].state="BLACK"
        gCheck(gpAcross,gpEdnlong)
