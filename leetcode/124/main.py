# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left : "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ''' Returns the max path sum of the current subtree '''

        # Comecando de baixo para cima, eu pego um nodo folha.
        # a cada iteracao, eu subo 1 nó pra cima, e tenho que decidir pra esse nó superior
        # a melhor sequencia pra prosseguir pra cima
        # e a melhor sequencia global. 
        # melhor sequencia global, no caso, é apenas a melhor sequencia seq pra prosseguir
        # ou a sequencia que nao envolve nodos de cima, apenas as duas subarvores

        # max( open_ended_left + curr + open_ended_right, curr + open_ended_right, open_ended_left + curr

        # max path sum global = max (max path sum left, max path sum right, )
        # the function above seems correct? 

        # at each step i need to retun the global max sum so far and the best path i can pass next

        (max_path_sum, max_oe_path_sum) = self.maxOpenEndedPathSum(root)

        return max_path_sum


    def maxOpenEndedPathSum(self, root: TreeNode) -> tuple[int, int]:
        " Returns max open ended path and the max path sum of the current subtree "

        # print(root, root.val, root.left, root.right)

        if root.left == None:
            max_oe_left = -1001
            max_left = -1001
        else:
            (max_left, max_oe_left) = self.maxOpenEndedPathSum(root.left)


        if root.right == None:
            max_oe_right = -1001
            max_right = -1001
        else:
            (max_right, max_oe_right) = self.maxOpenEndedPathSum(root.right)


        max_oe_path_sum_local = max(root.val, root.val + max_oe_left, root.val + max_oe_right)

        max_path_sum_global = max(max_left, max_right, (root.val + max_oe_left + max_oe_right), max_oe_path_sum_local)

        #print(max_left, max_right, (root.val + max_oe_left + max_oe_right), max_oe_path_sum_local)

        #print(root, root.val, root.left, root.right)
        #print(max_oe_path_sum_local)
        #print(" ")


        return (max_path_sum_global, max_oe_path_sum_local)





sol = Solution()

print(sol.maxPathSum(TreeNode(-10,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))))