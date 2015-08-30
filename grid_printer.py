#! /usr/bin/env python
# -*- coding: utf-8 -*- 

#Présente de façon visuelle une grille
def grid_disp(g): #g est de dimension 9*9
    for i in range(3):
        for j in range(3):
            tmp=""
            for k in range(9):
                if type(g[3*i+j][k]) == int:
                    tmp=tmp+str(g[3*i+j][k])+" "
                else:
                    tmp = tmp + "  "
                if(k==2 or k==5):
                    tmp=tmp+"| "
            print(tmp)
            #print(g[3*i+j])
        if(i<=1):
            print("---------------------")
    print(" ")
