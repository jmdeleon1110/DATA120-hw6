#!/usr/bin/env python
# coding: utf-8

# Problem 1: how many ways to make change?

# In[110]:


def coin_combinations(total): 
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


# In[111]:


dime = coin_combinations(10)
dime


# In[112]:


len(dime)


# Problem 2: dictionary filter

# In[75]:


def dict_filter(funct, dictionary):
    
    new_dict = {}
    
    for k, v in dictionary.items():
        if funct(k, v):
            new_dict[k] = v
        return new_dict   


# In[77]:


def checker(name, abbrev):
    return abbrev[0] == "I" and name[1] == "l"

example = {"Illinois": "IL", "Pennsylvania": "PA", "Indiana": "IN"}

dict_filter(checker, example)


# Problem 3: Tree Map

# In[109]:


def treemap(function, tree):
    key = function(tree.key)
    value = function(tree.value)
    tree.key = key
    tree.value = value
    
    for child in tree.children:
        treemap(function, tree)


# In[107]:


def update(key, value):
    lambda x, y: (x.upper(), y * 1000000)


# Problem 4: Tree modeling decisions

# In[142]:


class DTree:
    def __init__(self, variable=None, threshold=None, lessequal=None, greater=None, outcome=None):
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome
    
    def tuple_atleast(self):

        def traverse(child, max_index):
            if child is None:
                return max_index
            elif child.variable is not None:
                max_index = max(max_index, child.variable)
            max_index = max(traverse(child.lessequal, max_index), traverse(child.greater, max_index))
            return max_index

        max_index = traverse(self, -1)

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
                return helper(child.lessequal, existing_variables) and helper(child.greater, existing_variables)

        return helper(self, set()) 


# In[137]:


example_tree = DTree(
    0, 66,
    DTree(
        2, 10,
        DTree(None, None, None, None, "walk"),
        DTree(None, None, None, None, "stay home"),
        None
    ),
    DTree(None, None, None, None, "stay home"),
    None
)


# In[138]:


tuple_atleast(example_tree)

