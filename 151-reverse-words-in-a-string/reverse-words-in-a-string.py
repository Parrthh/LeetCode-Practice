class Solution:
    def trim_spaces(self, s: str) -> str:
        left, right = 0, len(s) - 1

        # Look for if there are any leading space:
        while left <= right and s[left] == " ":
            left += 1
        
        # Look for if there are any trailing spaces:
        while left <= right and s[right] == " ":
            right -= 1
        
        # Reducing multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1
        return output

    # The following method will reverse the whole string
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
    # The following method will reverse each word, because thats what we want to do
    def reverse_each_word(self, l:list) -> None:
        n = len(l)
        start, end = 0, 0
        while start < n:
            while end < n and l[end] != " ":
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1
    # This function is abstracting all the functions and using them to remove spaces, reversing the whole list, reverse each word and providing the output
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse(l, 0, len(l) - 1)
        self.reverse_each_word(l)
        return "".join(l)


"""
TIME COMPLEXITY: O(n)
1. trim_spaces -> O(n)
2. reverse -> O(n)
3. reverse_each_word -> O(n)
4. Joining the list of characters back into a s tring using "".join(l) -> O(n)
5. Therefore, the overall time complexity is O(n)


SPACE COMPLEXITY: O(n)
1. The trim_spaces method creates a new list output of size up to n
2. The reverse and reverse_each_word methods modify the list in place without additional space
3. Joining the list back into a string also requires O(n) spaces
4. The total space complexity: O(n)
"""