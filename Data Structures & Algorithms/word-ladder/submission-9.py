class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = {}

        for word in wordList:
            for i in range(len(word)):
                x = word[:i] + "*" + word[i+1:]
                if x not in d:
                    d[x] = [word]
                else:
                    d[x].append(word)
            
        out = 0
        q = deque([beginWord])
        visited = set([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return out + 1

                for i in range(len(word)):
                    x = word[:i] + "*" + word[i+1:]
                    if x in d:
                        for w in d[x]:
                            if w not in visited:
                                visited.add(w)
                                q.append(w)
            out += 1
        return 0