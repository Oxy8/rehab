
from functools import cache

class Solution(object):

    def interleaveCharacters(self, word1, word2, target):
        return (self.interleaveCharactersInner(word1, word2, target, False, False) % 1000000007)
    
    @cache
    def interleaveCharactersInner(self, word1, word2, target, word1_used, word2_used):
        """
        :type word1: str
        :type word2: str
        :type target: str
        :rtype: int
        """

        # i believe i can take a similar approach to the edit distance problem.
        # i can just treat the problem as a tree expansion and use memoization to avoid recomputing every subtree.
        # migrating to a table based approach is what will be the most interesting part it seems.

        # the tree expands even less, cause i only have 2 options, i cant use any random letter.
        # at the same time, the tree probably has less repetition and cant be cached as much.

        if len(target) == 0:
            if word1_used and word2_used:
                return 1
            else:
                return 0
                
            # I am missing  having to use at least one letter of each word. this fucks things up actually.

            # In order to detect if at least one char of each word was used, i can check the loops. if either loop was never navigated
            # that means that no word was used either.

        sum_word_1 = 0
        
        if len(word1) != 0:
            
            for pos in range(len(word1)):
                if word1[pos] == target[0]:
                    sum_word_1 += self.interleaveCharactersInner(word1[(pos+1):],word2,target[1:], True, word2_used)

        sum_word_2 = 0
        
        if len(word2) != 0: 
            for pos in range(len(word2)):
                if word2[pos] == target[0]:                  
                    sum_word_2 += self.interleaveCharactersInner(word1,word2[(pos+1):],target[1:], word1_used, True)                    
                    

        return (sum_word_1 + sum_word_2)


sol= Solution()
#print(sol.interleaveCharacters("abc", "bac", "abc"))
#print(sol.interleaveCharacters("cd", "cd", "ccd"))
#print(sol.interleaveCharacters("xy", "xy", "xyxy"))
#print(sol.interleaveCharacters("ab", "cde", "ace"))
#print(sol.interleaveCharacters("g", "jfgg", "jgfgg"))
#print(sol.interleaveCharacters("m", "mlklo", "mlk"))

print(sol.interleaveCharacters("nkmklolooklnkomlmkkkkoknkmnkmonnmolnokklnmmklm", "kkooomoonnomlllkkmonlloomklkmlkonkmkon", "knkokmoklomoloooklonnomnllkomlmlkkkkkmonkoklnlk"))




        