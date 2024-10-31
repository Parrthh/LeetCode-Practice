from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # STEP - 1: Create a mapping of each character in the alien dictionary
        # order to its index for quick comparison.
        # This dictionary allows us to convert the custom alien order into indices
        # for easier comparison in a standard lexicographical way.
        order_map = {char: index for index, char in enumerate(order)}
        
        # TIME COMPLEXITY: Building 'order_map' takes O(1) time since there are only 26 characters.
        # SPACE COMPLEXITY: The space for 'order_map' is also O(1) since it contains a fixed number of entries.

        # STEP - 2: Compare each adjacent pair of words to see if they are in the correct order.
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # STEP - 3: Compare each character in word1 and word2 until we find a difference
            # or until we reach the end of the shorter word.
            for j in range(min(len(word1), len(word2))):
                # If the characters at the current position are different
                if word1[j] != word2[j]:
                    # Check their priority based on the custom alien dictionary.
                    # If the character in word1 has a higher index than the character
                    # in word2 (meaning it comes later in alien order), return False.
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    # If we found that word1[j] < word2[j], we break out of the loop
                    # as we confirmed these two words are in the correct order.
                    break
            else:
                # STEP - 4: If we finish the for loop without finding a difference
                # and word1 is longer than word2, it means word1 cannot be a prefix of word2.
                # For instance, "apple" should come after "app" since "app" is a prefix of "apple".
                if len(word1) > len(word2):
                    return False

        # If all adjacent pairs are in the correct order, return True.
        return True

# TIME COMPLEXITY:
# - Let n = number of words, and m = average length of words.
# - We compare each word with its adjacent word, and for each comparison,
#   we might need to compare up to m characters.
# - Therefore, the overall time complexity is O(n * m).

# SPACE COMPLEXITY:
# - The only additional space we used is the dictionary 'order_map', which has a fixed size of 26 entries.
# - So the space complexity is O(1).
