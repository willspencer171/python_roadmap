from random import randint
from binary_trees_recursive import *

root = Tree()
adds = [randint(0, 50) for _ in range(15)]

for i in adds:
    root.add(i)

""" inorder = [str(item.key) for item in root.inorder()]
postorder = [str(item.key) for item in root.postorder()]
preorder = [str(item.key) for item in root.preorder()]

print(", ".join(inorder))
print(", ".join(postorder))
print(", ".join(preorder))

print(f"Expected Root: {root.key}")
print(f"Postorder Root: {postorder[-1]}")
print(f"Preorder Root: {preorder[0]}") """

""" root.delete_node(3)
print([item.key for item in root.inorder()]) """
print(root.show_hierarchy())
print("Height:", root.height)

""" print("Leaf nodes:")
print([item.key for item in root.get_leaf_nodes()])

print("Non Leaf nodes:")
print([item.key for item in root.get_non_leaf()])

print("are there any matches between lists?")
print(any([leaf.key == non.key for leaf, non
           in zip(root.get_non_leaf(), root.get_leaf_nodes())])) """

""" print("Count:")
print(root.count()) """

#delete_tree(root)
print([(item.key) for item in root.inorder()])
root.add(3)
print([(item.key) for item in root.inorder()])

new_root = Tree.from_iter(*[randint(50,100) for _ in range(20)])
new_root.add_tree(root)
print(new_root.show_hierarchy())
