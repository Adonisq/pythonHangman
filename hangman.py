from os import system

word = input("give a word to guess: ").upper()
wordWithoutSpaces = word.replace(" ", "")
guessedWords = []
counter = 5

def printWord():

    for i in range(len(word)):
        if word[i] in guessedWords: print(" " + word[i] + " ", end='') # print guessed letters if they exists
        elif word[i] == ' ': print(' ', end='')
        else:
            print(" _ ", end='') # if word[i] is not guessed, print _

def checkIfWin():

    wordNoDuplicates = list(dict.fromkeys(wordWithoutSpaces))

    if len(wordNoDuplicates) == len(guessedWords):
        return True

def verifyWord():

    if guessedWord not in guessedWords and guessedWord in wordWithoutSpaces:
        guessedWords.append(guessedWord)
        return True

    return False

while counter>0:

    print('\n')
    print("tries left: " + str(counter))
    printWord()
    print('\n')

    guessedWord = input('give a one letter of secret word: ').upper()

    if verifyWord() is not True:
        counter-=1

    #system('cls')

    if checkIfWin() is True:
        break


if checkIfWin() is True:
    print('you won! The full word is: ' + word)

else: print("you loose! The full word is: " + word)


