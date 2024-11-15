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

# define or constraints (split on semicolon)
separatedOrs = input.split(';')
#for item in separatedOrs:
    # problem += output >= parseAnyNot(item1)
    # problem += output >= parseAnyNot(item2)
    # problem += output <= parseAnyNot(item1) + parseAnyNot(item2)




# define not constraints
#find every variable with a dash right in front of it and add a - to it
#to explore the possiblity of adding a not to it, let's save all of these constraints to a list for now as well
notConstraints = []
split_on_dashes = input.split('-')
for segment in split_on_dashes:
    notVar = segment[0]
    newLPProblem = (1 - variables[notVar])
    problem += newLPProblem
    notConstraints.append(newLPProblem)


#define constraints for everything being ored


#problem += booleanLogic.GetSATResult(variables) == True #except, does it want the list of variables itself, or really just each of the letters it represents?

# define how it knows the problem is correct
#problem += BooleanLogic.GetSATResult

result = problem.solve()