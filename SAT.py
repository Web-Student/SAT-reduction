from pulp import LpVariable, LpProblem, LpMaximize, value

from main import BooleanLogic

# define input string
input = 'a;b;-c'
booleanLogic = BooleanLogic(input)
variables = {}

# define variables
for each in input.split(';'):
    if '-' in each:
        v = each.strip('-')
        variables[v] = LpVariable(v)
    else:
        variables[each] = LpVariable(v)
    
problem = LpProblem('SAT')

# define constraints
for var in variables.keys():
    problem += (variables[var] == 0 or variables[var] == 1)


#problem += booleanLogic.GetSATResult(variables) == True #except, does it want the list of variables itself, or really just each of the letters it represents?

# define how it knows the problem is correct
#problem += BooleanLogic.GetSATResult

result = problem.solve()