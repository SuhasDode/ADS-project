# main.py

from spell_checker import SpellChecker

def load_dictionary_from_file(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    checker = SpellChecker()

    # Load initial dictionary from file
    word_list = load_dictionary_from_file('./words.txt')
    checker.load_words(word_list)
    print(f"Loaded {len(word_list)} words into the dictionary!\n")

    while True:
        print("\n--- Spell Checker & Autocomplete ---")
        print("1. Check a word")
        print("2. Autocomplete suggestions")
        print("3. Show dictionary (word frequencies)")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            word = input("Enter word to check: ").strip()
            found = checker.check_word(word)
            if found:
                print(f"'{word}' is correct! (priority increased)")
            else:
                print(f"'{word}' not found.")
                suggestions = checker.suggest(word[:2])
                if suggestions:
                    print("Did you mean:", suggestions)
                else:
                    print("No suggestions available.")
        elif choice == '2':
            prefix = input("Enter prefix for autocomplete: ").strip()
            suggestions = checker.suggest(prefix)
            if suggestions:
                print("Suggestions:", suggestions)
            else:
                print("No suggestions found.")
        elif choice == '3':
            checker.display_dictionary()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
