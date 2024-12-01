"""Intuition:
#Read the text file
#Sort both the lists and compare them. Runtime: O(2*nlogn) + O(n) = O(nlogn)
"""

def main():
    #Read the text file
    with open(r'Day 1\input.txt', 'r') as file:
        list1 = []
        list2 = []
        for line in file:
            elements = line.split()
            list1.append(int(elements[0]))
            list2.append(int(elements[1]))
        list1.sort()
        list2.sort()

    #Compare the two lists
    cnt=0
    for i in range(len(list1)):
        cnt+=abs(list1[i]-list2[i])
    return cnt

if __name__ == '__main__':
    print(main())