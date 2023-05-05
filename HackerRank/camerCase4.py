#!/bin/python3
import sys


def findUpperCase(word):
    """
    Function that determines the positions of UpperCase
    letters in a word
    """
    upperCasePositions = []
    for letter in range(0, len(word)):
        if word[letter].isupper():
            upperCasePositions.append(letter)
    return upperCasePositions

# Reading multiline input from user
inputs = sys.stdin.read()
# Storing the read inputs (which are in string form) into a list
inputs_list = inputs.split('\r\n')

for index in range(0, len(inputs_list)):
    # Getting inputs from the list
    string = inputs_list[index]
    operation = string[0]
    var = string[2]
    title = string[4:]

    # Case for split
    if operation == 'S':
        upperCasePositions = findUpperCase(title)
        splitWords = []
        
        if var == 'C':
            for pos in range(0, len(upperCasePositions)):
                if pos == len(upperCasePositions) - 1:
                    splitWords.append(title[upperCasePositions[pos]:].lower())
                else:
                    splitWords.append(title[upperCasePositions[pos]:upperCasePositions[pos+1]].lower()+" ")
        elif var == 'V':
            for pos in range(0, len(upperCasePositions)):
                if pos == 0:
                    splitWords.append(title[:upperCasePositions[pos]].lower()+" ")
                else:
                    splitWords.append(title[upperCasePositions[pos - 1]:upperCasePositions[pos]].lower()+" ")
                if pos == len(upperCasePositions) - 1:
                    splitWords.append(title[upperCasePositions[pos]:].lower())
        elif var == 'M':
            for pos in range(0, len(upperCasePositions)):
                if pos == 0:
                    splitWords.append(title[:upperCasePositions[pos]].lower()+" ")
                else:
                    splitWords.append(title[upperCasePositions[pos - 1]:upperCasePositions[pos]].lower()+" ")
                if pos == len(upperCasePositions) - 1:
                    splitWords.append(title[upperCasePositions[pos]:-2].lower())
        
        transformed = ""
        for word in splitWords:
            transformed += word
        print(transformed)

        
    # Case for combine
    if operation == 'C':
        words = title.split()
        newWords = []
        if var == 'C':
            for word in words:
                newWord = word[0].upper() + word[1:]
                newWords.append(newWord)
        elif var == 'M':
            newWords.append(words[0])
            for index in range(0, len(words)):
                newWord = words[index][0].upper() + words[index][1:]
                newWords.append(newWord)
            newWords.pop(1)
            newWord = newWords[-1] + '()'
            newWords.pop(-1)
            newWords.append(newWord)
        elif var == 'V':
            newWords.append(words[0])
            for index in range(0, len(words)):
                newWord = words[index][0].upper() + words[index][1:]
                newWords.append(newWord)
            newWords.pop(1)

        transformed = ""
        for word in newWords:
            transformed += word
        print(transformed)      
"""
S;M;plasticCup()    =   plastic cup

C;V;mobile phone = mobilePhone

C;C;coffee machine = CoffeeMachine

S;C;LargeSoftwareBook   =   large software book

C;M;white sheet of paper = whiteSheetOfPaper()

S;V;pictureFrame    =   picture frame

"""


