letter_scores = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}

def get_word_score(word, multiplier=1):
    # the final score
    score = 0

    # convert to lowercase
    word = word.lower()

    # get the score for each character
    for character in word:
        # if the character is invalid, check the next character
        if character not in letter_scores:
            continue
        
        # only if the character is valid will we add on the current letter score
        score += letter_scores[character]
    
    return score * multiplier


# get all of the scores and print them out (the print bit was not really required)
print(f'The word score for the word "Jason" with multipler 1 = {get_word_score('Jason')}')
print(f'The word score for the word "Timmy" with multipler 2 = {get_word_score('Timmy', 2)}')
print(f'The word score for the word "Bob and James" with multipler 5 = {get_word_score('Bob and James', 5)}')