class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=0
        d={}
        ans=[]
        while l+9<len(s):
            st=s[l:l+10]
            if st in d:
                if d[st]==1:
                    ans.append(st)

                d[st]+=1
                
            else:
                d[st]=1

            l+=1
        return ans
