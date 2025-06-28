#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # trivial case
        if endWord not in wordList:
            return 0
        
        # add beginning word into wordlist
        wordList.append(beginWord)

        # make adjList
        adjList = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "_" + word[i+1:]  
                adjList[pattern].append(word)
        
        # BFS 
        vis = set([beginWord])
        q = deque([beginWord])
        steps = 1       # think of it as lvls of bfs

        # traversal
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps
                
                # make patterns of word
                for i in range(len(word)):
                    pattern = word[:i] + "_" + word[i+1:]

                    # get adj words of pattern
                    for adjWord in adjList[pattern]:
                        if adjWord not in vis:
                            vis.add(adjWord)
                            q.append(adjWord)
                
            steps += 1

        
# @lc code=end

