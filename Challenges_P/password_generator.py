
import random

word_file = "words.txt"
word_list = []

# file up the word_list
with open(word_file, "r") as words:
    for line in words:
        # remove white_space and make everything lowercase
        word = line.strip().title()

        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces


def generate_password():
    return (
        random.choice(word_list)
        + "_"
        + random.choice(word_list)
        + random.choice(word_list)
    )


############################ Better way #####################

# def generate_password():
#     return "".join(random.sample(word_list, 3))


# test your function
print((generate_password()))
