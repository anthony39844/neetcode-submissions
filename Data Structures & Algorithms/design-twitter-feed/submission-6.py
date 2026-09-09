class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweetCount = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.tweetCount, tweetId))
        self.tweetCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId] | {userId}
        heap = []
        for followerId in following:
            if self.tweets[followerId]:
                time, tweetId = self.tweets[followerId][-1]
                heap.append((time, tweetId, followerId, len(self.tweets[followerId]) - 1))

        out = []
        heapq.heapify(heap)
        while heap and len(out) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            out.append(tweetId)

            if idx > 0:
                next_time, next_tweet = self.tweets[user][idx - 1]
                heapq.heappush(heap, (next_time, next_tweet, user, idx - 1))
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)