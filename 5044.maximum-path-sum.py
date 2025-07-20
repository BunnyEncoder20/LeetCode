# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        def recursive(node):
            nonlocal maximumPathSum
            # base case
            if not node: return 0

            lst = recursive(node.left)
            rst = recursive(node.right)

            maximumPathSum = max(maximumPathSum, node.val+lst+rst)
            return node.val + max(lst, rst)

        maximumPathSum = float('-inf')
        recursive(root)
        return maximumPathSum


# Test cases
def test_maxPathSum():
    solution = Solution()
    
    # Test case 1: Simple tree [1,2,3]
    #       1
    #      / \
    #     2   3
    # Expected: 6 (2 + 1 + 3)
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    assert solution.maxPathSum(root1) == 6
    print("Test case 1 passed: [1,2,3] -> 6")
    
    # Test case 2: Tree with negative values [-10,9,20,null,null,15,7]
    #        -10
    #       /   \
    #      9     20
    #           /  \
    #          15   7
    # Expected: 42 (15 + 20 + 7)
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    assert solution.maxPathSum(root2) == 42
    print("Test case 2 passed: [-10,9,20,null,null,15,7] -> 42")
    
    # Test case 3: Single node with negative value [-3]
    # Expected: -3
    root3 = TreeNode(-3)
    assert solution.maxPathSum(root3) == -3
    print("Test case 3 passed: [-3] -> -3")
    
    # Test case 4: Tree with all negative values [-2,-1]
    #     -2
    #    /
    #   -1
    # Expected: -1
    root4 = TreeNode(-2)
    root4.left = TreeNode(-1)
    assert solution.maxPathSum(root4) == -1
    print("Test case 4 passed: [-2,-1] -> -1")
    
    # Test case 5: Larger tree [5,4,8,11,null,13,4,7,2,null,null,null,1]
    #         5
    #       /   \
    #      4     8
    #     /     / \
    #    11    13  4
    #   / \         \
    #  7   2         1
    # Expected: 48 (7 + 11 + 4 + 5 + 8 + 13)
    root5 = TreeNode(5)
    root5.left = TreeNode(4)
    root5.right = TreeNode(8)
    root5.left.left = TreeNode(11)
    root5.left.left.left = TreeNode(7)
    root5.left.left.right = TreeNode(2)
    root5.right.left = TreeNode(13)
    root5.right.right = TreeNode(4)
    root5.right.right.right = TreeNode(1)
    assert solution.maxPathSum(root5) == 48
    print("Test case 5 passed: complex tree -> 48")
    
    # Test case 6: Single node with positive value [1]
    # Expected: 1
    root6 = TreeNode(1)
    assert solution.maxPathSum(root6) == 1
    print("Test case 6 passed: [1] -> 1")
    
    print("\nAll test cases passed! ✅")


if __name__ == "__main__":
    test_maxPathSum()
