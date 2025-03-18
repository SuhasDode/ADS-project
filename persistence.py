# persistence.py

import json
from treap import TreapNode

def treap_to_dict(node):
    if node is None:
        return None
    return {
        'word': node.word,
        'priority': node.priority,
        'left': treap_to_dict(node.left),
        'right': treap_to_dict(node.right)
    }

def dict_to_treap(data):
    if data is None:
        return None
    node = TreapNode(data['word'])
    node.priority = data['priority']
    node.left = dict_to_treap(data['left'])
    node.right = dict_to_treap(data['right'])
    return node

def save_treap_to_file(root, filename="treap_data.json"):
    with open(filename, 'w') as f:
        json.dump(treap_to_dict(root), f, indent=4)

def load_treap_from_file(filename="treap_data.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return dict_to_treap(data)
    except FileNotFoundError:
        print(f"No save file found ({filename}). Starting fresh!")
        return None
