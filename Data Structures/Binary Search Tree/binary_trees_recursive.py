#! python3
"""
This is a recursively built BST found at https://www.section.io/engineering-education/implementing-binary-search-tree-using-python/
"""
class Tree:
    ISLEAF = {True: " (leaf)",
              False: ""}
    # tree is a tree of trees, each node is an individual tree
    def __init__(self, key=None, parent=None):  # function to insert data to our binary tree
        self.left = None  # setting leftchild of the tree to add items
        self.right = None  # setting rightchild of the tree to add items
        self.key = key
        self.parent = parent

    def __eq__(self, comp):
        return self.key == comp
    
    def __lt__(self, comp):
        return self.key < comp
    def __gt__(self, comp):
        return self.key > comp
    
    def show_hierarchy(self, level=0):
        ret = " . "*level+repr(self.key) + Tree.ISLEAF[self.isleaf] + "\n"
        children = list(item for item in (self.left, self.right) if item is not None)
        for child in children:
            ret += child.show_hierarchy(level+1)
        return ret

    def add(self, value):
        if self.key is None:
            self.key = value

        elif self.key == value:
            return
        
        # if there is no left child, create a Tree object there
        # if there is, recurse until there isn't
        elif self.key > value:
            if self.left:
                self.left.add(value)
            else:
                self.left = Tree(value, self)
        
        # if value greater than node key, set right child
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Tree(value, self)
    
    # Used to add a tree to a tree
    def add_tree(self, tree):
        if type(tree) != Tree:
            raise ValueError("'tree' arg must be of type Tree")
        
        if tree is not None:
            if tree.left:
                self.add_tree(tree.left)
            if tree.right:
                self.add_tree(tree.right)
            
            self.add(tree.key)
        
    def delete_node(self, val):
        if self is None:
            return self
        
        # Traverse to left
        if val < self.key:
            self.left = self.left.delete_node(val)
        
        # Traverse to right
        elif val > self.key:
            self.right = self.right.delete_node(val)

        # Found, delete node with three different cases
        else:
            # Node with one or no children
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
        
            # Node with two children
            temp = self.right.get_min()

            self.key = temp.key

            self.right = self.right.delete_node(temp.key)
        
        return self

    def search(self, value):
        if value == self.key:
            return self
        
        if value < self.key:
            if not self.left:
                return False
            return self.left.search(value)
        
        if not self.right:
            return False
        return self.right.search(value)
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current
    
    def count(self):
        if not self:
            return 0
                
        else:
            if not self.left and self.right:
                return self.right.count() + 1
            elif self.left and not self.right:
                return self.left.count() + 1
            elif self.isleaf:
                return 1
            return self.left.count() + self.right.count() + 1

    """ 
    Uses of different traversal orders:
    Inorder     - Get items in ascending order
    Postorder   - Deleting items from tree
    Preorder    - Copying items / tree
    """
    # doesn't return anything, is itself a generator
    def inorder(self):
        if self is not None:
            if hasattr(self, "left") and self.left:
                yield from self.left.inorder()
            
            yield self

            if hasattr(self, "right") and self.right:
                yield from self.right.inorder()

    # Did this by accident, depending on when you yield, you get different order
    def postorder(self):
        if hasattr(self, "left") and self.left:
            yield from self.left.postorder()
        if hasattr(self, "right") and self.right:
            yield from self.right.postorder()

        yield self
    
    def preorder(self):
        yield self

        if hasattr(self, "left") and self.left:
            yield from self.left.preorder()
        if hasattr(self, "right") and self.right:
            yield from self.right.preorder()
    
    def get_leaf_nodes(self):
        if not self:
            return
        
        if self.isleaf:
            yield self
        
        if self.left:
            yield from self.left.get_leaf_nodes()
        
        if self.right:
            yield from self.right.get_leaf_nodes()
    
    def get_non_leaf(self):
        if not self:
            return
        
        if not self.isleaf:
            yield self
        
        if self.left:
            yield from self.left.get_non_leaf()
        if self.right:
            yield from self.right.get_non_leaf()
    
    def delete_tree(self):
        if self is not None:
            if self.isleaf:
                del self.parent
                return
            if self.left:
                self.left.delete_tree()
                del self.left
                
            if self.right:
                self.right.delete_tree()
                del self.right
            
            if not self.parent:
                self.key = None
                self.left = None
                self.right = None
                self.clear_node()

    @classmethod
    def from_iter(cls, *iter):
        output = Tree()
        for item in iter:
            output.add(item)
        return output
            
    @property
    def isleaf(self):
        return self.height == 0

    @property
    def height(self):
        if self.left is None and self.right is None:
            return 0
        
        else:
            if self.left is None:
                left_depth = 0
            else:
                left_depth = self.left.height
            if self.right is None:
                right_depth = 0
            else:
                right_depth = self.right.height

            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1

def delete_tree(root: Tree):
    if root is not None:
        delete_tree(root.left)
        delete_tree(root.right)

        for attr in root.__dict__.copy():
            setattr(root, attr, None)
