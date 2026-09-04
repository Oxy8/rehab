class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin=0
        end=0
        max_len = 0


        for char in s:
            if char not in s[begin:end]:
                end+=1
            else:
                while char in s[begin:end]:
                    begin+=1
                end+=1

            max_len = max(max_len, (end-begin))
            #print(char, max_len)



        return max_len

s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))