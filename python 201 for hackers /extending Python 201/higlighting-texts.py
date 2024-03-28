def highlight_words(words, text):
    # ANSI escape code for color red
    start_highlight = '\033[91m'
    # ANSI escape code to reset color
    end_highlight = '\033[0m'
    # Iterate over each word in the list
    for word in words:
        # Replace all occurrences of the word with the highlighted version
        text = text.replace(word, start_highlight + word + end_highlight)
    return text

# Example usage
words_to_highlight = ["highlight", "bitch!!!!!!!"]
text = "This is a text to highlight the word highlight in Python. bitch!!!!!!!"

highlighted_text = highlight_words(words_to_highlight, text)
print(highlighted_text)
