class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # -------------------------------------------

    def __str__(self):
        return str(self.key)


# -----------------------------------------------


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ===========================================
    # Modification Methods
    # --------------------

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    # -------------------------------------------

    def insert(self, key):
        self.root = self._insert(self.root, key)

    # -------------------------------------------

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    # -------------------------------------------

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    # -------------------------------------------

    def delete(self, key):
        self.root = self._delete(self.root, key)

    # ===========================================
    # Search & Query Methods
    # ----------------------

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # -------------------------------------------

    def search(self, key):
        return self._search(self.root, key)

    # -------------------------------------------

    def _contains(self, node, key):
        if not node:
            return False

        if node.key == key:
            return True
        elif key < node.key:
            return self._contains(node.left, key)
        else:
            return self._contains(node.right, key)

    # -------------------------------------------

    def contains(self, key):
        return self._contains(self.root, key)

    # ===========================================
    # Traversal Methods
    # -----------------

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    # -------------------------------------------

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    # -------------------------------------------

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    # -------------------------------------------

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    # -------------------------------------------

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.key)

    # -------------------------------------------

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    # ===========================================
    # Tree Information Methods
    # ------------------------

    def _get_size(self, node):
        if not node:
            return 0
        return 1 + self._get_size(node.left) + self._get_size(node.right)

    # -------------------------------------------

    @property
    def size(self):
        return self._get_size(self.root)

    # -------------------------------------------

    def _get_height(self, node):
        if not node:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    # -------------------------------------------

    @property
    def height(self):
        return self._get_height(self.root)

    # -------------------------------------------

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node.key

    # -------------------------------------------

    @property
    def max(self):
        return self._find_max(self.root)

    # -------------------------------------------

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.key

    # -------------------------------------------

    @property
    def min(self):
        return self._find_min(self.root)

    # -------------------------------------------


# -----------------------------------------------


# 1. Initialization and Insertion
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)


# 2. Test Tree Information Methods
print("--- Initial Tree State ---")
print(f"Size of the tree: {bst.size}")
print(f"Height of the tree: {bst.height}")
print(f"Minimum value: {bst.min}")
print(f"Maximum value: {bst.max}")

print("-" * 20)

# 3. Test Traversal Methods
print(f"In-order Traversal: {bst.inorder_traversal()}")
print(f"Pre-order Traversal: {bst.preorder_traversal()}")
print(f"Post-order Traversal: {bst.postorder_traversal()}")

print("-" * 20)

# 4. Test Search & Query Methods
print(f"Contains {40}? {bst.contains(40)}")
print(f"Searching for node {40}: {bst.search(40)}")
print(f"Searching for node {100}: {bst.search(100)}")

print("-" * 20)

# 5. Test Deletion
print("\n--- Deleting Node 40 ---")
bst.delete(40)

# 6. Re-test everything to see the changes
print("\n--- Final Tree State ---")
print(f"Size of the tree after deletion: {bst.size}")
print(f"Height of the tree after deletion: {bst.height}")
print(f"In-order Traversal after deletion: {bst.inorder_traversal()}")
print(f"Contains {40} after deletion? {bst.contains(40)}")
