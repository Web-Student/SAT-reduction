
#useless comment
f = ['a;b;c', '-a;b;-c', '-d;-b', '-a;c', '-b;a']

class Verifier():
    def __init__(self, charValues):
        self.characterValues = charValues

    def Verify_sat(self, InputDictionary):
        def Or(inputs):
            separated_inputs = inputs.split(';')

            for i in separated_inputs:
                j = InputDictionary[i.strip('-')]
                if ('-' in i):
                    j = not j
                
                if(j):
                    return True
                
            return False
    
        accumuluated_bool = []

        for item in self.characterValues:
            accumuluated_bool.append(Or(item))

        if(False not in accumuluated_bool):
            return True
        else:
            return False


    def Get(self):
        for value in self.input_list():
            if (value):
                return 1
            
        return 0 #if we didn't find anything that was true
    
class SATStruct():
    def __init__(self, inputstruct):
        self.init


def test_And_Three_Ones():
    threeOnes = Verifier(['a','b','c'])
    answer = threeOnes.Verify_sat({'a':1, 'b': 1, 'c':1})
    assert answer

def test_Not_function_works():
    threeOnes = Verifier(['a','-b','c'])
    answer = threeOnes.Verify_sat({'a':1, 'b': 0, 'c':1})
    assert answer == True

def test_Or_Works():
    threeOnes = Verifier(['a;b;c'])
    answer = threeOnes.Verify_sat({'a':0, 'b': 0, 'c':0})
    assert answer == False

def test_Or_Works_again():
    threeOnes = Verifier(['a;b;c'])
    answer = threeOnes.Verify_sat({'a':0, 'b': 0, 'c':1})
    assert answer == True

def test_Longer_function():
    threeOnes = Verifier(['a;b;c', '-a;b;-c', '-d;-b', '-a;c', '-b;a'])
    answer = threeOnes.Verify_sat({'a':1, 'b': 1, 'c':1, 'd':0})
    assert answer == True

def test_Longer_function_is_false():
    threeOnes = Verifier(['a;b;c', '-a;b;-c', '-d;-b', '-a;c', '-b;a'])
    answer = threeOnes.Verify_sat({'a':0, 'b': 1, 'c':1, 'd':0})
    assert answer == False

def test_two_inputs():
    threeOnes = Verifier(['a;b', '-a;-b'])
    answer = threeOnes.Verify_sat({'a':0, 'b': 0})
    assert answer == False
    answer = threeOnes.Verify_sat({'a':0, 'b': 1})
    assert answer == True
    answer = threeOnes.Verify_sat({'a':1, 'b': 0})
    assert answer == True
    answer = threeOnes.Verify_sat({'a':1, 'b': 1})
    assert answer == False
    
def test_Always_false():
    threeOnes = Verifier(['a','b', '-a','-b'])
    answer = threeOnes.Verify_sat({'a':0, 'b': 0})
    assert answer == False
    answer = threeOnes.Verify_sat({'a':0, 'b': 1})
    assert answer == False
    answer = threeOnes.Verify_sat({'a':1, 'b': 0})
    assert answer == False
    answer = threeOnes.Verify_sat({'a':1, 'b': 1})
    assert answer == False

test_Not_function_works()