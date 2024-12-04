import re

def reader(file):
    """Helper function, reads a file and returns its content as a single string"""
    with open(file) as f:
        return f.read()

def preprocessing(data):
    """
    Preprocess the input data by finding all occurrences of specific patterns.
    
    The function uses a regular expression to match the following patterns in the input data:
    1. `mul(x,y)` - Matches multiplication operations where `x` and `y` are integers (1 to 3 digits).
    2. `don't()` - Matches the exact string "don't()".
    3. `do()` - Matches the exact string "do()".
    
    Args:
        data (str): The input data as a string.
        
    Returns:
        list: A list of strings matching the specified patterns.
    """
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    return re.findall(pattern, data)

def mul(a,b):
    return a*b

if __name__ == '__main__':
    data = reader(r'Day 3\input.txt')
    pre = preprocessing(data)
    ans = 0
    #Seperate based on do and don't
    is_do = True
    for op in pre:
        if op == "do()":
            is_do = True
            continue
        elif op == "don't()":
            is_do = False
            continue
        else:
            if is_do:
                a,b = map(int,op[4:-1].split(','))
                ans+=mul(a,b)
    print(ans)