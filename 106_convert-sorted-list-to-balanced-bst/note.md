```
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/convert-sorted-list-to-balanced-bst
@Language: Markdown
@Datetime: 16-12-16 20:41
```

用双指针法。具体来说就是，有两个指针，一个指针fast每次走两步，一个指针slow每次走一步，当fast指针走完时，说明slow指针正好走到了一半。用这样的方法就可以找到单链表的中间节点。

注意 helper函数确定start 和end两个参数。
也可以用O(n) 方法，类似BST的中序遍历的逆向思维。

http://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/