!pip install pulp
import pulp

# Create a Linear Programming Maximization problem
prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')

# Objective function
prob += 40 * x + 30 * y, "Total_Profit"

# Constraints
prob += 2 * x + y <= 100, "Machine_1_Capacity"
prob += x + 2 * y <= 80, "Machine_2_Capacity"

# Solve the problem
status = prob.solve()

# Output the results
print("Status:", pulp.LpStatus[status])
print(f"Optimal production of Product A: {x.varValue:.2f} units")
print(f"Optimal production of Product B: {y.varValue:.2f} units")
print(f"Maximum Profit: ${pulp.value(prob.objective):.2f}")
