# AlgorithmsDesignTechniquesandAnalysis
&lt;Algorithms Design Techniques and Analysis>M.H. a1suwaiyel textbook algorithms 



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
* 14.12同上
* 14.13 这道题有分析？。。。where？
* 14.14
* 