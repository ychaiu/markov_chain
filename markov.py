"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path,"r")
    text_string = text.read()

    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string_list = text_string.rstrip().split()

    bigrams_list = []

    for i in range(len(text_string_list) - 1):
        bigram = (text_string_list[i], text_string_list[i+1])
        bigrams_list.append(bigram)

    # for bigram in bigrams_list:
    #     chains[bigram] = []

    for i in range(len(text_string_list)-2):
        if (text_string_list[i], text_string_list[i+1]) == bigrams_list[i]:
            following_word = text_string_list[i+2]
            chains[bigrams_list[i]].append(following_word)
            .get('key', []).append

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

print(type(open_and_read_file(input_path)))