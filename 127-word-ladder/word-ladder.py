class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # To check if the endword is present in the wordList:
        if endWord not in wordList:
            return 0
        # List of neighbors:
        neighbors = defaultdict(list)
        # Adding the beginWord because it is not a part of wordList:
        wordList.append(beginWord)
        # Looping through every word in the wordList:
        for word in wordList:
            # For each word, we want to find the possible pattern
            # The pointer j goes through every single position of this word
            for j in range(len(word)):
                # For each position of this word, we want to replace a char with a wild card char
                pattern = word[:j] + "*" + word[j + 1:]
                # In our neighbor list, all the strings that fall in this pattern, we append the current word
                neighbors[pattern].append(word)
        # Keep track of the visited words
        visited_cell = set([beginWord])
        # We will be going layer by layer, and pop the word
        queue = deque([beginWord])
        # Number of words in the path
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighborWord in neighbors[pattern]:
                        if neighborWord not in visited_cell:
                            visited_cell.add(neighborWord)
                            queue.append(neighborWord)
            res += 1
        return 0

