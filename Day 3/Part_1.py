import re

def reader(file):
    """Helper function, reads a file and returns its content as a single string"""
    with open(file) as f:
        return f.read()

def preprocessing(data):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, data)

def mul(a,b):
    return a*b

if __name__ == '__main__':
    data = reader(r'Day 3\input.txt')
    pre = preprocessing(data)
    ans = 0
    for op in pre:
        a,b = map(int,op[4:-1].split(','))
        print(mul(a,b))
        ans+=mul(a,b)
    print(ans)