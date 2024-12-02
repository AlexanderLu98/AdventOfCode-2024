
def reader(file):
    """Helper function, reads a file and returns a list of lines."""
    with open(file) as f:
        return [line.strip() for line in f]

def checker(data):
    """
    Checks if the given list of numbers is in strictly decreasing or increasing order
    with a difference of 1 to 3 between consecutive numbers.

    Args:
        data (list of str): A list of string representations of numbers.

    Returns:
        bool: True if the list is in strictly decreasing or increasing order with the
              specified difference between consecutive numbers, False otherwise.
    """
    #Decreasing or increasing order
    if int(data[0])==int(data[1]):
        return False
    elif int(data[0]) > int(data[1]):
        is_decreasing = True
    else:
        is_decreasing = False
    
    #Iterate thorugh list and check if the difference between consecutive numbers is between 1 and 3
    data_len = len(data)
    for i in range(data_len - 1):
        if is_decreasing:
            diff = int(data[i]) - int(data[i+1])
            if diff < 1 or diff > 3:
                return False
        else:
            diff = int(data[i+1]) - int(data[i])
            if diff < 1 or diff > 3:
                return False
    return True
    
if __name__ == '__main__':
    data = reader(r'Day 2\input.txt')
    cnt = 0
    for line in data:
        report = line.split()
        #Brute force approach to find the number of valid reports
        for i in range(len(report)):
            tmp = report[:i] + report[i+1:]
            if checker(tmp):
                cnt+=1
                print(tmp)
                break
    print(cnt)
