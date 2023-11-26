import requests
from bs4 import BeautifulSoup

def get_syllable_count(word):
    url = f"https://www.collinsdictionary.com/dictionary/english/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        syllables = soup.find('span', class_='SyllableCount')

        if syllables:
            return int(syllables.text)

    return None

def get_all_words():
    with open('collins_dictionary.txt', 'r') as f:
        words = f.read().splitlines()

    return words

def generate_word_syllable_list():
    words = get_all_words()
    word_syllable_list = []

    for word in words:
        syllable_count = get_syllable_count(word)

        if syllable_count is not None:
            word_syllable_list.append((word, syllable_count))

    return word_syllable_list

if __name__ == '__main__':
    word_syllable_list = generate_word_syllable_list()
    print(word_syllable_list)
