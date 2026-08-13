from collections import defaultdict, deque
import heapq
class Twitter:

    def __init__(self):
        self.follower_list = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        culminated = self.follower_list.get(userId, set()).copy()
        culminated.add(userId)
        res = []
        heap = []
        pointers = {}
        for followee in culminated:
            if followee in self.tweets and self.tweets[followee]:
                pointers[followee] = len(self.tweets[followee]) - 1
                heapq.heappush_max(
                    heap,
                    (self.tweets[followee][pointers[followee]], followee)
                )
        while len(res) < 10 and heap:
            tweet, f = heapq.heappop_max(heap)

            res.append(tweet[1])

            pointers[f] -= 1

            if pointers[f] >= 0:
                heapq.heappush_max(
                    heap,
                    (self.tweets[f][pointers[f]], f)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_list:
            self.follower_list[followerId] = set()
        self.follower_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_list and followeeId in self.follower_list[followerId]:
            self.follower_list[followerId].remove(followeeId)
        
