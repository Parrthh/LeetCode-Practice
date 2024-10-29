class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Create frequency counter
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_counter = freq.get(1,1)
        freq.pop(1,None)
        max_counter = max_counter -1 if max_counter%2 == 0  else max_counter
        print(max_counter)
        if len(set(nums)) == 1:
            return max_counter

        se_t = freq.keys()

        # If no frequency is greater than 1, return 1
        if max(freq.values()) == 1:
            return max_counter


        # Filter out elements with frequency greater than 1
        new_freq = {k: v for k, v in freq.items() if v > 1 }

        # Sort dictionary by frequency in descending order
        sorted_freq = dict(sorted(new_freq.items(), key=lambda item: item[1], reverse=False))

        # Counter for the output
        counter = 1

        print(sorted_freq)

        # Iterate over sorted keys
        for next_val in sorted_freq:
            # Check squares and increment counter as needed
            #print('$')
            while next_val*next_val in se_t:
                print(next_val)
                counter += 2  # Increment by 1 instead of 2 for consistency

                if next_val * next_val in sorted_freq:
                    next_val = next_val * next_val

                else:
                    break
            
            if counter > max_counter:
                max_counter = counter

            counter = 1

        return max_counter



        