def productExceptSelf(nums):
    res = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        res[i] = res[i] * prefix
        prefix = prefix * nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * postfix
        postfix = postfix * nums[i]
    return res

# Add your input here
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)
