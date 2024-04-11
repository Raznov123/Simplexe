from scipy.optimize import linprog
import numpy as np

def solve_simplex(obj, lhs, rhs, bnd):
    # Résoudre le problème d'optimisation linéaire avec la méthode du simplexe pour maximiser
    optimization_max = linprog(c=obj, A_ub=lhs, b_ub=rhs, bounds=bnd, method='simplex')
    
    # Vérifier si la solution maximale est réalisable
    if optimization_max.success:
        solution_max = optimization_max.x
    else:
        raise ValueError("Le problème n'a pas de solution maximale réalisable.")
    
    # Modifier les coefficients de l'objectif pour minimiser
    obj_min = [-c for c in obj]
    
    # Résoudre le problème d'optimisation linéaire avec la méthode du simplexe pour minimiser
    optimization_min = linprog(c=obj_min, A_ub=lhs, b_ub=rhs, bounds=bnd, method='simplex')
    
    # Vérifier si la solution minimale est réalisable
    if optimization_min.success:
        solution_min = [-x for x in optimization_min.x]
    else:
        raise ValueError("Le problème n'a pas de solution minimale réalisable.")
    
    return solution_max, solution_min
