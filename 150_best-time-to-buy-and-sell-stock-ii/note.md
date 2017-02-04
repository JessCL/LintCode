```
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii
@Language: Markdown
@Datetime: 16-12-20 23:03
```

http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html

分析：贪心法。从前向后遍历数组，只要当天的价格高于前一天的价格，就算入收益。

代码：时间O(n)，空间O(1)