def buildArray(nums):
    #nums = [0,2,1,5,3,4]
    ans = []
    # i = to the index of nums

    for i in range(len(nums)):
        ans.append(nums[nums[i]])
        print(ans)
    return ans
        

buildArray([0,2,1,5,3,4])

