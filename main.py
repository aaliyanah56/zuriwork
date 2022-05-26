# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    if len(word1) != len(word2):
        return False
 
    word1 = sorted(word1)
    word2 = sorted(word2)
 
    return word1 == word2

word1 = "hello"
word2 = "racecar"
print(find_anagrams(word1, word2))
