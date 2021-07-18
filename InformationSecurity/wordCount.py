import operator
from collections import Counter, OrderedDict
import pathlib

file_name = "livro.txt"
path = str(pathlib.Path().resolve()) + "/"
#path = str(pathlib.Path().resolve()) + "/InformationSecurity/"
def start(file_name):
    word_count = {}
    file = open(path + file_name)
    lines = file.read().splitlines()
    line = lines[2]
    for line in lines:
        wordList = word_list(line)
        clean_list = clean_wordlist(wordList)
        line_count = create_dictionary(clean_list)
        word_count = dict(Counter(word_count) + Counter(line_count))
    print(word_count)
    ordered = OrderedDict(word_count)
    print(ordered)
    ordered_count = Counter(ordered).most_common()
    print(ordered_count)
    save_list('word_count_list.txt', ordered_count)
    top = Counter(word_count).most_common(10)
    print(top)
    save_list('top_word_count_list.txt', top)

    
def save_list(file_name, list):
    file1 = path + file_name
    with open(file1, 'w') as file:
        file.write(str(list.pop(0))+'\n')
        file.close()
    with open(file1, 'a') as file:
        for item in list:            
            file.write(str(item)+'\n')
        file.close()
        
def word_list(text):
    wordList = []
    words = text.lower().split()
    for each_word in words:
        wordList.append(each_word)
    return wordList

def clean_wordlist(wordlist):
    clean_list = [] 
    for word in wordlist:
        symbols = '!@#$%^&*()_+=-{}|:¨;´<>?,./'

        for i in range(0,len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    return clean_list
    

def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return Counter(word_count)

if __name__ == '__main__':
    start('livro.txt')
