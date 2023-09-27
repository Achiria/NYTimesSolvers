import json

if __name__ == '__main__':
    file = open("../words_dictionary.json", "r")
    words = json.load(file)
    
    for word in words:
        if len(word) < 3:
            words.remove(word)
    
    json_object = json.dumps(words, indent=4)
    
    with open("../words_dictionary_prog.json", "w") as outfile:
        outfile.write(json_object)    
    