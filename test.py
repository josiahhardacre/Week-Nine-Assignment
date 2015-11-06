def sortLetters(word):
    word = word.lower()
    listWord = list(word)
    listWord.sort()
    sortedLetters = ''.join(listWord)
    return 

def createDictionary(fileName, dictionary):
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        line =  line.strip()
        word = line.lower()
        if word[0] == 'v':
            sortedWord = sortLetters(word)
            dictionary[sortedWord] = word
    fileHandle.close()

def findAnagrams(fileName, aDict):
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        line = line.strip()
        quizword = line.lower()
        print(quizword, aDict[sortLetters(quizword)])
    fileHandle.close()

def main():
    aDict = {}
    filename = 'wordList.txt'
    quizListName = 'quizwords.txt'
    createDictionary(filename, aDict)
    findAnagrams(quizListName, aDict)
    
main()