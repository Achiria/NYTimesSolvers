import json
import copy
from pdb import set_trace as bp

letterGroups = [["a","x","n"],["o","h","l"],["i","m","e"],["p","y","t"]] 
perfectLength = 6

NUM_LETTERS = 12

def sortByWordLength(words):
    sortedWords = sorted(words, key=len)
    sortedWords.reverse()
    return sortedWords

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

# def checkNextWord(solution, nextWord):
    # usedLetters = []
    # for word in solution:
        # usedLetters.extend(word)
    # if solution[-1][-1] == nextWord[0]:
        # for letter in nextWord[1:]:
            # if letter in usedLetters:
                # return False
        # return True
    # return False   
    
def checkNextWord(solution, nextWord):
    if nextWord in solution:
        return False
    if solution[-1][-1] == nextWord[0]:
        return True
    return False   
    
# def getNextWords(solution, wordSet):
    # hasValidNextWord = False
    # for nextWord in wordSet:
        # if checkNextWord(solution, nextWord):
            # hasValidNextWord = True
            # newSolution = []
            # newSolution.extend(solution)
            # newSolution.append(nextWord)
            
            # getNextWords(newSolution, wordSet)
    # if not hasValidNextWord:
        # finalSolutions.append(solution)
        
def getNextWords(solution, wordSet):
    print(solution)
    usedLetters = []
    for word in solution:
        for letter in word:
            if letter not in usedLetters:
                usedLetters.append(letter)
    print(usedLetters)
    if len(usedLetters) < NUM_LETTERS:
        hasValidNextWord = False
        for nextWord in wordSet:
            if checkNextWord(solution, nextWord):
                hasValidNextWord = True
                newSolution = copy.deepcopy(solution)
                newSolution.append(nextWord)
                
                getNextWords(newSolution, wordSet)
        if not hasValidNextWord:
            finalSolutions.append(solution)
    else:
        finalSolutions.append(solution)
        
# def getEverySolution(wordSet):
    # for word in wordSet:
        # getNextWords([word], wordSet)
    # return 
    
def getShortestSolution(wordSet):
    shortestSolution = [wordSet]
    for word in wordSet:
        solution = [word]
        solution = getNextWords(solution, wordSet)
        solutionLength = 0
        for word in solution:
            solutionLength += len(word)
        if solutionLength < len(shortestSolution):
            shortestSolution = [solution]
    return shortestSolution
        
        
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
           
    wordSet = sortByWordLength(wordSet)
    print(wordSet)
    # getEverySolution(wordSet)
    
    shortestSolution = getShortestSolution(wordSet)

    # completeSolutions = []
    # perfectSolutions = []
    # usedLetters = []
    # for possibleSolution in finalSolutions:
        # isComplete = True
        # solutionLength = 0
        # solutionSize = len(possibleSolution)
        # for word in possibleSolution:
            # solutionLength += len(word)
            # usedLetters.extend(word)
        # for letter in usedLetters:
            # if letter not in letters:
                # isComplete = False
        # for letter in letters:
            # if letter not in usedLetters:
                # isComplete = False
        # if isComplete:
            # completeSolutions.append(possibleSolution)
        # if solutionSize == perfectLength:
            # perfectSolutions.append(possibleSolution)
         
    # print(str(len(finalSolutions)) + " solutions found.")
    # print("Solutions: " + str(finalSolutions))
    # print(str(len(completeSolutions)) + " complete solutions found.")
    # print("Complete solutions: " + str(completeSolutions))
    # print(str(len(perfectSolutions)) + " perfect solutions found.")
    # print("Perfect solutions: " + str(perfectSolutions))
    

