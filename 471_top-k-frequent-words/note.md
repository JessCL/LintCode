```
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/top-k-frequent-words
@Language: Markdown
@Datetime: 16-12-18 01:07
```

为了保证You should order the words by the frequency of them in the return list, the most frequent one comes first. If two words has the same frequency, the one with lower alphabetical order come first.
不能保证heap的大小为O(k)

所以都放到heap里，复杂度O(nlogn)