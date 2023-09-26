import json
from pdb import set_trace as bp

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
	
if __name__ == '__main__':
    file = open("../words_dictionary.json", "r")
    words = json.load(file)

    letters = ''
    letterGroups = [["e","t","c"],["a","u","f"],["l","i","r"],["y","m","s"]]
    for i in letterGroups:
        letters = letters + ''.join(str(v) for v in i)

    wordSet = []
    for word in words:
        if len(word) > 2:
            valid = checkWord(word, letters, letterGroups)
            if valid:
                wordSet.append(word)

    validSolutions = []

    for i in wordSet:
        possibleSolution = [i]
        checkAgainst = i
        for j in wordSet:
            validWord = True
            if checkWordPair(checkAgainst, j):
                usedLetters = ''.join(str(v) for v in possibleSolution)
                for letter in j:
                    if letter in usedLetters[:-1]:
                        validWord = False
                if validWord:
                    possibleSolution.append(j)
                    checkAgainst = j
        validSolutions.append(possibleSolution)

    # TODO validSolutions are normal are correct at this point
    print("All valid solutions: " + str(validSolutions))

    # importing the pandas package
    import pandas as pd

    # creating DataFrame
    df = pd.DataFrame(validSolutions, columns= ['A','B','C','D','E'])
    df
    
    # filter out NaN values from the 'col1' column
    filtered_df = df[ df['E'].notna() ]
    print(filtered_df)
    
    max_length_A = df['A'].apply(lambda x: len(x)).max()
    print(max_length_A)
    
    filtered_B = df[ df['B'].notna() ]
    max_length_B = filtered_B['B'].apply(lambda x: len(x)).max()
    print(max_length_B)
    
    filtered_C = df[ df['C'].notna() ]
    max_length_C = filtered_C['C'].apply(lambda x: len(x)).max()
    print(max_length_C)
    
    filtered_D = df[ df['D'].notna() ]
    max_length_D = filtered_D['D'].apply(lambda x: len(x)).max()
    print(max_length_D)
    
    filtered_E = df[ df['E'].notna() ]
    max_length_E = filtered_E['E'].apply(lambda x: len(x)).max()
    print(max_length_E)   
    
    df.loc[df['A'].str.len() == max_length_A]