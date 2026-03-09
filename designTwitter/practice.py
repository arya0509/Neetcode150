from collections import defaultdict
import heapq
class Twitter(object):

    def __init__(self):
        self.follower=defaultdict(set)
        self.tweets=defaultdict(list)
        self.time=0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append([-(self.time+1),tweetId])
        self.time+=1
        
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        self.follower[userId].add(userId)

        minHeap=[]
        for followee in self.follower[userId]:
            if(followee in self.tweets):
                index=len(self.tweets[followee])-1
                time,tweetID=self.tweets[followee][index]
                heapq.heappush(minHeap,(time,tweetID,followee,index-1))
        res=[]
        while(minHeap and len(res)<10):
            time,tweetID,followee,index=heapq.heappop(minHeap)
            res.append(tweetID)
            if(index>=0):
                time,tweetID=self.tweets[followee][index]
                heapq.heappush(minHeap,(time,tweetID,followee,index-1))
        return res

        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if(followeeId in self.follower[followerId]):
            self.follower[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)