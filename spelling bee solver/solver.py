import json

if __name__ == '__main__':
    file = open("words_dictionary.json", "r")
    words = json.load(file)
    
    centerLetter = "g"
    letters = ["o","a","p","n","d","r"]
    
    maxLength = 0
    length = 0
    
    for word in words:
        noBadLetters = True
        if centerLetter in word:
            for letter in word:
                if letter != centerLetter and letter not in letters:
                    noBadLetters = False
        else:
            noBadLetters = False
        
        if noBadLetters:
            if len(word) > 4:
                print(word)
    