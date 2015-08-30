#! /usr/bin/env python
# -*- coding: utf-8 -*- 

import os

#Différents énoncés
sudoku1=[[0,0,2,4,0,0,0,1,7],[0,6,0,0,3,2,5,0,4],[5,0,0,9,0,0,0,0,8],[6,0,8,0,0,0,9,3,0],[0,2,0,0,0,0,0,6,0],[0,5,3,0,0,0,8,0,1],[3,0,0,0,0,1,0,0,6],[2,0,4,8,6,0,0,5,0],[7,9,0,0,0,5,1,0,0]]
force1 = [[7,9,0,0,0,6,0,0,3],[0,0,1,0,2,0,0,7,0],[0,6,8,0,0,0,5,1,4],[0,0,0,3,9,0,6,0,0],[8,7,0,2,0,4,0,9,5],[0,0,6,0,8,5,0,0,0],[4,1,2,0,0,0,8,5,0],[0,5,0,0,4,0,3,0,0],[3,0,0,7,0,0,0,6,1]]
force3 = [[2,0,0,8,0,7,0,0,1],[0,0,1,0,0,4,8,0,0],[0,5,0,0,0,6,0,2,0],[8,9,3,0,0,0,0,0,2],[0,0,0,0,9,0,0,0,0],[7,0,0,0,0,0,9,4,8],[0,6,0,4,0,0,0,8,0],[0,0,2,1,0,0,4,0,0],[5,0,0,2,0,3,0,0,9]]
force4 = [[0,8,0,3,6,0,9,0,0],[0,9,0,0,0,0,0,0,0],[0,0,0,0,7,0,3,0,5],[8,0,0,0,0,1,2,0,0],[9,0,0,0,4,0,0,0,7],[0,0,7,5,0,0,0,0,1],[5,0,2,0,3,0,0,0,0],[0,0,0,0,0,0,0,6,2],[0,0,9,0,1,2,0,5,0]]
extrem = [[0,3,0,0,0,0,0,6,4],[0,0,0,0,0,0,7,0,9],[0,7,0,2,0,8,0,0,0],[2,6,0,0,0,9,0,0,0],[8,0,0,6,0,3,0,0,7],[0,0,0,1,0,0,0,3,2],[0,0,0,5,0,1,0,8,0],[9,0,5,0,0,0,0,0,0],[3,4,0,0,0,0,0,7,0]]

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

#Génère la grille de travail avec les différents candidats
def generate_candidat_grid(enonce):
    grid = enonce[:]
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                grid[i][j] = [1,2,3,4,5,6,7,8,9]
    return grid

def local_refresh_grid(grid, last_square_change):
    
    
    
    def refresh_line(i):
        case_change = []
        # Élimination des candidats dans les autres case de la ligne
        existant = []
        for j in range(9):
            if type(grid[i][j]) == int:
                existant.append(grid[i][j])
        for j in range(9):
            if type(grid[i][j]) != int:
                for c in existant:
                    if c in grid[i][j]:
                        grid[i][j].remove(c)
                        case_change.append((i,j))
        
        # Choix du chiffre s'il n'apparait comme candidat que dans une case
        occurence = [0,0,0,0,0,0,0,0,0]
        for j in range(9):
            if type(grid[i][j]) == list:
                for c in grid[i][j]:
                    occurence[c-1] = occurence[c-1] + 1
        for r in range(9):
            if occurence[r] == 1:
                for j in range(9):
                    if type(grid[i][j]) == list and ( (r+1) in grid[i][j] ):
                        grid[i][j] = (r+1)
                        case_change.append((i,j))
        return case_change
    
    
    
    def refresh_column(j):
        case_change = []
        # Élimination des candidats dans les autres case de la colonne
        existant = []
        for i in range(9):
            if type(grid[i][j]) == int:
                existant.append(grid[i][j])
        for i in range(9):
            if type(grid[i][j]) != int:
                for c in existant:
                    if c in grid[i][j]:
                        grid[i][j].remove(c)
                        case_change.append((i,j))
        
        # Choix du chiffre s'il n'apparait comme candidat que dans une case
        occurence = [0,0,0,0,0,0,0,0,0]
        for i in range(9):
            if type(grid[i][j]) == list:
                for c in grid[i][j]:
                    occurence[c-1] = occurence[c-1] + 1
        for r in range(9):
            if occurence[r] == 1:
                for i in range(9):
                    if type(grid[i][j]) == list and ( (r+1) in grid[i][j] ):
                        grid[i][j] = (r+1)
                        case_change.append((i,j))
        return case_change



    def refresh_square(a,b):
        case_change = []
        # Élimination des candidats dans les autres case du carré
        existant = []
        for i in range(3):
            for j in range(3):
                if type(grid[3*a+i][3*b+j]) == int:
                    existant.append(grid[3*a+i][3*b+j])
        for i in range(3):
            for j in range(3):
                if type(grid[3*a+i][3*b+j]) == list:
                    for c in existant:
                        if c in grid[3*a+i][3*b+j]:
                            grid[3*a+i][3*b+j].remove(c)
                            case_change.append((3*a+i,3*b+j))
        
        # Choix du chiffre s'il n'apparait comme candidat que dans une case
        occurence = [0,0,0,0,0,0,0,0,0]
        for i in range(3):
            for j in range(3):
                if type(grid[i][j]) == list:
                    for c in grid[i][j]:
                        occurence[c-1] = occurence[c-1] + 1
        for r in range(9):
            if occurence[r] == 1:
                for i in range(3):
                    for j in range(3):
                        if type(grid[i][j]) == list and ( (r+1) in grid[i][j] ):
                            grid[i][j] = (r+1)
                            case_change.append((i,j))
        return case_change
    


    # Execution des fonctions précédantes
    case_change = []
    for i in range(9):
        l = refresh_line(i)
        case_change = case_change + l
            
    for j in range(9):
        l = refresh_column(j)
        case_change = case_change + l
    
    for a in range(3):
        for b in range(3):
            l = refresh_square(a,b)
            case_change = case_change + l
    
    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) == list:
                if len(grid[i][j]) == 1:
                    grid[i][j] = grid[i][j][0]
                    case_change.append((i,j))
    
    #print(case_change)
    return (grid, case_change)



#all_square = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def naive(grid):
    case_change = [(0,0)] # Initialisation non vide
    iteration = 0
    while len(case_change) > 0:
        (grid, case_change)= local_refresh_grid(grid, case_change)
        iteration += 1
        print(grid)
        grid_disp(grid)
    print "Arrêt après %i itérations" % iteration
    return grid

def solve(grid):
    
    def choice_determination(grid):
        min_candidat_number = 9
        for i in range(9):
            for j in range(9):
                if type(grid[i][j]) == list and len(grid[i][j]) < min_candidat_number:
                    min_candidat_number = len(grid[i][j])
        if min_candidat_number == 0:
            print("Erreur1")
        else:
            for i in range(9):
                for j in range(9):
                    if type(grid[i][j]) == list and len(grid[i][j]) == min_candidat_number:
                        return (i,j)
            print("Erreur2")
    
    if is_full(grid):
        return (grid, True)
    else:
        if is_solvable(grid):
            print "grid est solvable"
            grid2 = naive(grid)
            if grid2 == grid:
                print is_solvable(grid)
                (i,j) = choice_determination(grid)
                candidat = grid[i][j]
                #Assignation temporaire
                print "Décision arbitraire en (%i,%i)" % (i,j)
                grid2[i][j] = candidat[0]
                (hyp_grid, sol_hyp) = solve(grid2)
                if is_full(hyp_grid):
                    return (hyp_grid, True)
                else:
                    print "Mauvaise décision"
                    candidat = candidat[1:]
                    grid[i][j] = candidat
                    return solve(grid)
            else:
                return solve(grid2)
        else:
            return (grid, False)



def is_full(grid):
    for i in grid:
        for j in i:
            if type(j) == list:
                return False
    return True

def is_solvable(grid):
    for i in grid:
        for j in i:
            if type(j) == list and j == []:
                return False
    return True
# Différents test de fonctionnement

if __name__ == '__main__':
    #grid_disp(null_grid_generate())
    #grid_disp(sudoku1)
    #print(generate_candidat_grid(sudoku1))
    grid = generate_candidat_grid(extrem)
    #print(grid)
    solve(grid)
    all_square = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    '''for i in range(10):
        (grid, square_change)= local_refresh_grid(grid, all_square)
        print(grid)
        grid_disp(grid)
'''