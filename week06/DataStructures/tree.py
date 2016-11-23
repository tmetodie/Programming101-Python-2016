from collections import deque

class TreeNode:
    def __init__(self, value, children=None):
        if children is None:
            children = []

        self.value = value
        self.children = children

root = TreeNode(5, [TreeNode(4,
                            [TreeNode(2)]),
                           TreeNode(3)])

def concat(xs):
    result = []
    for x in xs:
        result.extend(x)

    return result

def walk(node):
    return [node.value] + concat([walk(child) for child in node.children])

# print(walk(root))
def add_child(root, parent_value, child_value):
    stop_recursion = False
    def inner_recursion(root, parent_value, child_value):
        nonlocal stop_recursion

        if stop_recursion:
            return

        if root.value == parent_value:
            root.children.append(TreeNode(child_value))
            stop_recursion = True
            return

        for child in root.children:
            inner_recursion(child, parent_value, child_value)

    inner_recursion(root, parent_value, child_value)
print(add_child(root, 5, 8))

def add_child_stack(root, parent_value, child_value):
    stack = deque()
    stack.append(root)

    while len(stack) != 0:
        current = stack.pop()

        if current.value == parent_value:
            current.children.append(TreeNode(child_value))
            return

        for child in current.children:
            stack.append(child)

class Tree:
    class TreeNode:
        def __init__(self, value, children=None):
            if children is None:
                children = []

            self.value = value
            self.children = children
            self.level = 0

    def __init__(self, root):
        self.__root = self.TreeNode(root)
        self.__size = 1

    def __find(self, value):
        stack = deque()
        stack.append(self.__root)

        while len(stack) != 0:
            current_node = stack.pop()

            if current_node.value == value:
                return current_node

            for child in current_node.children:
                stack.append(child)

    def __height(self, root):
        if not root.children:
            return 1

        return 1 + max([self.__height(child) for child in root.children])

    def height(self):
        return self.__height(self.__root) - 1

    def find(self, value):
        return self.__find(value)

    def add_child(self, parent, child):
        node = self.__find(parent)
        node.children.append(self.TreeNode(child))
        self.__size += 1

    def count_nodes(self):
        return self.__size

    def tree_levels(self):
        queue = deque()
        queue.append((0, self.__root))

        result = {}

        while len(queue) != 0:
            level, current_node = queue.popleft()

            if level not in result:
                result[level] = [current_node.value]
            else:
                result[level].append(current_node.value)

            for child in current_node.children:
                queue.append((level + 1, child))

        return result

def main():
    t = Tree(5)
    # print(t.find(5))
    t.add_child(5, 4)
    t.add_child(5, 8)
    t.add_child(4, 3)
    # print(t.find(4))
    # print(t.count_nodes())
    # print(t.height())
    print(t.tree_levels())
    # t.add_child(root_node, TreeNode(4))
    # t.add_child(TreeNode(4), TreeNode(2))


if __name__ == '__main__':
    main()
