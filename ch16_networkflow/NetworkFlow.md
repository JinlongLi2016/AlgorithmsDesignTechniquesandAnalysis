# 网络流问题

图中各边都有一个容量，在图G中从源点s开始到汇点t的流的最大值就是最大流问题。

# 预备知识

图G上的流是一个顶点对上的实函数f，具有以下4个条件。

1. 斜对称。
2. 容量约束
3. 流守恒
4. f(v, v) = 0

定义：一个割{S, T}是把顶点集分成两个自己S T的一个划分，使得s S t T。割的容量c(S, T) 定义为

---

## 图的存储方式(邻接矩阵 & 邻接表)

1. 邻接矩阵

   顶点间的关系存储在一个$n*n$矩阵M中。若u, v 两个顶点有边，对于无向图有权图，则M[u, v] = M[v, u] = weight[u, v]，对于有向图则有 M[u, v] = weight[u, v]

2. 邻接表

   图的顶点存储在一个线性表中，每个顶点的邻接边都以链表的形式依附在线性表该顶点上。对于有向图，需要θ(n+m)的空间，对于无向图，需要θ(n+2m)的空间。

---

* Dijkstra

```
Dijkstra Algorithm: 单源最短路径
Input	含权有向图G=(V, E), V={1, 2,..., n}
Output	G中顶点1到其他顶点的距离
1    X = {1}, Y = V - {1}； λ[1] = 1
2    for y = 2->n:
3        if y 与 1 相邻: λ[y] = length[1, y]
4        else: λ[y] = +inf
5    for j = 1 -> n-1:
6    	y = argmin(λ[y])  (y∈Y)
7    	X = X ∪ {y}
8    	Y = Y - {y}
9    	for y邻近的每条边 (y, w):
10    		if w ∈ Y and λ[y] + length[y, w] < λ[w]:
11    			λ[w] = λ[y] + length[y, w]
```

可以看到，在第6步，选择Y集合中离X集合最近的点需要O(n)的时间，总共需要循环n-1次。对于**邻接表存储形式**，第9步在整个算法执行过程中需要θ(m)次。算法总**时间复杂度为**$O(n^2 + m)$.

==对于具有非负权的有向图G和一个源点s，算法Dijkstra在**$O(n^2)$**的时间内找到s到图中所有顶点的最短距离。==

---

**贪心算法**一章通过把Y集合构建为最小堆进而把时间复杂度减少到O(mlgn)，对于稠图，时间复杂度为O(m)。

## 图的遍历(DFS/BFS)

对于邻接表存储的形式

1. DFS 时间复杂度为O(m)
2. BFS 时间复杂度为O(m)

# Ford-Fulkerson  福特弗克森方法

福特福克森方法每次选择一条增广路径，并用该增广路径的瓶颈容量来扩大网络流。

```
Alg 161 Ford-Fulkerson
Input 	网络(G, s, t, c)
Output: G 中的一个流
    初始化剩余图 R = G
    for (u, v) 属于 E
        f(u, v) = 0
    end for
    while 在R中有一条增广路径 p = s,.., t:
        设Δ为p的瓶颈容量
        for p 中的每条边(u, v):
            f(u, v) = f(u, v) + Δ
        end for
        更新剩余图R
    end while
```

# 最大容量增值 (MCA)

最大容量增值 在福特福克森方法的基础上，每次扩大网络流时选择容量最大的一条增广路径进行增值。

# 最短路径长度增值 (MPLA)

**层次图**：给定有向图 G(V, E)，它的层次图L (V, E'), E'={(u, v) | level(v) = level(u) + 1}。level(v)是顶点v的层次，即从s到v的路径中边的最小数。

算法从零网络流开始，初始化剩余图R为原图。然后逐阶段增大网络流，每个阶段分成两个步骤

1. 根据剩余图R计算层次图，如果ｔ不在层次图中则终止，否则继续
2. 只要在层次图L中有从ｓ到ｔ的路径ｐ，就用ｐ的瓶颈容量对路径ｐ进行增值。修改层次图L和剩余图R（删除饱和边以及增加某些边）。

```
Alg 最小路径长度增值 MPLA
Input	(G, s, t, c)
Output	G的最大流
    for (u, v) in E:
        f(u, v) = 0
    end for
    初始化剩余图，R=G
    查找R的层次图L
    while t in L:
        while 在L中t可以从s到达:
            let p=L中s->t的一条路径
            设Δ为p的瓶颈容量
            用Δ增值当前流
            沿着路径p更新L和R
        end while
        用剩余图R计算新的层次图
    end while
```

更新L：移除饱和边，非饱和边的容量减少？
更新剩余图R：移除饱和边，非饱和边的容量减少，可能还要增加逆向边？

时间复杂度分析：每个阶段计算的层次图路径长度都比前个阶段层次图中路径长度长，因此最多有n个阶段。每个阶段构造层次图需要m的时间(line16)，同时在每个阶段可能最多需要需要进行m次增值，而每次增值寻找最短增广路径需要m的时间(line10-15)。因此，时间复杂度为$O(nm + nm^2)$

**最小路径长度增值(MLPA) 算法能够在$O(nm^2)$内找到有向图的最大流** 

# Dinic阻塞流算法 

Dinic算法把时间复杂度进一步减小为$O(n^2m)$，在MPLA中，计算层次图后增广路径逐条找出，而Dinic更加高效地找出所有地增广路径，这也是改进运行时间地原因所在。

---

**阻塞流**：设G为一个网络，H是包含s和t的G的子图。H中的流f成为关于H的阻塞流，如果在H中每一条从s到t的路径中都至少有一条边饱和。

---

Dinic算法和前一个算法一样，算法整个流程被分为最多n个阶段，每个阶段由寻找层次图和关于此层次图阻塞流以及用阻塞流来增大网络流组成。

```
Alg Dinic 阻塞流算法
Input	(G, s, t, c)
Output	G的最大流
for (u, v) ∈ E:
	f(u, v) = 0
初始化剩余图 R = G
搜索层次图 L
while t 为 L中的顶点:
	 u = s
	 p = u
	 while outdegree(s) > 0 and u != t:
	 	while u != t and outdegree(s) > 0：# 前进搜索出一条增广路径
	 		if outdegree(u) > 0:
	 			suppose (u,v)为L中一条边
	 			p = p, v
	 			u = v
	 		else:
	 			删除L中 u 的邻接边
	 			删除p最末尾顶点u，且令p的倒数第二个节点为u
	 	if u == t:  
	 		假设p的瓶颈容量为Δ，沿着p推送一个Δ的流。
	 		修改层次图和剩余图
	 		把u置为修改层次图后s在路径p上能达到的最后一个顶点，注意u可能是s
	 计算新的层次图（根据剩余图）
```

最外层的循环对应于n-2个层次图（阶段），每个阶段内通过深度优先的方式来寻找增广路径。每寻找到一条增广路径 （语句`if u == t`）就用路径p的瓶颈容量进行增值。

它的时间复杂性分析如下，n-2个外层循环，每个外层循环内要深度优先遍历整张图并附带删除顶点和边 (m + n)。对于每一条增广路径增值的时间为 n (即沿着路径p推流，修改层次图和剩余图)，最多有m跳增广路径，时间为(nm)。故总的时间复杂性为$O(n^2m)$

**阻塞流(Dinic) 算法能够在$O(n^2m)$内找到有向图的最大流**

# MPM算法

MPM算法相比于Dinic算法寻找到了一个更快的寻找阻塞流的算法$O(n^2)$

顶点v的**通过量**（throughput），为引入边的总容量和引出边的总容量中的最小值。

```Alg 
Algorithm MPM
Input	(G, s, t, c)
Output	G的最大流
    for (u, v) ∈ E:
        f(u, v) = 0
    初始化剩余图 R = G 
    查找剩余图R的层次图L
    while t 为 L中的层次图顶点:
        while t 在L中从s能到达:
            查找最小通过量为g的顶点v
            从v到t推下g个单元流
            从s到v拉入g个单元流
            更新 f, L, R
        使用剩余图R计算新的层次图L
```
