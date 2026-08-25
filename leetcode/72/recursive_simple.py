from functools import cache


class Solution(object):
    @cache
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # we can add a character, remove it or use.
        # There is the table based dynamic programming recipe, but what i want is a tree based approach so i can learn things properly, not just remember.
        # i want a recursive function which solves this shit..

        # The problem is the explosion of states which is clearly noticeable. We don't know if any of the letter can be used.
        # We can use memoization, or treat it as a graph to represent repetitive states.

        # is this what dynamic programming is about? is it just memoization as a table?
        # That is what is looks like to me. We have a recursive formula and we treat the formula + memoization via modelling in a table as the way to go.

        if len(word1) == 0 and len(word2) == 0:
            return 0
        
        if len(word1) == 0 and len(word2) != 0:
            return len(word2)

        if len(word1) != 0 and len(word2) == 0:
            return len(word1)

        if word1[0] == word2[0]:
            cost_edit = 0
        else:
            cost_edit = 1
    
        return min( 1 + (self.minDistance(word1[1:],word2)),
                    1 + (self.minDistance(word1,word2[1:])),
                    cost_edit + (self.minDistance(word1[1:],word2[1:])))
    

        


solution = Solution()
print(solution.minDistance("horse", "ros"))
print(solution.minDistance("intention", "execution"))