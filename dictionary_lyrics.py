# dictionary_lyrics.py

def lyrics_to_frequencies(lyrics):
    #Return the frequency of word in a song lyrics
    myDict = {}

    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1

    return myDict

# test goes here
she_loves_you = ['she', 'loves', 'you',
'yeah',
'she', 'loves', 'you', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah']
print(lyrics_to_frequencies(she_loves_you))