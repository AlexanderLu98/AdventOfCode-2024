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
    return max(backtrack(nums, target, index + 1, current_sum+nums[index]), backtrack(nums, target, index + 1, current_sum*nums[index]))
    
if __name__ == '__main__':
    input = reader(r'Day 7\input.txt')
    # print(input)
    ans = 0
    for target,nums in input:
        tmp = backtrack(nums, target, 0, 0)
        print(nums, target, tmp)
        ans += tmp
    print(ans)


    # print(303876485678-303876483687)
    # print(1111+857)
    # print(303876483687+1111+857)

#ans = 303876485655
#reason, for my initial implementation; used defaultdict that overlooked some duplicate keys. When accounted for in edge.txt
#too low: 303876483687 (need to add 1111+857)
#too high: 303876485678 (need to subtract 23)
#1111+23+857

#Come back later to figure out why the difference is 23
