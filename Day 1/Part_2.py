
from collections import Counter
def part_2():
    """
This script reads a text file containing pairs of integers, processes the data, and calculates a sum based on the frequency of the second list's elements.
Functions:
    part_2(): Reads the input file, processes the data into two lists, counts the frequency of elements in the second list, and calculates the sum based on the frequency of elements in the first list.
Usage:
    Run the script to execute the part_2 function and print the result.
Example:
    Given an input file 'input.txt' with the following content:
    1 2
    3 4
    1 2
    The script will output the calculated sum based on the described logic.
    """
    with open(r'Day 1\input.txt', 'r') as file:
        list1 = []
        list2 = []
        for line in file:
            elements = line.split()
            list1.append(int(elements[0]))
            list2.append(int(elements[1]))
        Counter_list = Counter(list2)
    ans = 0
    for i in range(len(list1)):
        ans += list1[i] * Counter_list[list1[i]]
    return ans

if __name__ == '__main__':
    print(part_2())
