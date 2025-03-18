# treap.py

class TreapNode:
    def __init__(self, word):
        self.word = word
        self.priority = 1  # Frequency-based priority
        self.left = None
        self.right = None


def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x


def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y


def rebalance(root):
    if root.left and root.left.priority > root.priority:
        return rotate_right(root)
    if root.right and root.right.priority > root.priority:
        return rotate_left(root)
    return root


def insert(root, word):
    if root is None:
        return TreapNode(word)

    if word < root.word:
        root.left = insert(root.left, word)
        root = rebalance(root)
    elif word > root.word:
        root.right = insert(root.right, word)
        root = rebalance(root)
    else:
        # Word already exists → increase priority
        root.priority += 1
        root = rebalance(root)

    return root


def search_and_update(root, word):
    if root is None:
        return root, False

    if word == root.word:
        root.priority += 1
        root = rebalance(root)
        return root, True

    if word < root.word:
        root.left, found = search_and_update(root.left, word)
        root = rebalance(root)
        return root, found

    root.right, found = search_and_update(root.right, word)
    root = rebalance(root)
    return root, found


def autocomplete_helper(root, prefix, suggestions, limit=5):
    if root is None:
        return

    if len(suggestions) >= limit:
        return

    # Explore left subtree
    autocomplete_helper(root.left, prefix, suggestions, limit)

    # Check current word
    if root.word.startswith(prefix):
        suggestions.append((root.word, root.priority))

    # Explore right subtree
    autocomplete_helper(root.right, prefix, suggestions, limit)


def get_autocomplete(root, prefix, limit=5):
    suggestions = []
    autocomplete_helper(root, prefix, suggestions, limit * 5)  # Get more to sort by priority
    suggestions.sort(key=lambda x: (-x[1], x[0]))  # Sort by priority DESC, then word ASC
    return [word for word, _ in suggestions[:limit]]


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [(root.word, root.priority)] + inorder(root.right)
