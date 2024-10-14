class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        print(list_x)
        rev_x = list_x[::-1]
        print(rev_x)
        for i in range(len(list_x)):
            if list_x[i] != rev_x[i]:
                return False
            
        return True
           
