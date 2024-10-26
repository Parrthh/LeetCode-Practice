class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # STEP - 1: Create mapping of each character in the alien dict
        order_map = {char:index for index, char in enumerate(order)}
        # STEP - 2: Compare each adjacent pair
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            # STEP - 3: Compare each character
            for j in range(min(len(word1), len(word2))):
                # If the first character of each word is not same
                if word1[j] != word2[j]:
                    # We check if it has more priority compared to word2
                    # if yes we return False
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    break
            # Keep the else block on if for loop completes without hitting a break statement
            else:
                    # STEP - 4: Check if the len of word1 is more
                    # If it is then return False
                    # Because word1 cannot be the prefix of word 2
                if len(word1) > len(word2):
                    return False
        return True