# Write a program to find anagrams in a given list of words. Two words are called
# anagrams if one word can be formed by rearranging letters of another. For example
# ‘eat’, ‘ate’ and ‘tea’ are anagrams.

def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

if __name__ == "__main__":
    words = ["eat", "ate", "tea", "race", "care", "heart", "earth"]
    print(groupAnagrams(words))