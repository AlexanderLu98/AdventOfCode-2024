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
        int: The middle value of the update if the rules are satisfied, otherwise 0.
    """
    update = update.split(',')
    tmp = set()
    for i in range(len(update)):
        if int(update[i]) in tmp:
            return 0
        tmp.update(rules_dict[int(update[i])])
    return int(update[len(update)//2])



if __name__ == '__main__':
    # Read the rules and updates from the input file
    rules, updates = reader(r'Day 5\input.txt')
    
    # Create a dictionary from the rules
    rules = createDefaultDict(rules)
    
    ans = 0
    # Iterate through each update (excluding the last empty line)
    for update in updates[:-1]:
        # Check the rules against the update and accumulate the result
        ans += checkRules(rules, update)
    
    # Print the final accumulated result
    print(ans)

   