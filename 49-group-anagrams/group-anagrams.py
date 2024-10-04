class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            arr = []

            dic_t = dict()

            for y in strs:

                x = y
                x = list(x)
                x.sort()
                x = ''.join(x)

                print(x)
                
                if dic_t.get(x, False) == False:
                    
                    dic_t[x] = [y]

                else:
                    dic_t[x].append(y)

            return list(dic_t.values())


        