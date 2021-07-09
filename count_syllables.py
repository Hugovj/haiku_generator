import json
from string import punctuation
from nltk.corpus import cmudict
from nltk.data import normalize_resource_name

with open('hoofdstuk_8_9\missing_words.json') as f:
    missing_words = json.load(f)

cmudict = cmudict.dict()

def count_syllables(words):
    """Use corpora to count syllables in English word or phrase."""
    # prep words for cmudict corpus
    words = words.replace('-', ' ')
    words = words.lower().split()
    num_syllables = 0
    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word in missing_words:
            num_syllables += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_syllables += 1
    return num_syllables

def main():
    while True:
        print("Syllable Counter")
        word = input("Enter word or phras; else press Enter to Exit: ")
        if word == '':
            quit()
        try:
            num_syllables = count_syllables(word)
            print(f"Number of syllables in {word} is: {num_syllables}")
        except KeyError:
            print("Word not found. Try again.\n")

if __name__ == '__main__':
    main()
