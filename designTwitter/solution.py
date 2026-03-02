from collections import defaultdict
import heapq
class Twitter(object):

    def __init__(self):
        self.tweetMap =defaultdict(list)
        self.followMap=defaultdict(set)
        self.time=0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
       
        self.tweetMap[userId].append([self.time,tweetId])
        self.time-=1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        minHeap=[]
        self.followMap[userId].add(userId)

        for foloweeId in self.followMap[userId]:
            if foloweeId in self.tweetMap:
                index=len(self.tweetMap[foloweeId])-1
                count,tweetId=self.tweetMap[foloweeId][index]
                heapq.heappush(minHeap,[count,tweetId,foloweeId,index-1])
        res=[]
        while(minHeap and len(res)<10):
            count,tweetId,foloweeId,index=heapq.heappop(minHeap)
            res.append(tweetId)
            if(index>=0):
                count,tweetId=self.tweetMap[foloweeId][index]
                heapq.heappush(minHeap,[count,tweetId,foloweeId,index-1])
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)
            

        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if(followeeId in self.followMap[followerId]):
            self.followMap[followerId].remove(followeeId)
                


        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)