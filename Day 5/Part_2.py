from collections import defaultdict
def reader(file):
    """Helper function, reads a file and returns a list of lines."""
    with open(file) as f:
        rules, updates = f.read().split('\n\n')
        return rules.split('\n'), updates.split('\n')
    
def createDefaultDict(rules):
    """Creates a dictionary with the rules as keys and the values as the corresponding
    values in the rules."""
    rules_dict = defaultdict(set)
    for rule in rules:
        key, value = rule.split('|')
        rules_dict[int(value)].add(int(key))
    return rules_dict

def checkRules(rules_dict, update):
    """Checks the rules against the update and returns a value based on the rules.
    
    Args:
        rules_dict (defaultdict): The dictionary containing the rules.
        update (str): The update string to check against the rules.
        
    Returns:
        boolean: Return True if the rules are satisfied, otherwise False.
    """
    update = update.split(',')
    tmp = set()
    for i in range(len(update)):
        if int(update[i]) in tmp:
            return False
        tmp.update(rules_dict[int(update[i])])
    return True

def sorter(rules_dict, update):
    """Sorts the update based on the rules and returns the middle value of the sorted list.
    
    Args:
        rules_dict (defaultdict): The dictionary containing the rules.
        update (str): The update string to sort based on the rules.
        
    Returns:
        int: The middle value of the sorted list.
    """
    update = update.split(',')
    tmp = defaultdict(int)
    
    # Initialize the tmp dictionary with the update values as keys and 0 as their values.
    for i in range(len(update)):
        tmp[int(update[i])] = 0
    
    # Count the occurrences of each rule in the update.
    for i in range(len(update)):
        for j in rules_dict[int(update[i])]:
            if j in tmp:
                tmp[j] = tmp[j] + 1
    
    # Sort the tmp dictionary by its values in descending order and get the keys.
    sorted_tmp = [k for k, v in sorted(tmp.items(), key=lambda item: item[1], reverse=True)]
    
    # Return the middle value of the sorted list.
    return sorted_tmp[len(sorted_tmp) // 2]
    



if __name__ == '__main__':
    # Read the rules and updates from the input file
    rules, updates = reader(r'Day 5\input.txt')
    
    # Create a dictionary from the rules
    rules = createDefaultDict(rules)
    
    ans = 0
    
    # Iterate through each update except the last one
    for update in updates[:-1]:
        # Check if the update satisfies the rules
        if not checkRules(rules, update):
            # If not, add the middle value of the sorted update to the answer
            ans += sorter(rules, update)
    
    # Print the final answer
    print(ans)
        

   