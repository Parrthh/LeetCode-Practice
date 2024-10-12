class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_table = {}
        l = list(text)
        print(l)

        for i in l:
            if i in hash_table:
                hash_table[i] +=1
            else:
                hash_table[i] = 1
        
        return min(hash_table.get('b',0), hash_table.get('a',0), hash_table.get('l',0)//2, hash_table.get('o',0)//2, hash_table.get('n',0))
        