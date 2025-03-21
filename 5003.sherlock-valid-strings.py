'''
herlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
Example
s = "abc"
This is a valid string because frequencies are {a:1,b:1,c:1}.
s = "abcc"
This is a valid string because we can remove one c and have 1 of each character in the remaining string.
s = "abccc"
This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a:1,b:1,c:2}.
'''

from collections import Counter
def isValid(s):
    fpp = Counter(s)
    fppf = Counter(fpp.values())
    
    # normally 1 or more than 2 freq
    if len(fppf) == 1: return "YES"
    if len(fppf) > 2: return "NO"
    
    # for 2 diff freq
    f1, f2 = sorted(fppf.keys())  # ensure f1 < f2
    
    # case : {a:1, c:4} - we can remove a to make valid string
    # check if freq == 1 and it occurs only once
    if f1 == 1 and fppf[f1] == 1:
        return "YES"
    
    # case : {a:1, c:2} - we can remove one c and make valid
    # check if higher freq = lower freq + 1 and only occurs once
    if f2 == f1 + 1 and fppf[f2] == 1:
        return "YES"
    
    # else
    return "NO"