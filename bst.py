from node import Node


class BST:
    def __init__(self):
        self.root = None
        self.last_inserted = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.last_inserted = self.root
        else:
            self.last_inserted = self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data, parent=current)
                return current.left
            return self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data, parent=current)
                return current.right
            return self._insert_recursive(current.right, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data, parent=node)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data, parent=node)
            else:
                self._insert(node.right, data)

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right:
            new_root.right.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node
        node.parent = new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left:
            new_root.left.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root

    def dsw_balance(self):
        if self.root is None:
            return

        #Zbieranie węzłów w kolejności in-order
        spine = self._flatten_to_spine(self.root)

        #Budowanie zrównoważonego drzewa z listy węzłów
        self.root = self._build_balanced_tree(spine)

    def _inorder_collect(self, node, spine):
        if node is None:
            return
        self._inorder_collect(node.left, spine)
        spine.append(node)
        self._inorder_collect(node.right, spine)

    def _flatten_to_spine(self, node):
        spine = []
        self._inorder_collect(node, spine)
        return spine

    def _build_balanced_tree(self, spine):
        if not spine:
            return None
        mid = len(spine) // 2
        root = spine[mid]

        #Zbudowanie lewego i prawego poddrzewa
        root.left = self._build_balanced_tree(spine[:mid])
        root.right = self._build_balanced_tree(spine[mid + 1:])

        #Ustawienie rodziców dla dzieci
        if root.left:
            root.left.parent = root
        if root.right:
            root.right.parent = root

        return root

    def _update_parent(self, node):
        #Aktualizowanie rodzica dla każdego węzła
        if node:
            if node.left:
                node.left.parent = node
            if node.right:
                node.right.parent = node
            self._update_parent(node.left)
            self._update_parent(node.right)

    def _inorder_traversal(self, node, nodes):
        if node:
            self._inorder_traversal(node.left, nodes)
            nodes.append(node)
            self._inorder_traversal(node.right, nodes)

    def delete(self, data):
        node_to_delete = self._find(self.root, data)
        if node_to_delete:
            self._delete_node(node_to_delete)

    def _find(self, node, data):
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self._find(node.left, data)
        else:
            return self._find(node.right, data)

    def _delete_node(self, node):
        #Usuwanie węzła
        if node.left is None and node.right is None:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
        elif node.left is None:  #Węzeł ma tylko prawego potomka
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            else:
                self.root = node.right
            node.right.parent = node.parent
        elif node.right is None:  #Węzeł ma tylko lewego potomka
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                self.root = node.left
            node.left.parent = node.parent
        else:  #Węzeł ma dwóch potomków
            successor = self._min(node.right)
            node.data = successor.data
            self._delete_node(successor)

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def find(self, data):
        return self._find_recursive(self.root, data)

    def _find_recursive(self, current, data):
        if current is None or current.data == data:
            return current
        if data < current.data:
            return self._find_recursive(current.left, data)
        return self._find_recursive(current.right, data)

    def clear(self):
        self.root = None
        self.last_inserted = None

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def min_value(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.data if current else None

    def max_value(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.data if current else None
