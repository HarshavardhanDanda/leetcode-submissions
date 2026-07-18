class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        i,j=0,0
        k=set()
        maxSum=0
        while(j<len(s)):
            if(s[j] in k):
                while(s[j] in k):
                    k.remove(s[i])
                    i+=1
            k.add(s[j])
            print(s[i:j+1], i, j)
            maxSum=max(maxSum, j-i+1)
            j+=1
        return maxSum

        