import json
from pdb import set_trace as bp

letterGroups = [["a","x","n"],["o","h","l"],["i","m","e"],["p","y","t"]] 
totalLetters = 12
perfectLength = 6


finalSolutions = []

def getGroup(iterable, toGet):
    for i in range(len(iterable)):
        for j in iterable[i]:
            if j == toGet:
                return i
            
def checkWord(word, checkLetters, letterGroups):
    for letter in word:
        if letter in checkLetters:
            if word.count(letter) > 1:
                return False
            if word.index(letter) != len(word)-1:
                lGroup = getGroup(letterGroups, letter)
                lNGroup = getGroup(letterGroups, word[word.index(letter)+1])
                if lGroup == lNGroup:
                    return False
        else:
            return False
    return True
    
def checkLetters(perm, wordIndex):
    for oneLetter in perm[wordIndex]:
        if wordIndex+1 < len(perm):
            for twoLetter in perm[wordIndex+1]:
                if twoLetter == oneLetter:
                    return False
    return True
    
def checkNextWord(solution, nextWord):
    usedLetters = []
    for word in solution:
        usedLetters.extend(word)
    if solution[-1][-1] == nextWord[0]:
        for letter in nextWord[1:]:
            if letter in usedLetters:
                return False
        return True
    return False   
    
def recursiveCall(solution, wordSet):
    hasValidNextWord = False
    for nextWord in wordSet:
        if checkNextWord(solution, nextWord):
            hasValidNextWord = True
            newSolution = []
            newSolution.extend(solution)
            newSolution.append(nextWord)
            
            recursiveCall(newSolution, wordSet)
    if not hasValidNextWord:
        finalSolutions.append(solution)
        
def getSolutions(wordSet):
    for word in wordSet:
        recursiveCall([word], wordSet)
    return
 
        
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
                
    getSolutions(wordSet)

    completeSolutions = []
    perfectSolutions = []
    for possibleSolution in finalSolutions:
        solutionLength = 0
        solutionSize = len(possibleSolution)
        for word in possibleSolution:
            solutionLength += len(word)
        if solutionLength == len(letters) + solutionSize - 1:
            completeSolutions.append(possibleSolution)
        if solutionSize == perfectLength:
            perfectSolutions.append(possibleSolution)
         
    print(str(len(completeSolutions)) + " complete solutions found.")
    print("Complete solutions: " + str(completeSolutions))
    print(str(len(perfectSolutions)) + " perfect solutions found.")
    print("Perfect solutions: " + str(perfectSolutions))
    

