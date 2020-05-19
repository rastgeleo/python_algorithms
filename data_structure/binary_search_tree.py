from collections import deque


class Node:
    """Binary node structure for BST"""
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:  # it's empty tree
            self.root_node = node
        else:                       # not empty tree
            current = self.root_node
            parent = None
            while True:
                parent = current    # trace parent
                if node.data < current.data:
                    # left child data is always smaller
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        print('Removing {}'.format(node.data))

        if parent is None and node is None:
            return False

        # get children count to deal with cases with different children
        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None

        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                # link child to the parent node on to
                # where the node to remove located
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                # node to remove is root node
                self.root_node = next_node

        else:
            # the node to remove have two children
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                # find the leftmost_node which is the successor
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data  # swap the data

            # leftmost_node is bound to have a right child only
            # relink child to the parent_of_leftmost_node as leftmost_node will
            # be garbage collected
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                # root is none or didn't find the matching data
                print('None found')
                return None
            elif current.data == data:
                print('found {}'.format(data))
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def inorder(self, root_node='root'):
        """In order traversal"""
        if root_node == 'root':
            current = self.root_node
        else:
            current = root_node

        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node='root'):
        if root_node == 'root':
            current = self.root_node
        else:
            current = root_node

        if current is None:
            return

        print(current.data)
        self.inorder(current.left_child)
        self.inorder(current.right_child)

    def postorder(self, root_node='root'):
        if root_node == 'root':
            current = self.root_node
        else:
            current = root_node

        if current is None:
            return

        self.inorder(current.left_child)
        self.inorder(current.right_child)
        print(current.data)

    def breadth_first_traversal(self):
        """
        breadth_traversal using queue structure
        """
        list_of_nodes = []  # list to return
        traversal_queue = deque([self.root_node])   # start from root_node
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)   # pop node and put data in result
            if node.left_child:     # if child, put it in the queue
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
        return list_of_nodes

    def get_node_with_parent(self, data):
        """Helper method to get node with its parent for deletion"""
        parent = None
        current = self.root_node
        if current is None:     # empty tree
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent, current)


tree = BST()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)
