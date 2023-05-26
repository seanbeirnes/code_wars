# Decodes a string of morese code into a readable string.
# Example: decode_morse('.... . -.--   .--- ..- -.. .') should return "HEY JUDE"
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    sentence = []
    for word in morse_code.split("   "):
        chars = word.split(" ")
        new_word = ""
        for char in chars:
            new_word += MORSE_CODE.get(char, "")
        sentence.append(new_word)
    return " ".join(sentence).strip()
