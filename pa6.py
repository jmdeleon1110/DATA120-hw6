def make_change(total): 
    coin_types = [1,5,10,25,100]
    combinations = []    
    
    if total in coin_types:
        combinations.append([total])

    for coin in [c for c in coin_types if c < total]:
        sub_combinations = coin_combinations(total - coin)
        for combination in sub_combinations:
            new_combination = [coin] + combination
            new_combination.sort() 
            if new_combination not in combinations:  
                combinations.append(new_combination)

    return combinations

def dict_filter(funct, dictionary):
    
    new_dict = {}
    
    for k, v in dictionary.items():
        if funct(k, v):
            new_dict[k] = v
        return new_dict

def treemap(self, function):
    
        self.key = function(self.key)
        self.value = function(self.value)
        
        for child in self.children:
            child.treemap(function)

class DTree:
    def __init__(self, variable=None, threshold=None, lessequal=None, 
greater=None, outcome=None):
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome
    
    def tuple_atleast(self):

        def helper(child, max_index):
            if child is None:
                return max_index
            elif child.variable is not None:
                max_index = max(max_index, child.variable)
            max_index = max(helper(child.lessequal, max_index), 
helper(child.greater, max_index))
            return max_index

        max_index = helper(self, -1)

        return max_index + 1

    def find_outcome(self, variable):
        if self.outcome is not None:
            return self.outcome

        temperature, humidity, wind = variable

        if self.variable == 0:
            variable_value = temperature
        elif self.variable == 1:
            variable_value = humidity
        elif self.variable == 2:
            variable_value = wind

        if variable_value <= self.threshold:
            if self.lessequal is not None:
                return self.lessequal.find_outcome(variable)
            else:
                return self.outcome  
        else:
            if self.greater is not None:
                return self.greater.find_outcome(variable)
            else:
                return self.outcome 
        
    def no_repeats(self):

        def helper(child, existing_variables):
            if child is None:
                return True 
            elif child.variable in existing_variables:
                return False  
            else:
                existing_variables.add(child.variable)
                return helper(child.lessequal, existing_variables) and 
helper(child.greater, existing_variables)

        return helper(self, set()) 

