 # Count Words and Characters

def count_words_and_characters(text):
    # Initialize counters
    word_count = 0
    char_count = 0
    in_word = False

    for char in text:
        if not char.isspace():
            char_count += 1
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False

    return word_count, char_count

print(count_words_and_characters("sai machindra aher"))