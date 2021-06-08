class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.route = []

    def add(self, value):
        self.root = self._add(self.root, value)
    
    def _add(self, node, value):
        if node is None:
            return Node(value)
        if value <= node.value:
            node.left = self._add(node.left, value)
        else:
            node.right = self._add(node.right, value)
        return node

    def inorder(self):
        self.route = []
        self._inorder(self.root)
        return self.route

    def _inorder(self, node):
        if node:
            if self._inorder(node.left):
                return True
            self.route.append(node.value)
            if self._inorder(node.right):
                return True
        return False
    
    def preorder(self):
        self.route = []
        self._preorder(self.root)
        return self.route

    def _preorder(self, node):
        if node:
            self.route.append(node.value)
            if self._preorder(node.left):
                return True
            if self._preorder(node.right):
                return True
        return False
    
    def posorder(self):
        self.route = []
        self._posorder(self.root)
        return self.route

    def _posorder(self, node):
        if node:
            if self._posorder(node.left):
                return True
            if self._posorder(node.right):
                return True
            self.route.append(node.value)
        return False
