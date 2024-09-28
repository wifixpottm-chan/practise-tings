class Solution:
    def totalFruits(self,arr):
        i=0
        j=0
        maxi=0
        s={}
        
        while j<len(arr):
            if arr[j] not in s and len(s)<2:
                s[arr[j]]=1
                j+=1
            elif arr[j] not in s and len(s)==2:
                while len(s)==2:
                    s[arr[i]]=s[arr[i]]-1
                    if s[arr[i]]==0:
                        del s[arr[i]]
                    i+=1
                s[arr[j]]=1
                j+=1
            elif arr[j] in s:
                s[arr[j]]+=1
                j+=1
        
            maxi=max(maxi,sum(s.values()))
        
        return maxi
