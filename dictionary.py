import tkinter as tk
from PyDictionary import PyDictionary
from googletrans import Translator

# Function to look up words
def lookup_word():
    word = entry.get()
    
    # Check if the word is in English
    if dictionary.meaning(word):
        meaning = dictionary.meaning(word)
        meaning_text.config(text=meaning)
    else:
        # Translate English word to Sinhala
        translator = Translator()
        translation = translator.translate(word, src="en", dest="si")
        meaning_text.config(text=translation.text)

# Create the main window
root = tk.Tk()
root.title("Multi-Language Dictionary")
root.geometry("850x650")
root.configure(bg="black")

# Create a Dark GUI
root.tk_setPalette(background='black', foreground='white')

# Create an entry field
entry = tk.Entry(root, font=("Arial", 16), bg="gray", fg="black")
entry.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Create a button to look up words
search_button = tk.Button(root, text="Search", command=lookup_word, font=("Arial", 16))
search_button.pack(pady=10)

# Create a label to display word meanings
meaning_text = tk.Label(root, text="", font=("Arial", 14), wraplength=380, justify=tk.LEFT, bg="black", fg="white")
meaning_text.pack(pady=30, padx=30, fill=tk.BOTH, expand=True)

# Initialize the English dictionary
dictionary = PyDictionary()

# Run the GUI application
root.mainloop()