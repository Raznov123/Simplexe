import tkinter as tk
from tkinter import ttk
from simplexe import solve_simplex

def solve_simplex_problem():
    # Récupérer les données du problème depuis les champs de saisie
    try:
        obj = list(map(float, obj_entry.get().split(',')))
        lhs_text_content = lhs_text.get("1.0", tk.END).strip().split("\n")
        lhs = [list(map(float, c.split(','))) for c in lhs_text_content]
        rhs = list(map(float, rhs_entry.get().split(',')))
        bnd = [(0, float('inf'))] * len(obj)

        # Appeler la fonction de résolution du simplexe
        solution_max, solution_min = solve_simplex(obj, lhs, rhs, bnd)

        # Afficher la solution dans le cadre solution
        solution_text = "Solution optimale :\n"
        for i, (max_val, min_val) in enumerate(zip(solution_max, solution_min)):
            solution_text += f"max: {max_val}, min: {min_val}\n"
        solution_label.config(text=solution_text)
    except Exception as e:
        solution_label.config(text=str(e))

root = tk.Tk()
root.title("Résolution de problème d'optimisation linéaire avec Simplexe")

input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ttk.Label(input_frame, text="Coefficients de l'objectif (séparés par des virgules):").grid(row=0, column=0, sticky="w")
obj_entry = ttk.Entry(input_frame, width=50)
obj_entry.grid(row=1, column=0, padx=5, pady=5)

ttk.Label(input_frame, text="Contraintes (une par ligne, séparées par des virgules):").grid(row=2, column=0, sticky="w")
lhs_text = tk.Text(input_frame, width=50, height=5)
lhs_text.grid(row=3, column=0, padx=5, pady=5)

ttk.Label(input_frame, text="RHS des contraintes (séparé par des virgules):").grid(row=4, column=0, sticky="w")
rhs_entry = ttk.Entry(input_frame, width=50)
rhs_entry.grid(row=5, column=0, padx=5, pady=5)

solve_button = ttk.Button(root, text="Résoudre", command=solve_simplex_problem)
solve_button.grid(row=1, column=0, padx=10, pady=10)

solution_frame = ttk.Frame(root, padding="10")
solution_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

solution_label = ttk.Label(solution_frame, text="")
solution_label.pack()

root.mainloop()
