class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max(root):
    if root is None:
        return None
    
    current = root
    while current.right is not None:
        current = current.right
    
    return current.val

# Створення двійкового дерева пошуку
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

# Знаходження найбільшого значення в дереві
max_value = find_max(root)
print("Найбільше значення в двійковому дереві пошуку:", max_value)
