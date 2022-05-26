# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    if len(word) != len(anagram):
        return False
 
    word = sorted(word)
    anagram = sorted(anagram)
 
    return word == anagram

word = "hello"
anagram = "racecar"
print(find_anagrams(word, anagram))
