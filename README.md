# AlgorithmsDesignTechniquesandAnalysis
&lt;Algorithms Design Techniques and Analysis>M.H. a1suwaiyel textbook algorithms 

《算法设计技巧与分析》

<div align=center> <img src=./resources/textbook.jpg /><img src=./resources/textbook2.jpg /></div>



## 目录


5. 归纳法 (induction)

6. 分治

7. 动态规划 (DP )

8. 贪婪(Greedy)

9. .

10. .

11. .

12. .

    Part 5 克服困难性

13. 回溯(backtrack)

14. 随机算法(Randomized Algs)

15. 近似算法

    Part 6 指定域问题的迭代改进算法

16. 网络流

17. 匹配

    Part 7 计算几何

18. 几何扫描

19. 韦恩图解

---

## 课后习题

Ch14 Randomized  Algs [to be continue.]

* 14.2 使用硬币生成1 ... n之间的随机数（大于n的忽略）,并把选择的元素与随后一位元素交换，再生成1..(n-1)之间的元素。

* 14.5  **Fisher–Yates shuffle** 随机打乱一个数组

```
-- To shuffle an array a of n elements (indices 0..n-1):
for i from n−1 downto 1 do
     j ← random integer such that 0 ≤ j ≤ i # 生成 1->i的随机数并把该数与最后一个数交换
     exchange a[j] and a[i]
```

* 14.10 平均情况下二者的平均查找次数一样。
  * 对于线性查找，n个元素里面有k个相当于n/k个元素里面有一个目标元素x，那么平均情况下搜索完这n/k个元素必然会遇到目标元素。
  * 对于随机查找，一次就能搜索到的概率是k/n，那么平均情况下 1/(k/n) = n/k次就能够查找到目标元素。
* 14.11 选择一个数不在上半部的概率为0.5。如果选择两个数，均不在上半部的概率是0.25。如果选择k个数，都不在上半部的概率为。如果我们选择这k个数当中最大的一个值，这个值在下半部的概率是？在上半部的概率是？
* 14.12 同上
* 14.13 *Freivalds' algorithm* 生成一个n维随机向量$$X$$ ，每个元素$$x_i ∈{{0, 1}}$$   时间复杂性为$$O(n^2)$$  Its time [analysis ](<http://www.cs.nthu.edu.tw/~wkhon/random12/lecture/lecture3.pdf>)is very strange~。It seems to assume most elements are 0s.
* 14.14 原问题等价于验证 AB==I 。这个问题在14.13中有所讨论。
* 14.16 把选择的元素与最后一个元素交换。
* 14.17 上题的时空复杂度分别为 O(m) ， O(1 
* 14.20 [参考](<http://www.cs.nthu.edu.tw/~wkhon/random12/lecture/lecture3.pdf>)
* 14.22 计算它们互不相同的概率，就可以得出其概率是 难以置信的0.5。

---

Ch16 Network Flow

* 16.1 证明对于图中任意一条边(u, v)，流函数的四个条件依旧满足。
* 16.2 
* 16.6 构建一个虚拟的源点，连接所有的源点，边的容量为每个真实源点的通过量。
* 16.8 DFS
* 16.9 对图G做一些修改，每个顶点分裂为两个顶点，这两个顶点间用一个顶点容量大小的边连接。
* 16.10 DFS，记录最大瓶颈容量的路径
* 16.11 BFS
* 16.12 剩余图中有的边并未在层次图中出现。
* 16.14 最大流，每个节点的容量为单位容量
* 16.15 想要找出图G的最小割，也就是找出它的最大流。找出最大流之后，确定最小割的方法是？把源点只通过非饱和边能到的顶点加入S。其他则为T。
* 16.18 由题，所有顶点的最小度为k，则|E| >= K * |V| / 2