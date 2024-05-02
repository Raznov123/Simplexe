import tkinter as tk
import numpy as np
from scipy.optimize import linprog

# Create the main application window
root = tk.Tk()
root.title("Simplex Solver")

# Number of Coefficients for Objective Function Label and Entry
num_coefficients_label = tk.Label(root, text="Number of Coefficients:")
num_coefficients_label.grid(row=0, column=0, padx=5, pady=5)

num_coefficients_entry = tk.Entry(root, width=5)
num_coefficients_entry.grid(row=0, column=1, padx=5, pady=5)

# Number of Constraints Label and Entry
num_constraints_label = tk.Label(root, text="Number of Constraints:")
num_constraints_label.grid(row=1, column=0, padx=5, pady=5)

num_constraints_entry = tk.Entry(root, width=5)
num_constraints_entry.grid(row=1, column=1, padx=5, pady=5)

# Objective Function Coefficients
def update_objective_coefficients(event):
    num_coeffs_text = num_coefficients_entry.get()
    if num_coeffs_text.isdigit():
        num_coeffs = int(num_coeffs_text)
        for label, entry in zip(objective_coefficient_labels, objective_coefficient_entries):
            label.grid_forget()
            entry.grid_forget()
        del objective_coefficient_labels[:]
        del objective_coefficient_entries[:]

        for i in range(num_coeffs):
            label = tk.Label(root, text=f"X{i+1} :")
            label.grid(row=2, column=i+2, padx=(0, 5), pady=(5, 3), sticky='e')
            entry = tk.Entry(root, width=5)
            entry.grid(row=2, column=i+3, padx=(0, 10), pady=(5, 3), sticky='w')
            objective_coefficient_labels.append(label)
            objective_coefficient_entries.append(entry)

num_coefficients_entry.bind('<KeyRelease>', update_objective_coefficients)

objective_coefficient_labels = []
objective_coefficient_entries = []

# Constraints
def update_constraint_rows_on_entry(event):
    num_constraints_text = num_constraints_entry.get()
    if num_constraints_text.isdigit():
        num_constraints = int(num_constraints_text)
        update_constraint_rows(num_constraints)

num_constraints_entry.bind('<KeyRelease>', update_constraint_rows_on_entry)

constraint_entries = []
constraint_frames = []  # Store frames for constraints

def update_constraint_rows(num_constraints):
    for frame in constraint_frames:
        frame.grid_forget()  # Remove frames from grid

    constraint_entries.clear()  # Clear entries list
    constraint_frames.clear()  # Clear frames list

    for i in range(num_constraints):
        constraint_frame = tk.Frame(root)
        constraint_frame.grid(row=i+3, column=0, columnspan=5, padx=5, pady=(0, 3), sticky='w')
        constraint_frames.append(constraint_frame)

        constraint_entries.append([tk.Entry(constraint_frame, width=5) for _ in range(int(num_coefficients_entry.get()) + 1)])
        for j, entry in enumerate(constraint_entries[i]):
            entry.grid(row=0, column=j, padx=5, pady=5)

def solve():
    # Collect coefficients
    c = [float(entry.get()) for entry in objective_coefficient_entries]

    # Collect constraints
    A = []
    b = []
    for entries in constraint_entries:
        constraint_coeffs = [float(entry.get()) for entry in entries[:-1]]
        constraint_rhs = float(entries[-1].get())
        A.append(constraint_coeffs)
        b.append(constraint_rhs)

    # Convert to numpy arrays
    c = np.array(c)
    A = np.array(A)
    b = np.array(b)

    # Solve linear programming problem
    max_solution = linprog(c, A_ub=A, b_ub=b, method='highs')  # Maximize
    min_solution = linprog(-c, A_ub=A, b_ub=b, method='highs')  # Minimize

    # Display results
    result_label.config(text=f"Max Solution: {max_solution.fun}\nMin Solution: {min_solution.fun}")

# Solve Button
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=100, column=0, columnspan=2, pady=10)

# Output Area
output_frame = tk.Frame(root)
output_frame.grid(row=101, column=0, columnspan=2)

result_label = tk.Label(output_frame, text="")
result_label.pack()

root.mainloop()
