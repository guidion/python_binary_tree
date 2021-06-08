from BinaryTree import BinaryTree

tree = BinaryTree()

tree.add('F')
tree.add('B')
tree.add('A')
tree.add('D')
tree.add('C')
tree.add('E')
tree.add('G')
tree.add('I')
tree.add('H')

print('Pre orden: ', ' '.join(tree.preorder()))
print('In  orden: ', ' '.join(tree.inorder()))
print('Pos orden: ', ' '.join(tree.posorder()))