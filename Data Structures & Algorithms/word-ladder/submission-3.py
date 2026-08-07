class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            adj = defaultdict(list)
            wordList.append(beginWord)

            def check(s1: str, s2: str) -> bool:
                diff_count = 0
                for c1, c2 in zip(s1, s2):
                    if c1 != c2:
                        diff_count += 1
                        if diff_count > 1:
                            return False
                            
                return diff_count == 1

            for i in range(len(wordList)):
                for j in range(len(wordList)):
                    if i != j:
                        if check(wordList[i], wordList[j]):
                            adj[wordList[i]].append(wordList[j])

            q = deque([beginWord])
            out = 0
            visited = set()
            
            while q:
                for i in range(len(q)):
                    word = q.popleft()
                    visited.add(word)
                    if word == endWord:
                        return out + 1

                    for w in adj[word]:
                        if w not in visited:
                            q.append(w)
                out += 1

            return 0