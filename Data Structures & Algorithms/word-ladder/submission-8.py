class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                w = word[:i] + "*" + word[i+1:]
                adj[w].append(word)

        q = deque([beginWord])
        visited = set(beginWord)
        out = 0

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return out + 1

                for i in range(len(w)):
                    x = w[:i] + "*" + w[i+1:]
                    for word in adj[x]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
            out += 1 
        return 0
