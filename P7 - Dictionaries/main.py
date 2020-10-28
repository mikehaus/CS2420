"""
Main.py CS2420 Project 7
Mike Hollingshaus
"""
from hashmap import HashMap
from operator import itemgetter

def clean_line(raw_line):
    '''
    removes all punctuation from input string and
    returns a list of all words which have a length greater than one
    '''
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)): # pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z': 
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words

def main():
    """
    Main function
    """
    hashmap = HashMap()
    file = open('AliceInWonderland.txt', 'r')
    for line in file:
        text = clean_line(line)
        for word in text:
            hashmap.set(word)
    file.close()
    mylist = []
    for i in hashmap.dictionary:
        if i is not None:
            mylist.append(i)
    mylist.sort(key=lambda x: x[1], reverse=True)
    print('The most common words are:')
    for i in range(0, 15):
        index = mylist[i]
        print(index[0] + '       ' + str(index[1]))

main()
