Trees are recursive data structures. 
 - Each node in the tree is root of smaller tree. These are Subtrees

Important variables : Path, Depth, Level, Height
Path = There is exactly one path connecting each node to the root node.
Depth = number of edges on the path from the node to the root.
Level = modes with same depth form a level (level 0, 1, and 2)
Height = number of levels (3)

# Binary Tree 
an ordered tree having following properties: 
    1. every node at most two children (that's why it's binary)
    2. each child labeled as right child or left child.
    3. left children precede right children

Proper binary tree = when every node has either 0 or 2 children
:seedling:


>[!Important]
> Each level can hold at most 2^n^ nodes
> Binary tree of geight h contains atleast h nodes
> Binary tree of hight h contains atmost 2^^ - 1 nodes

>[!Note]
> Binary tree supports following operations: 
> get_root(), set_left(tree), get_left(), set_right(tree), get_right()
> Code 


## Tree Traversal 

1. Preorder Traversal : 
- visit root N, 
- recursive preorder Trav of N's left child, 
- recusrsive preorder trav of N's right child

2. Inorder Traversal: 
- recursive inorder Trav of N's left child
- visit root N
- recursive inorder Trav of right child

3. Postorder Traversal 
- recursive postorder trav of N's left child
- recursive postorder trav of N's right child
- visit root N
4. Levelorder Traversal

- top to bottom , left to right, one level at a time
>[!TIP]
> Check pseudocode of LevelOrder

# Bnary Search Tree

Important Terms : key, key-value pair, item, node
All BSTs should contain 

node k in BST : all nodes in k's left subtree < k ,,, all nodes in k's right subtree > k

Search Insert Delete Operations Pseudo Code

## BST :Efficiency

| Operation         | Best Case | Average Case | Worst Case |
|------------------|----------|-------------|------------|
| search(key)      | O(1)     | O(h)        | O(h)       |
| insert(key, item)| O(1)     | O(h)        | O(h)       |
| delete(key)      | O(1)     | O(h)        | O(h)       |

