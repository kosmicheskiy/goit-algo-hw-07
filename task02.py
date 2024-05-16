class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min(root):
    if root is None:
        return None
    
    current = root
    while current.left is not None:
        current = current.left
    
    return current.val

# Створення двійкового дерева пошуку
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

# Знаходження найменшого значення в дереві
min_value = find_min(root)
print("Найменше значення в двійковому дереві пошуку:", min_value)
