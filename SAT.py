from pulp import PULP_CBC_CMD, LpVariable, LpProblem, LpMaximize, LpSolver, value

from main import BooleanLogic

def FindSat(input) :
    # define input string
    booleanLogic = BooleanLogic(input)
    variables = {}

    # define variables
    for each in input:
        for literalItem in each.split(';'):
            if literalItem is None:
                continue
            
            if '-' in literalItem:
                v = literalItem.strip('-')
                variables[v] = LpVariable(v,cat="Binary")
            else:
                variables[literalItem] = LpVariable(literalItem, cat="Binary")
        
    problem = LpProblem('SAT', LpMaximize)

    # define or constraints (split on semicolon for OR)
    orVariables = []
    for item in input:
        newOr = LpVariable(item+'_or')
        separatedLiterals = item.split(';') #are we splitting on a semi-colon twice?
        orComponent = []
        for l in separatedLiterals:
            if l is None:
                continue
            if('-' in l): # each of these branches: add to 'orComponent' list for use in the last constraint
                # find variable[l]
                orComponent.append(not variables[l.strip('-')])
                problem += newOr >= (not variables[l.strip('-')])
            else:
                orComponent.append(variables[l])
                problem += newOr >= variables[l]

        problem += newOr <= sum(orComponent)
        orVariables.append(newOr)

    print(orVariables)

    sumName = '' + ''.join(input) + '_and'
    newAND = LpVariable(sumName)
    for orVar in orVariables:
        problem += newAND <= orVar

    problem += newAND >= sum(orVariables, -1)

    status = problem.solve(PULP_CBC_CMD(msg=1))

    # define not constraints
    #find every variable with a dash right in front of it and add a - to it
    #to explore the possiblity of adding a not to it, let's save all of these constraints to a list for now as well
    print(status)
    # answer = LpSolver.actualSolve(problem) #google says any NaN variables, or duplicate variable names, will cause this error
    # print(answer)

    BinaryLiterals = {}
    for solution in variables.keys():
        BinaryLiterals[solution] = value(variables[solution])
    
    print(BinaryLiterals)

    #define constraints for everything being ored


    #problem += booleanLogic.GetSATResult(variables) == True #except, does it want the list of variables itself, or really just each of the letters it represents?

    # define how it knows the problem is correct
    #problem += BooleanLogic.GetSATResult


input = ['a']
FindSat(input)