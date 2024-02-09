class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups
        anagram_groups = {}
        
        # Iterate through each word in the input list
        for word in words:
            # Sort the characters in the word to create a key
            key = "".join(sorted(word))
            
            # If key is not in the dictionary, add a new entry with the word as a list
            if key not in anagram_groups:
                anagram_groups[key] = [word]
            # If key is already present, append the word to the existing list
            else:
                anagram_groups[key].append(word)
        
        # Return the values (anagram groups) of the dictionary
        return anagram_groups.values()
        
