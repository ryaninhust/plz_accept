from functools import reduce
# url: http://oj.leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    # @param s, a string
    # @return a string

    def reverseWords(self, s):
        words = s.split(' ')
        words = filter(lambda x: x is not '', words)
        if not words:
            return ""
        words.reverse()
        raw_result = reduce(lambda w1, w2: w1 + " " + w2, words)
        return raw_result.strip()
