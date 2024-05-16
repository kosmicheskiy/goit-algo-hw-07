class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_of_values(root):
    if root is None:
        return 0
    
    stack = []
    current = root
    total_sum = 0

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            total_sum += current.val
            current = current.right
        else:
            break
    
    return total_sum

# Створення двійкового дерева пошуку
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

# Знаходження суми всіх значень в дереві
total_sum = sum_of_values(root)
print("Сума всіх значень в двійковому дереві пошуку:", total_sum)
