from binary_tree import Node


def order(root):
    if root:
        order(root.left)
        print(root.val)
        order(root.right)


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root, key):
    if root == None or root.val == key:
        return root

    if root.val < key:
        return str(search(root.right, key))+" from right side"

    return str(search(root.left, key))+" from left side"


r = Node(40)

r = insert(r, 80)
r = insert(r, 30)
r = insert(r, 90)
r = insert(r, 120)
r = insert(r, 240)

order(r)

print(r)

print(search(r, 120))
