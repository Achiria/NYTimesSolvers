import json
from pdb import set_trace as bp

totalLetters = 12
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
    
def checkWordPair(i, j):
    if i[-1] == j[0]:
        for iL in i[:-1]:
            for jL in j[1:]:
                if iL == jL:
                    return False
        return True
    return False
    
    
    
def findSets(word, wordSet):
    toReturn = []
    usedLetters = []
    for letter in word:
        usedLetters.append(letter)
 
    toReturn.append(getNextArray(toReturn, [word], usedLetters, wordSet))
    bp()
    return toReturn
    
def getNextArray(solutions, words, usedLetters, wordSet):
    #bp()
    for nextWord in wordSet:
        if isNextWordValid(words[-1], nextWord, usedLetters):
            usedLetters.extend(nextWord[1:])
            words.append(nextWord)
            return getNextArray(solutions, words, usedLetters, wordSet)
    solutions.append(words)
    return solutions

def isNextWordValid(word, nextWord, usedLetters):
    if word[-1] == nextWord[0]:
        for letter in nextWord[1:]:
            if letter in usedLetters:
                return False
        return True
    return False

def getSubLists(word, wordSet, usedLetters, solution, solutions):
    solution.append(word)
    if len(usedLetters) != totalLetters:
        for wordTwo in wordSet:
            if isNextWordValid(word, wordTwo, usedLetters):
                usedLetters.extend(wordTwo[1:])
                # solution.append(wordTwo)
                newSolution = getSubLists(wordTwo, wordSet, usedLetters, solution, solutions)
    if len(solutions) > 0:
        if solution != solutions[-1]:
            solutions.append(solution)
    else:
        solutions.append(solution)
    return solutions
    
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
    
# def getSolutions(letters, wordSet):
    # solutions = []
    # for word in wordSet:
        # usedLetters = []
        # usedLetters.extend(word)
        # solutions.extend(getSubLists(word, wordSet, usedLetters, [], []))
    # return solutions

def recursiveCall(solution, wordSet):
    hasValidNextWord = False
    # bp()
    for nextWord in wordSet:
        if checkNextWord(solution, nextWord):
            hasValidNextWord = True
            newSolution = []
            newSolution.extend(solution)
            newSolution.append(nextWord)
            
            recursiveCall(newSolution, wordSet)
            # break
            # solution.append(nextWord)
    if not hasValidNextWord:
        finalSolutions.append(solution)
        
def getSolutions(wordSet):
    # solution = []
    # bp()
    for word in wordSet:
        recursiveCall([word], wordSet)
        # solutions.extend(getSubLists(word, wordSet, usedLetters, [], []))
    return
 
        
if __name__ == '__main__':
    file = open("../words_dictionary.json", "r")
    words = json.load(file)
    
    letters = ''
    letterGroups = [["i","k","a"],["c","h","w"],["e","p","o"],["d","r","n"]] 
    for i in letterGroups:
        letters = letters + ''.join(str(v) for v in i)  
       
    wordSet = []
    for word in words:
        if len(word) > 2:                              
            valid = checkWord(word, letters, letterGroups)
            if valid:
                wordSet.append(word)
                
    # validSolutions = [] 

    
    # validSolutions = getSolutions(letters, wordSet)
    
    # bp()
    # print(validSolutions)

    getSolutions(wordSet)
    print(finalSolutions)






    # for i in wordSet:
        # findSets(i, wordSet)
    
        # possibleSolution = [i]
        # checkAgainst = i
        # for j in wordSet:    
            # validWord = True
            # if checkWordPair(checkAgainst, j):
                # usedLetters = ''.join(str(v) for v in possibleSolution)
                # for letter in j:
                    # if letter in usedLetters[:-1]:
                        # validWord = False
                # if validWord:
                    # possibleSolution.append(j)
                    # checkAgainst = j
                    # # bp()
                    # # flatSolution = list(flatten(possibleSolution))
                    # # bp()
                    # # if len(flatSolution) > 6:
                        # # bp()
        # # toRemove = []
        # # for wordOne in range(len(possibleSolution)):
            # # for wordTwo in range(len(possibleSolution)):
                # # if abs(wordOne-wordTwo) > 1:
                    # # # bp()
                    # # if not checkWordPairShared(possibleSolution[wordOne], possibleSolution[wordTwo]):
                        # # toRemove.append(wordTwo)
                        # # # possibleSolution.pop(wordTwo)
        # # for removalIndex in reversed(range(len(toRemove))):
            # # possibleSolution.pop(removalIndex)
        # validSolutions.append(possibleSolution)
        # # print(possibleSolution)
    
    # TODO validSolutions are normal are correct at this point
    #print("All valid solutions: " + str(validSolutions))
    
    longestSolutionLength = 0
    longestSolution = []
    biggestSolutionSize = 0
    biggestSolution = []
    completeSolutions = []
    perfectSolutions = []
    # for possibleSolution in validSolutions:
    for possibleSolution in finalSolutions:
        solutionLength = 0
        solutionSize = len(possibleSolution)
        for word in possibleSolution:
            solutionLength += len(word)
        if solutionLength >= longestSolutionLength:
            if solutionLength > longestSolutionLength:
                longestSolutionLength = solutionLength
                longestSolution = []
            longestSolution.append(possibleSolution)
        if solutionSize >= biggestSolutionSize:
            if solutionSize > biggestSolutionSize:
                biggestSolutionSize = solutionSize
                biggestSolution = []
            biggestSolution.append(possibleSolution)
        if solutionLength == len(letters) + solutionSize - 1:
            perfectSolutions.append(possibleSolution)
        # usedLetters = []
        # for word in possibleSolution:
            # for letter in word:
                # usedLetters.append(letter)
        # allLetters = True
        # for letter in letters:
            # if letter not in usedLetters:
                # allLetters = False
        # if allLetters:
            # completeSolutions.append(possibleSolution)
                
       
    
    print("Biggest solution found: " + str(biggestSolution))    
    print("Longest solution found: " + str(longestSolution))    
    print(str(len(completeSolutions)) + " complete solutions found.")
    print("Complete solutions: " + str(completeSolutions))
    print(str(len(perfectSolutions)) + " perfect solutions found.")
    print("Perfect solutions: " + str(perfectSolutions))
    
    # TODO validSolutions are not normal and have nested lists
    #print("All valid solutions: " + str(validSolutions))
            
            
            

# def checkWordPairShared(i, j):
    # for iL in i:
        # for jL in j:
            # if iL == jL:
                # return False
        # return True            
            
# def createAndValidate(iterable, gennedPerm):
    # toReturn = ''
    # for k in range(len(gennedPerm)):
        # toReturn = toReturn + ''.join(str(v) for v in gennedPerm[k])
        # if k != len(gennedPerm)-1:
            # kGroup = getGroup(iterable, gennedPerm[k])
            # knGroup = getGroup(iterable, gennedPerm[k+1])
            # if kGroup == knGroup:
                # return ""
    # return toReturn

# def permutations(iterable):
    # pool = tuple(iterable)
    # n = len(pool)
    # r = n

    # indices = list(range(n))
    # cycles = list(range(n, n-r, -1))
    # while n:
        # for i in reversed(range(r)):
            # cycles[i] -= 1
            # if cycles[i] == 0:
                # indices[i:] = indices[i+1:] + indices[i:i+1]
                # cycles[i] = n - i
            # else:
                # j = cycles[i]
                # indices[i], indices[-j] = indices[-j], indices[i]
                # gennedPerm = list(pool[i] for i in indices[:r])
                # yield gennedPerm
                # break
        # else:
            # return
            
            

# Old generator code
# results in list with ~1500! values

    # print(str(len(wordSet)))
    # print(wordSet)
    # permGen = permutations(wordSet) 
    # perms = []
    
    #for perm in permGen:
    #    perms.append(perm)
    #print("perms len " + str(len(perms)))
    
    # permIndex = 0
    # uselessWords = []
    
    # while True:
    # #for perm in perms:
        # perm = next(permGen)
        # print(perm)
        # indexesToRemove = []
        # for wordIndex in reversed(range(len(perm)-1)):
            # if not checkLetters(perm, wordIndex):
                # indexesToRemove.append(wordIndex+1)
            # elif wordIndex+1 < len(perm):
                # if perm[wordIndex][-1] != perm[wordIndex+1][0]:
                    # indexesToRemove.append(wordIndex+1)
        # for index in indexesToRemove:
            # perm.pop(index)
        # print(perm)
        # if len(perm) == 1:
            # perms.pop(permIndex)
            # # uselessWords.append(perm[0])
        # permIndex += 1
        