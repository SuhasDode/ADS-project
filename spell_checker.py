# spell_checker.py

from treap import insert, search_and_update, get_autocomplete, inorder
from persistence import save_treap_to_file, load_treap_from_file

class SpellChecker:
    def __init__(self, save_file="treap_data.json"):
        self.save_file = save_file
        self.root = load_treap_from_file(self.save_file)

    def load_words(self, word_list):
        for word in word_list:
            word = word.strip().lower()
            self.root = insert(self.root, word)
        self.save()

    def check_word(self, word):
        word = word.lower()
        self.root, found = search_and_update(self.root, word)
        self.save()
        return found

    def suggest(self, prefix, limit=5):
        prefix = prefix.lower()
        return get_autocomplete(self.root, prefix, limit)

    def display_dictionary(self):
        entries = inorder(self.root)
        for word, freq in entries:
            print(f"{word} (used {freq} times)")

    def save(self):
        save_treap_to_file(self.root, self.save_file)
