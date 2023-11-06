class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    x=[i,j]
                    return x
                    break
                
            
s=Solution()
input_string=input("list of numbers ")
break_string=input_string.split()
nums=[int(num) for num in break_string]
target=int(input("provide the sum of two numbers "))
result=s.twoSum(nums,target)
print("here is the indices of the numbers ",result)
