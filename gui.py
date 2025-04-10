import tkinter as tk
from tkinter import messagebox, simpledialog
from spell_checker import SpellChecker

class SpellCheckerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Treap Spell Checker & Autocomplete")
        self.master.geometry("500x400")

        self.checker = SpellChecker()

        # GUI Components
        self.label = tk.Label(master, text="Enter a word or prefix:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.check_btn = tk.Button(master, text="Check Word", command=self.check_word, width=20)
        self.check_btn.pack(pady=5)

        self.suggest_btn = tk.Button(master, text="Autocomplete", command=self.autocomplete, width=20)
        self.suggest_btn.pack(pady=5)

        self.load_btn = tk.Button(master, text="Load Dictionary", command=self.load_words, width=20)
        self.load_btn.pack(pady=5)

        self.load_btn = tk.Button(master, text="Display Dictionary", command=self.display, width=20)
        self.load_btn.pack(pady=5)

        self.output = tk.Text(master, height=10, width=50, font=("Arial", 12))
        self.output.pack(pady=10)

    def check_word(self):
        word = self.entry.get().strip()
        if not word:
            messagebox.showwarning("Input Error", "Please enter a word.")
            return
        found = self.checker.check_word(word)
        if found:
            self.output.insert(tk.END, f"'{word}' is correct! (priority increased)\n")
        else:
            suggestions = self.checker.suggest(word[:2])
            if suggestions:
                self.output.insert(tk.END, f"'{word}' not found. Suggestions: {suggestions}\n")
            else:
                self.output.insert(tk.END, f"'{word}' not found. No suggestions.\n")

    def autocomplete(self):
        prefix = self.entry.get().strip()
        if not prefix:
            messagebox.showwarning("Input Error", "Please enter a prefix.")
            return
        suggestions = self.checker.suggest(prefix)
        if suggestions:
            self.output.insert(tk.END, f"Suggestions for '{prefix}': {suggestions}\n")
        else:
            self.output.insert(tk.END, f"No suggestions found for '{prefix}'.\n")

    def load_words(self):
        file_path = simpledialog.askstring("Load Dictionary", "Enter dictionary file path (e.g., words.txt):")
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    word_list = f.readlines()
                    self.checker.load_words(word_list)
                    self.output.insert(tk.END, f"Loaded {len(word_list)} words from {file_path}\n")
            except FileNotFoundError:
                messagebox.showerror("File Error", f"File not found: {file_path}")

    def display(self):
        words = self.checker.display_dictionary()
        self.output.insert(tk.END,f"Dictionary - \n")
        for word ,prio in words:
            self.output.insert(tk.END,f"{word} - {prio}\n")

def run_gui():
    root = tk.Tk()
    app = SpellCheckerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
