"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # Store the value inside this node and set left and right child
        # pointers to None since a brand-new node starts with no children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # Initialize an empty Binary Search Tree by setting the root to None.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        """
             A BST keeps data organized by enforcing a strict ordering rule at every node.
             Values smaller than the current node always go to the left, and values
             larger than the current node always go to the right. This keeps the tree
             sorted so future searches know which direction to look.
             """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If empty spot reached, create and return the new node.
        if node is None:
            return Node(value)

        # If the new value is smaller, move down into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # If the new value is larger, move down into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the updated node reference back up the call stack.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        """
        Linear search checks items one by one from start to finish (O(n)).
        Each comparison lets us eliminate half of the remaining tree—just 
        like looking up a word in a dictionary.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If the value is not in the tree, return false
        if node is None:
            return False

        # If the value is found, return True
        if value == node.value:
            return True

        # Search left if target is smaller, or right if larger.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        #Return a list containing the values from an in-order traversal.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        """
        Because every node to the left is smaller than the current node, and
        every node to the right is larger, visiting the entire left subtree
        first, recording the current node second, and visiting the right subtree
        last.
        """
        if node is not None:
            # 1. Visit the left subtree
            self._inorder_recursive(node.left, values)
            # 2. Visit the current node
            values.append(node.value)
            # 3. Visit the right subtree
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    # Insert each value into the tree.
    # Because 50 is inserted first, it becomes the root. Values like 30, 20,
    # and 40 go into the left subtree, while 70, 60, and 80 go to the right.
    # At every step, comparing against a node cuts away the opposite branch,
    # shrinking the remaining search space immediately.
    for value in values_to_insert:
        tree.insert(value)
    print(f"Inserted values: {values_to_insert}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits Left -> Root -> Right.
    # Since smaller values sit on the left and larger ones on the right,
    # this prints the values in ascending sorted order.
    sorted_values = tree.inorder()
    print(f"In-order traversal (sorted): {sorted_values}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Test two existing values (40 and 80) and two missing values (25 and 99).
    # For 40: checks 50 (goes left) -> checks 30 (goes right) -> finds 40 (True).
    # For 25: checks 50 (left) -> 30 (left) -> 20 (right) -> hits None (False).
    print(f"Search for 40 (exists): {tree.search(40)}")
    print(f"Search for 80 (exists): {tree.search(80)}")
    print(f"Search for 25 (missing): {tree.search(25)}")
    print(f"Search for 99 (missing): {tree.search(99)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Empty tree operations
    # Searching or traversing an empty tree safely returns False or an empty
    # list because the base cases check for `node is None` right away.
    empty_tree = BST()
    print(f"Empty tree traversal: {empty_tree.inorder()}")
    print(f"Empty tree search for 10: {empty_tree.search(10)}")

    # Inserting duplicate values
    # Inserting 50 again does not add a second 50 because `_insert_recursive`
    # only inserts when `value < node.value` or `value > node.value`.
    tree.insert(50)
    print(f"After inserting duplicate 50: {tree.inorder()}")

    # ===============================
    # 6. REAL-WORLD BST EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD EXAMPLE: STUDENT ID LOOKUP ===")

    # Scenario: A university registrar stores active Student IDs in a BST.
    # Using a BST allows quick verification of whether an ID is registered
    # and makes it easy to export a sorted roster of all student IDs.
    student_ids_bst = BST()
    registered_ids = [1045, 1012, 1089, 1003, 1027, 1064, 1095]

    for sid in registered_ids:
        student_ids_bst.insert(sid)

    print(f"Registered IDs (sorted roster): {student_ids_bst.inorder()}")
    print(f"Is Student ID 1027 active? {student_ids_bst.search(1027)}")
    print(f"Is Student ID 1050 active? {student_ids_bst.search(1050)}")


if __name__ == "__main__":
    main()