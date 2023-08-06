def threeSum(nums):
        sumarr = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l = 1
            r = len(nums) - 1
            while l < r:
                n = sorted([nums[i],nums[l],nums[r]])
                if nums[i]+nums[l]+nums[r] == 0:
                    if n not in sumarr: 
                        sumarr.append(n)
                    l+=1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l+=1
                else:
                    r-=1
        return sumarr

print(threeSum([1,2,-2,-1]))