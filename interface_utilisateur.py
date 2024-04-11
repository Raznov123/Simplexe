import tkinter as tk
from tkinter import ttk
from simplexe import solve_simplex

def solve_simplex_problem():
    # Récupérer les données du problème depuis les champs de saisie
    coefficients = list(map(float, variables_entry.get().split(',')))
    constraints_text_content = constraints_text.get("1.0", tk.END).strip().split("\n")
    constraints = [list(map(float, c.split(','))) for c in constraints_text_content]
    objective = objective_combobox.get()

    # Appeler la fonction de résolution du simplexe
    solution = solve_simplex(coefficients, constraints, objective)

    # Afficher la solution dans l'interface utilisateur
    solution_text = "Solution optimale :\n"
    for var, val in solution.items():
        solution_text += f"{var}: {val}\n"
    solution_label.config(text=solution_text)

# Création de l'interface utilisateur
root = tk.Tk()
root.title("Résolution de problème d'optimisation linéaire avec Simplexe")

# Cadre pour entrer les données du problème
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ttk.Label(input_frame, text="Coefficients des variables (séparés par des virgules):").grid(row=0, column=0, sticky="w")
variables_entry = ttk.Entry(input_frame, width=50)
variables_entry.grid(row=1, column=0, padx=5, pady=5)

ttk.Label(input_frame, text="Contraintes (une par ligne):").grid(row=2, column=0, sticky="w")
constraints_text = tk.Text(input_frame, width=50, height=5)
constraints_text.grid(row=3, column=0, padx=5, pady=5)

ttk.Label(input_frame, text="Objectif:").grid(row=4, column=0, sticky="w")
objective_combobox = ttk.Combobox(input_frame, values=["max", "min"])
objective_combobox.grid(row=5, column=0, padx=5, pady=5)

# Bouton pour résoudre le problème
solve_button = ttk.Button(root, text="Résoudre", command=solve_simplex_problem)
solve_button.grid(row=1, column=0, padx=10, pady=10)

# Cadre pour afficher la solution
solution_frame = ttk.Frame(root, padding="10")
solution_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

solution_label = ttk.Label(solution_frame, text="")
solution_label.pack()

root.mainloop()
