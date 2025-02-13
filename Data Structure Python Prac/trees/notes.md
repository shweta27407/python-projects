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

# Binary Search Tree

Important Terms : key, key-value pair, item, node
All BSTs should contain 

node k in BST : all nodes in k's left subtree < k ,,, all nodes in k's right subtree > k

>[!Note]
>As the number of elements in the tree increases, the height does not increase linearly, but rather in proportion to O(log n).
> Height is in O(log n)
> Binary Trees cand egenerate into 𝑂(𝑛) runtime complexity
> 3
>    \
>     9
>      \
>      17
>        \
>         18
>           \
>            19
>              \
>               23 



Search Insert Delete Operations Pseudo Code

#### Height Balance Property 
bal(T) = h(Tright) - h(Tleft)

## BST :Efficiency

| Operation         | Best Case | Average Case | Worst Case |
|------------------|----------|-------------|------------|
| search(key)      | O(1)     | O(h)        | O(h)       |
| insert(key, item)| O(1)     | O(h)        | O(h)       |
| delete(key)      | O(1)     | O(h)        | O(h)       |

## AVL Trees / Adelson Velsky Landis
- it is a BST
- for each internal node, the balance of the subtree rooted at is either 0, -1 or +1

## 2-3-4 Trees
- each internal node has at least two children (called as d-nodes)
- each node contains d-1 data items of form (key, value)
- the keys form a search tree

### 2-3-4 Efficiency

| Operation         | Best Case | Average Case | Worst Case |
|------------------|----------|-------------|------------|
| search(key)      | O(1)     | O(log n)        | O(log n)       |
| insert(key, item)| O(1)     | O(log n)        | O(log n)       |
| delete(key)      | O(1)     | O(log n)        | O(log n)       |

Implementing 234 trees require lot of edge case handling, three separate node classes

## Red-Black Trees
- Red Black tree represent 2-3-4 tree by means of binary tree whose nodes are colored either red or black
- have simpler implementation compared to 2-3-4 trees



