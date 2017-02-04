```
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii
@Language: Markdown
@Datetime: 16-12-20 23:33
```

分析：动态规划法。以第i天为分界线，计算第i天之前进行一次交易的最大收益preProfit[i]，和第i天之后进行一次交易的最大收益postProfit[i]，最后遍历一遍，max{preProfit[i] + postProfit[i]} (0≤i≤n-1)就是最大收益。第i天之前和第i天之后进行一次的最大收益求法同Best Time to Buy and Sell Stock I。

http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html