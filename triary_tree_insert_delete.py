class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""
    def __init__(self):
        self.root = None
        self.size = None

    # Please complete this method.
    """Inserts val into the tree. There is no need to rebalance the tree."""
    def insert(self, val):
        if self.root:
            self._insert(val,self.root)
        else:
            self.root = Node(val)
        if self.size == None:
            self.size = 1
        else:
            self.size = self.size + 1
    
    def _insert(self,val,cur_node):
        # find the correct node to insert the node
        # left check
        if val < cur_node.val:
            # check if left node exists
            if cur_node.left:
                self._insert(val,cur_node.left)
            else:
                cur_node.left = Node(val)
        # right check
        elif val > cur_node.val:
            if cur_node.right:
                self._insert(val,cur_node.right)
            else:
                cur_node.right = Node(val)
        # equal check
        elif val == cur_node.val:
            print "Mideel inser"
            cur_node.mid = Node(val)
        
    
    # Please complete this method.
    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""
    def delete(self, val):
        if self.root:
            self._delete(val,self.root)
        else:
            # nothing to delete
            pass
    
    def _delete(self,val,cur_node):
        if val == cur_node.val:
            # check for middle element
            if cur_node.mid and cur_node.mid.val == val:
                cur_node.mid = None
            else:
                if cur_node.right:
                    temp_node = self._findMin(cur_node.right)
                    cur_node.val = temp_node.val
                    cur_node.mid = temp_node.mid
                else:
                    # make left sub tree as head
                    cur_node = cur_node.left
        # traversal cases
        elif val < cur_node.val:
            if cur_node.left:
                self._delete(val,cur_node.left)
        elif val > cur_node.val:
            if cur_node.right:
                self._delete(val,cur_node.right)
    
    def _findMin(self,cur_node):
        # go to the leftmost value
        if cur_node.left:
            return self._findMin(cur_node.left)
        else:
            return cur_node
