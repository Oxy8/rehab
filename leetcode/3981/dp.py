from functools import cache

class Solution(object):

    def interleaveCharacters(self, word1, word2, target):
        return self.interleaveCharactersInner(word1, word2, target)
        return (self.interleaveCharactersInner(word1, word2, target, False, False) % 1000000007)
    
    @cache
    def interleaveCharactersInner(self, word1, word2, target):
        """
        :type word1: str
        :type word2: str
        :type target: str
        :rtype: int
        """
        len_word_1 = len(word1)
        len_word_2 = len(word2)
        len_target = len(target)

        dp = [[[0] * (len_word_1 + 1) for _ in range(len_word_2+1)] for _ in range(len_target)]

        for i_letra_t in range(len_target):

            for i_letra_w1 in range(len_word_1):
                if word1[i_letra_w1] == target[i_letra_t]:
                    for iter_1 in range(i_letra_w1+1):
                        for iter_2 in range(len_word_2):
                            dp[i_letra_t][iter_2][iter_1] += 1

            for i_letra_w2 in range(len_word_2):
                if word2[i_letra_w2] == target[i_letra_t]:
                    for iter_2 in range(i_letra_w2+1):
                        for iter_1 in range(len_word_1):
                            dp[i_letra_t][iter_2][iter_1] += 1

        for i_letra_t in range(len_target-2, -1, -1):
            for i_letra_w1 in range(len_word_1):
                for i_letra_w2 in range(len_word_2):
                    dp[i_letra_t][i_letra_w2][i_letra_w1] = max(dp[i_letra_t+1][i_letra_w2][i_letra_w1+1],dp[i_letra_t+1][i_letra_w2+1][i_letra_w1])*dp[i_letra_t][i_letra_w2][i_letra_w1]




        return dp[0][0][0]                                             
                    

        return (sum_word_1 + sum_word_2)


sol= Solution()
print(sol.interleaveCharacters("abc", "bac", "abc"))
print(sol.interleaveCharacters("cd", "cd", "ccd"))
print(sol.interleaveCharacters("xy", "xy", "xyxy"))
print(sol.interleaveCharacters("ab", "cde", "ace"))
#print(sol.interleaveCharacters("g", "jfgg", "jgfgg"))
#print(sol.interleaveCharacters("m", "mlklo", "mlk"))

# print(sol.interleaveCharacters("nkmklolooklnkomlmkkkkoknkmnkmonnmolnokklnmmklm", "kkooomoonnomlllkkmonlloomklkmlkonkmkon", "knkokmoklomoloooklonnomnllkomlmlkkkkkmonkoklnlk"))

print(sol.interleaveCharacters("wbaba","wba","wab"))



        