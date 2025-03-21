'''
Problem:
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings. Please implement encode and decode.

Example:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
Constraints:

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoding = ""
        for s in strs:
            encoding += str(len(s)) + "#" + s
        return encoding

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, strs):
        res = []
        i = 0

        while i < len(strs):
            # extract numbers till #
            j = i 
            while strs[j] != '#':
                j += 1
            # convert it to int to get length of the word
            length = int(strs[i:j])
            
            # add the word to the resultant
            res.append(strs[j+1:j+1+length])
            
            # update i pointer
            i = j+1+length
        
        return res