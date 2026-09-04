class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        letter_set = set(s)

        best = 0

        for current_letter in letter_set:
            begin = 0
            end = 0

            wrong_chars=0



            for char in s:
                if char != current_letter:

                    wrong_chars+=1

                    while wrong_chars > k:
                        if s[begin] != current_letter:
                            wrong_chars -= 1

                        begin+=1

                end+=1
                
                best = max(best,end-begin)

        return best

s = Solution()

print(s.characterReplacement("ABAB",2))