f = open('26.1.txt')
n = int(f.readline())
nums = []
for _ in range(n):
    pair = list(map(int, f.readline().split()))
    pair[1] = -pair[1]
    nums += [pair]
nums.sort()
r, m = 0, 0
for i in range(1, len(nums)):
    if nums[i][0] == nums[i-1][0]:
        if nums[i][1] - nums[i-1][1] == 3:
            r = nums[i][0]
            m = -nums[i][1] + 1
print(r, m)
