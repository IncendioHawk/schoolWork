def getFile(path):
    with open(path, 'r') as file:
        return file.read()

def getWords():
    sentences = getFile('./data/sentences.txt')
    words = sentences.split(' ')
    return words

def getNumWords(words):
    return len(words)

def main():
    words = getWords()
    numWords = getNumWords(words)
    print(numWords)

def reverse(str):
    return str[::-1]

main()