from collections import Counter

class Solution:
    def check_anagram(self,s):
        from collections import Counter
        n,sCounter=len(s),Counter(s)
        for i in range(1,n//2+1):
            if n%i==0:
                subs=s[:i]
                if Counter(subs*(n//i))==sCounter:
                    return subs
        return s

    def check_anagramN2(self, s):
        length = len(s)
        for window_size in range(1, length // 2 + 1):
            if length % window_size == 0:
                window_counter = Counter(s[:window_size])
                for i in range(window_size, length, window_size):
                    if window_counter != Counter(s[i:i+window_size]):
                        break
                    #window_counter = window_counter + Counter(s[i:i+window_size]) - Counter(s[i-window_size:i])
                else:
                    return s[:window_size]
        return s    


    
    def check_anagramDQ(self, s, window_size=1):
        def is_anagram(s, window_counter, window_size):
            length = len(s)

            for i in range(window_size, length, window_size):
                if window_counter != Counter(s[i:i+window_size]):
                    return False
                #window_counter = window_counter + Counter(s[i:i+window_size]) - Counter(s[i-window_size:i])

            return True

        length = len(s)

        if window_size > length // 2:
            return s

        if length % window_size == 0:
            window_counter = Counter(s[:window_size])
            if is_anagram(s, window_counter, window_size):
                return s[:window_size]

        return self.check_anagramDQ(s, window_size + 1)

sol=Solution()
print(sol.check_anagramDQ('abcabc'))  # 2
print(sol.check_anagramDQ('abcdbca'))  # 2
print(sol.check_anagramDQ('ababbaab'))  # 2
print(sol.check_anagramDQ('bcaacbabc'))  # 2
print(sol.check_anagram('abcabc'))  # 2
print(sol.check_anagram('abcdbca'))  # 1
print(sol.check_anagram('ababbaab'))  # 1
print(sol.check_anagram('bcaacbabc'))  # 1
print(sol.check_anagramN2('abcabc'))  # 2
print(sol.check_anagramN2('abcdbca'))  # 1
print(sol.check_anagramN2('ababbaab'))  # 1
print(sol.check_anagramN2('bcaacbabc'))  # 1