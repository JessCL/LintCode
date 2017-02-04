# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/median-of-two-sorted-arrays
@Language: Python
@Datetime: 16-12-24 20:11
'''

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)

        if (lenA + lenB) % 2 == 0:  
            index1 = (lenA + lenB) / 2
            index2 = (lenA + lenB) / 2 + 1
        else: 
            index1 = (lenA + lenB) / 2 + 1
            index2 = (lenA + lenB) / 2 + 1
            
        if lenA == 0 and lenB == 0:
            return 0
        elif lenA == 0:
            return float(B[index1 - 1] + B[index2 - 1]) / 2
        elif lenB == 0:
            return float(A[index1 - 1] + A[index2 - 1]) / 2
            
        indexA = 0
        indexB = 0
        count = 0
        num1 = None
        num2 = None
        while indexA < lenA and indexB < lenB:
            if A[indexA] < B[indexB]:
                count += 1
                if count == index1:
                    num1 = A[indexA]
                if count == index2:
                    num2 = A[indexA]
                    break
                indexA += 1
                    
            else:
                count += 1
                if count == index1:
                    num1 = B[indexB]
                if count == index2:
                    num2 = B[indexB]
                    break
                indexB += 1
                    
        if num1 is not None and num2 is not None:
            #print num1, num2
            return float(num1 + num2) / 2
        while indexA < lenA:
            count += 1
            if count == index1:
                num1 = A[indexA]
            if count == index2:
                num2 = A[indexA]
                break
            indexA += 1
                
        while indexB < lenB:
            count += 1
            if count == index1:
                num1 = B[indexB]
            if count == index2:
                num2 = B[indexB]
                break 
            indexB += 1
        #print num1, num2
        return float(num1 + num2) / 2

        