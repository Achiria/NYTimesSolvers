import json
import copy
from pdb import set_trace as bp

letterGroups = [["n","g","l"],["i","o","u"],["a","c","e"],["m","j","t"]] 

NUM_LETTERS = 12

def sortByWordLength(words):
    sortedWords = sorted(words, key=len)
    sortedWords.reverse()
    return sortedWords

def getUsedLetters(words):
    usedLetters = []
    for word in words:
        for letter in word:
            if letter not in usedLetters:
                usedLetters.append(letter)
    return usedLetters

def getGroup(letterGroups, letterToGet):
    for i in range(len(letterGroups)):
        for j in letterGroups[i]:
            if j == letterToGet:
                return i
            
def checkWord(word, checkLetters, letterGroups):
    for il in range(len(word)):
        if word[il] in checkLetters:
            if il < len(word) - 1:
                lGroup = getGroup(letterGroups, word[il])
                lNGroup = getGroup(letterGroups, word[il+1])
            if lGroup == lNGroup:
                return False
        else:
            return False
    return True

def checkNextWord(solution, nextWord):
    usedLetters = getUsedLetters(solution)
    if solution[-1][-1] == nextWord[0]:
        for letter in nextWord[1:]:
            if letter in usedLetters:
                return False
        return True
    return False   
    
def checkNextWordWithRepeats(solution, nextWord):
    if nextWord in solution:
        return False
    if solution[-1][-1] == nextWord[0]:
        return True
    return False   

        
def getNextWords(solution, wordSet, maxDepth):
    if len(solution) <= maxDepth:
        usedLetters = getUsedLetters(solution)
        if len(usedLetters) < NUM_LETTERS:
            hasValidNextWord = False
            for nextWord in wordSet:
                # if checkNextWord(solution, nextWord):
                if checkNextWordWithRepeats(solution, nextWord):
                    hasValidNextWord = True
                    newSolution = copy.deepcopy(solution)
                    newSolution.append(nextWord)
                    
                    getNextWords(newSolution, wordSet, maxDepth)
            if not hasValidNextWord:
                finalSolutions.append(solution)
        else:
            finalSolutions.append(solution)
        
def getEverySolution(wordSet, letters):
    maxDepth = 1
    haveCompleteSolution = False
    while not haveCompleteSolution:
        for word in wordSet:
            getNextWords([word], wordSet, maxDepth)
        for solution in finalSolutions:
            if checkCompleteness(solution, letters):
                haveCompleteSolution = True
        maxDepth += 1
    return  

def checkCompleteness(solution, letters):
    usedLetters = getUsedLetters(solution)
    for letter in letters:
        if letter not in usedLetters:
            return False
    return True      
        
finalSolutions = []
        
if __name__ == '__main__':
    file = open("../words_dictionary.json", "r")
    words = json.load(file)
    
    letters = ''
    for i in letterGroups:
        letters = letters + ''.join(str(v) for v in i)  
       
    wordSet = []
    for word in words:
        if len(word) > 2:                              
            valid = checkWord(word, letters, letterGroups)
            if valid:
                wordSet.append(word)
           
    # wordSet = sortByWordLength(wordSet)
    # print(wordSet)
    getEverySolution(wordSet, letters)
    
    shortestSolution = []
    shortestSolutionLength = 99999
    completeSolutions = []
    for solution in finalSolutions:
        solutionLength = 0
        usedLetters = getUsedLetters(solution)
        for word in solution:
            solutionLength += len(word)
            usedLetters.extend(word)
        if checkCompleteness(solution, letters):
            completeSolutions.append(solution)
            if solutionLength < shortestSolutionLength:
                shortestSolutionLength = solutionLength
                shortestSolution = [solution]
         
    print(str(len(finalSolutions)) + " solutions found.")
    print("Solutions: " + str(finalSolutions))
    print(str(len(completeSolutions)) + " complete solutions found.")
    print("Complete solutions: " + str(completeSolutions))
    print("Shortest solution: " + str(shortestSolution))
    

