import nltk
from nltk.corpus import wordnet
import random
import tkinter as tk
from tkinter import filedialog, OptionMenu

# Create a function to handle the translation
def translate_sentence():
    sentence = input_text.get("1.0", tk.END).strip()  # Get the input sentence from the text widget
    words = nltk.word_tokenize(sentence)

    # Determine the synonym conversion level
    level = synonym_level.get()

    # Iterate over each word in the sentence
    for i, word in enumerate(words):
        # Get the Part-of-Speech (POS) tag for the word
        pos_tags = nltk.pos_tag([word])
        pos_tag = pos_tags[0][1]

        # Get synonyms for the word based on its POS tag
        synonyms = []
        for syn in wordnet.synsets(word, pos=wordnet.NOUN if pos_tag.startswith('N') else wordnet.VERB):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())

        # Replace the word with a random synonym based on the selected level
        if level == "normal" and synonyms:
            synonym = random.choice(synonyms)
            words[i] = synonym
        elif level == "posh" and synonyms:
            synonym = random.choice(synonyms)
            words[i] = synonym.upper()
        elif level == "sophisticated british woman" and synonyms:
            synonym = random.choice(synonyms)
            words[i] = synonym.title()

    # Join the modified words to form the translated sentence
    translated_sentence = ' '.join(words)
    output_text.delete("1.0", tk.END)  # Clear the output text widget
    output_text.insert(tk.END, translated_sentence)  # Insert the translated sentence

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, content)

# Create the GUI window
window = tk.Tk()
window.title("Sentence Translator")
window.configure(bg="black")  # Set the background color of the window

# Create the input text widget
input_label = tk.Label(window, text="Enter a sentence:", bg="black", fg="white", font=("Arial", 12))  # Set background, foreground color, and font style of the label
input_label.pack()
input_text = tk.Text(window, height=4, bg="black", fg="white", font=("Arial", 12))
input_text.pack()

# Create the synonym level dropdown menu
synonym_label = tk.Label(window, text="Synonym Conversion Level:", bg="black", fg="white", font=("Arial", 12))
synonym_label.pack()
synonym_levels = ["normal", "posh", "sophisticated british woman"]
synonym_level = tk.StringVar(window)
synonym_level.set(synonym_levels[0])  # Set the default level
synonym_dropdown = OptionMenu(window, synonym_level, *synonym_levels)
synonym_dropdown.pack()

# Create the translate button
translate_button = tk.Button(window, text="Translate", command=translate_sentence, font=("Arial", 12))
translate_button.pack()

# Create the output text widget
output_label = tk.Label(window, text="Translated sentence:", bg="black", fg="white", font=("Arial", 12))  # Set background, foreground color, and font style of the label
output_label.pack()
output_text = tk.Text(window, height=4, bg="black", fg="white", font=("Arial", 12))
output_text.pack()

# Create the open file button
open_file_button = tk.Button(window, text="Open File", command=open_file, font=("Arial", 12))
open_file_button.pack()

# Start the GUI event loop
window.mainloop()
