

def twoSum(nums, target: int):
    length = len(nums)
    for i in range(length):
        for j in range(i+1,length):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

if __name__ == '__main__':
    print(twoSum([3, 4, 5, 1], 6))