# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from collections import deque
def level_order_traversal(root):
    # trivial case
    if not root: return []

    ans = []
    q = deque([root])
    while q:
        node = q.popleft()
        ans.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ans



from collections import deque
def level_order_traversal_group(root):
    # trivial case
    if not root: return []

    ans = []
    q = deque([root])

    while q:
        levelsize = len(q)
        level = []
        for _ in range(levelsize):
            node = q.popleft()
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
        
    return ans
