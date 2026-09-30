import json

if __name__ == '__main__':
    file = open("../words_dictionary.json", "r")
    words = json.load(file)
    
    letters = ["r","t","o","o","e","x","c"]

    possibleWords = []

    def checkWord(word, availableLetters):
        badLetter = None
        for letter in word:
            if letter in availableLetters:
                availableLetters.remove(letter)
            else:
                if badLetter is None:
                    badLetter = letter
                else:
                    return None
        return badLetter

    # words = ["exotic"]
    for word in words:
        if word == "exotic":
            print("found exotic")
        availableLetters = letters.copy()
     
        badLetter = checkWord(word, availableLetters)
        if badLetter is not None:
            combination = [word, badLetter]
            possibleWords.append(combination)
            
    print(possibleWords)