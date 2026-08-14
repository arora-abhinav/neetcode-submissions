# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "None"
        string = ""
        def dfs(root):
            nonlocal string
            if not root:
                string += "N,"
                return 
            string += str(root.val)+","
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        string = string[:-1]
        print(string)
        return string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "None":
            return None
        nums = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if i > len(nums) - 1:
                return root
            if nums[i] == "N":
                i += 1
                return None 
            root = TreeNode(int(nums[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
        
            
