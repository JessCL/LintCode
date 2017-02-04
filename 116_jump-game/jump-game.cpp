/*
@Copyright:LintCode
@Author:   cong liu
@Problem:  http://www.lintcode.com/problem/jump-game
@Language: C++
@Datetime: 16-12-14 20:12
*/

class Solution {
public:
    bool canJump(vector<int> A) {
        int tmpMax = 0;
        int n = A.size();
        for (int i = 0; i < n; i++) {
            if (i > tmpMax) return false;
            if (tmpMax < i + A[i])
                tmpMax = i + A[i];
        }
        return true;
    }
};