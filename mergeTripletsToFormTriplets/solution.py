class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        a=b=c=float("-inf")
        for triplet in triplets:
            currFirst=triplet[0]
            currSecond=triplet[1]
            currThird=triplet[2]
            if(max(a,currFirst)>target[0] or max(b,currSecond)>target[1] or  max(c,currThird)>target[2]):
                continue
            a=max(a,currFirst)
            b= max(b,currSecond)
            c= max(c,currThird)
        return a ==target[0] and b==target[1] and c==target[2]