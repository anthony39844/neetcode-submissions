class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            adj = defaultdict(list)
            wordList.append(beginWord)

            for word in wordList:
                for i in range(len(word)):
                    mask = word[:i] + "*" + word[i+1:]
                    adj[mask].append(word)
            
            print(adj)

            q = deque([beginWord])
            out = 0
            visited = set(beginWord)
            
            while q:
                for i in range(len(q)):
                    word = q.popleft()
                    if word == endWord:
                        return out + 1
                    for j in range(len(word)):
                        mask = word[:j] + "*" + word[j+1:]

                        for w in adj[mask]:
                            if w not in visited:
                                visited.add(w)
                                q.append(w)
                out += 1

            return 0