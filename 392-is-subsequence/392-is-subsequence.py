class Solution(object):
    def isSubsequence(self, sString, tString):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(sString) > len(tString):
            return False
        if len(sString) == 0:
            return True
        subsequence=0
        for i in range(0,len(tString)):
            if subsequence <= len(sString) -1:
                print(sString[subsequence])
                if sString[subsequence]==tString[i]:

                    subsequence+=1
        return  subsequence == len(sString) 
