class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # STEP - 1: Combine and sort the data by timestamp
        # Here, we are creating alist of typles (timestanp, username, website)
        # We will sort the list by timestamp to ensurre we consider visits in chronological order
        data = sorted(zip(timestamp, username, website))

        # STEP - 2: Group websites visited by each user
        # Using a dictionary to group all visits for each user in chronological order
        # The dictionary will store the list of website visited by each user
        user_visits = defaultdict(list)
        for time, user, site in data:
            user_visits[user].append(site)
        
        # STEP - 3: Generate all 3-sequence patterns for each user
        # For each user, generate all possible co,binations of 3-sequence patterns from their visit history
        # Store these patterns in a dictionary with a set of users who visited the pattern
        # combinations function from Python's Itertools library to generate all 3 -sequence combinations
        # combinations(sites, 3) -> generates all possible ways to choose three websites from the list sites
        # while preserving the order in which they appear
        pattern_count = defaultdict(set)
        for user, sites in user_visits.items():
            # Generate all possible 3-sequence combinations
            if len(sites) >= 3:
                for pattern in combinations(sites, 3):
                    pattern_count[pattern].add(user)
        
        # STEP - 4: Determime the most frequencet 3-sequence pattern
        # Counting the number of unique users who visited each 3-sequence pattern
        # Choose the pattern with the highest count. If there is a tie, return the lexicographically smallest pattern
        max_pattern = None
        max_count = 0

        for pattern, users in pattern_count.items():
            count = len(users)
            # Check if we have a new maximum or lexicographically smaller pattern
            if count > max_count or (count == max_count and (max_pattern is None or pattern < max_pattern)):
                max_pattern = pattern
                max_count = count
        return list(max_pattern)

"""
TIME COMPLEXITY: O(n^3)
1. Sorting -> O(n log n)
2. Generating 3-sequence: O(n^3/u^2), where u is the number of users (assuming m = n/u)
3. Counting and comparing patterns :O(n^3)
4. Therefore, overall time complexity is O(n^3)

SPACE COMPLEXITY: O(n ^ 3)
1. The overall space complexity is dominated by the storage requirements for the pattern_count 
dictionary, which can be up to O(n ^ 3) in the worst case
"""