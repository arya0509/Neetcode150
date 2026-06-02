class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        triplet=triplets[0]
        for t in triplets:
            if(t==triplet):
                continue
            a= max(triplet[0],t[0])<=target[0]
            b= max(triplet[1],t[1])<=target[1]
            c= max(triplet[2],t[2])<=target[2] 

            if(a and b and c):
                triplet[0]=max(triplet[0],t[0])
                triplet[1]=max(triplet[1],t[1])
                triplet[2]=max(triplet[2],t[2])
        return triplet == target 

