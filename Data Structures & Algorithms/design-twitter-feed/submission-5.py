class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweetCount = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.tweetCount, tweetId))
        self.tweetCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = list(self.tweets[userId])
        following = self.following[userId]
        for i in following:
            heap += list(self.tweets[i])
        heapq.heapify(heap)
        out = []
        for i in range(10):
            if heap:
                out.append(heapq.heappop(heap)[1])
            else:
                break
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
