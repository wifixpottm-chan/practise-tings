class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        tempk=k
        i=0
        j=0
        maxi=0
        while j<len(nums):
            if nums[j]==1 and tempk>=0:         
                j+=1
            elif nums[j]==0 and tempk>0:
                j+=1
                tempk-=1
                print('hi', tempk)
            elif nums[j]==0 and tempk==0:
                while tempk<=0:
                    if nums[i]==0:
                        tempk+=1
                    i+=1
            maxi=max(maxi,j-i)
        return maxi
