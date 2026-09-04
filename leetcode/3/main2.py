class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin=0
        end=0
        max_len = 0

        tmp_str = ""

        for char in s:
            if char not in tmp_str:
                tmp_str += char
            else:
                while char in tmp_str:
                    tmp_str = tmp_str[1:]
                tmp_str += char

            max_len = max(max_len, len(tmp_str))
            print(char, max_len)

        return max_len
