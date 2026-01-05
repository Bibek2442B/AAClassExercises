def countWords(text):
    words = text.split()
    wordList=[]
    words.sort(key=str.lower)
    for word in words:
        count = words.count(word)
        obj=(word,count)
        if obj in wordList:
            continue
        wordList.append(obj)

    for word in wordList:
        print(f"{word[0]}: {word[1]}")


countWords("This is a test sentence is is ")
