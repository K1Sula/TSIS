n = int(input())
nums = []

for i in range(n):
    x = int(input())
    nums.append(x)

def spy_game(*nums):
    Yes_007 = False
    for j in range(len(nums) - 2 ):
        if j == 0:
            if nums[j] == 0 and nums[j + 1] == 0 and nums[j + 1] == 7:
                Yes_007 = True
                break
        elif j == len(nums) - 3:
            if nums[j] == 0 and nums[j + 1] == 0 and nums[j + 2] == 7 :
                Yes_007 = True
                break
        elif nums[j] == 0 and nums[j + 1 ] == 0 and nums[j + 2] == 7:
            Yes_007 = True
            break

    return Yes_007

Which_one = spy_game(*nums)
print(Which_one)

