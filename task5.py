def count_word_frequency(words):
    """
    Count the frequency of each unique word from a list of words.

    Args:
        words (list): A list of strings.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    # Create a set of unique words
    unique_words = set(words)

    # Initialize a dictionary with each unique word's count set to 0
    counts = {word: 0 for word in unique_words}

    # Iterate through the words and update their counts
    for word in words:
        if word in counts:
            counts[word] += 1

    return counts

# Example usage
words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
result = count_word_frequency(words)
print(result)
