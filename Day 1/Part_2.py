#Counter on second list
#for loop over first list with key value pair to the counter
#return sum
from collections import Counter
def part_2():
    #Read the text file
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
