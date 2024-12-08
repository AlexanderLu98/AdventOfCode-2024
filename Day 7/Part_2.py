from collections import defaultdict

def reader(file):
    with open(file) as f:
        input = []
        for line in f:
            target, *nums = line.split(":")
            nums = list(map(int, "".join(nums).split()))
            input.append((int(target), nums))
        return input

# backtracking on operator "*" and "+" and verify the results are the same as the key of the dictionary at the end. return the key if it is the same. else return 0
def backtrack(nums, target, index, current_sum):
    if current_sum > target:
        return 0
    if index == len(nums):
        if target == current_sum:
            return target
        return 0
    conc = int(str(current_sum)+str(nums[index]))
    return max(backtrack(nums, target, index + 1, current_sum+nums[index]), backtrack(nums, target, index + 1, current_sum*nums[index]), backtrack(nums, target, index + 1, conc))
    
if __name__ == '__main__':
    input = reader(r'Day 7\edge.txt')
    # print(input)
    ans = 0
    for target,nums in input:
        tmp = backtrack(nums, target, 0, 0)
        print(nums, target, tmp)
        ans += tmp
    print(ans)

    #too high: 146111650243239
    #too high 146111650243239-23 = 146111650243216
    #not right 146111650243239-857 = 146111650242382
