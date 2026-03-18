# Task
"""Write a function word_frequency(text) that takes a string, splits it into words, and returns a
dict with {word: count}.
Then: load a paragraph of text (hardcode something a few sentences long), call your
function, and print the top 5 most common words.
Ignore punctuation. Lowercase everything before counting. Use sorted() with a key."""



def word_frequency(text):
    text_into_words = text.lower().split()
    words_count = [{word:text_into_words.count(word)} for word in set(text_into_words)]
    return words_count
user_input = """
    Write a function word_frequency(text) that takes a string, splits it into words, and returns a
    dict with {word: count}.
    Then: load a paragraph of text (hardcode something a few sentences long), call your
    function, and print the top 5 most common words.
    Ignore punctuation. Lowercase everything before counting. Use sorted() with a key.
    """

word_freq = word_frequency(user_input)
print(word_freq)

