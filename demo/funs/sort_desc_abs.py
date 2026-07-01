
nums = [-10, 5, 4, -30, 55, -90]

for num in sorted(nums, key = abs, reverse=True):
    print(num)

