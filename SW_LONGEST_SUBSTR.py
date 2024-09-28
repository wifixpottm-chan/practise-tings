class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0

        if len(s)==0:
            return 0
        se=set()

        maxi=1

        while r<len(s):
            if s[r] not in se:
                se.add(s[r])
                
            else:
                while s[r] in se:
                    se.remove(s[l])
                    l+=1
                se.add(s[r])

            r+=1
            maxi=max(r-l,maxi)
        return maxi
