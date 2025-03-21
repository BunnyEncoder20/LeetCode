'''
A gene is represented as a string of length n (where n is divisible by 4), composed of the letters A, C, T, and G. It is considered to be steady if each of the four letters occurs exactly I times. For example, GACT and AAGTCCT are both steady genes.
Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady.
Right now, he is examining a gene represented as a string gene. It is not necessarily steady. Fortunately,

Limak can choose one (maybe empty) substring of gene and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string gene, can you help Limak find
the length of the smallest possible substring that he can replace to make gene a steady gene?

Note: A substring of a string s is a subsequence made up of zero or more contiguous characters of s.
As an example, consider gene = ACTGAAAG. The substring A A just before or after G can be replaced
with C'T or TC. One selection would create ACTGACTG.

Function Description
Complete the steadyGene function in the editor below. It should return an integer that represents the length of the smallest substring to replace.
steadyGene has the following parameter:
• gene: a string
'''

from collections import Counter
def steadyGene(gene):
    n = len(gene)
    req = n//4
    fpp = Counter(gene)
    
    # already in steady state
    if all(fpp[c] == req for c in "ACTG"):
        return 0
    
    l,r = 0,0
    minlen = n
    
    while r < n:
        fpp[gene[r]] -= 1   
        while all(fpp[c] <= req for c in "ACGT"):
            minlen = min(minlen, r-l+1)
            fpp[gene[l]] += 1
            l += 1 
        r += 1
    return minlen