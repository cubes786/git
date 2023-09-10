class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed([word for word in s.split()]))
    
    def reverse_words(self, s: str) -> str:
        words = s.split()
        def recursive_reverse(words, i):
            if i == len(words):
                return ''
            else:
                return recursive_reverse(words, i + 1) + ' ' + words[i] if i != len(words) - 1 else words[i]
        return recursive_reverse(words, 0)

    
sol=Solution()
s1 = "the sky is blue"
print(sol.reverseWords(s1))
print(sol.reverse_words(s1))