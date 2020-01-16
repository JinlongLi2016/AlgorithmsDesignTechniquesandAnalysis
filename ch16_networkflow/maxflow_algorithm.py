import networkx as nx
import matplotlib.pyplot as plt

from collections import defaultdict

# 网络流图F中存储边流量的键为 'flow'
# 原图G和剩余图R边容量值为 'capacity'

# Ford-Fulkson方法
def initialize_residual_g(G, F):
    # R can be initialized as G
    '''# 根据原图G和流图F计算剩余图R
    
    Params:
        G: nx.DiGraph 有向图
        F: 有向图 
    Return:
        R: a directed graph as Residual Graph
    '''
    R = nx.DiGraph()
    R.add_nodes_from(G.nodes)
    R.add_edges_from(G.edges)
    
    for e in G.edges:
        # 顺向剩余图 = 容量 - 流量 
        # 逆向 = 流量
        R.edges[e]['capacity'] = G.edges[e]['capacity'] - F.edges[e]['flow']
        if e[::-1] not in R.edges:
            R.add_edge(*e[::-1])
#            print("edges:", e, R.edges[e[::-1]])
        
        if 'capacity' not in R.edges[e[::-1]]:
            R.edges[e[::-1]]['capacity'] = 0
        R.edges[e[::-1]]['capacity'] += F.edges[e]['flow']
    return R

def update_residual_g(R, path, bottle_v):
    for i in range(len(path) - 1):
        R.edges[path[i], path[i+1]]['capacity'] -= bottle_v
        R.edges[path[i+1], path[i]]['capacity'] += bottle_v
    


# 在剩余图R（有向图）中寻找一条增广路径
def AnAugmentedPath(G, _s, _t):
    '''Find an augmented path in G
    
    Params:
        _s:
        _t:
    Return:
        path: (nodes list) empty if there exists no such path.
    '''
    # 用深度优先搜索寻找一条 _s -> _t的路径

    visted = defaultdict(bool)
    path = []
    
    def dfs(n, p):
        # 已经访问过的路径存在p 中
        # n is the node to be visted.
        visted[n] = True
        p.append(n)
        
        if n == _t:
            return True
        for anode in G.neighbors(n):
            if (not visted[anode]) and G.edges[n, anode]['capacity'] > 0 :
                if dfs(anode, p): 
                    return True
        
        visted[n] = False
        p.pop()
        return False
    if dfs(_s, path):
        return path
    else:
        return []

def print_graph(_G):
    for e in _G.edges:
        data = _G.edges[e]['capacity'] if 'capacity' in _G.edges[e] else _G.edges[e]['flow']
        print(e, ":", data)

    
def bottle_neck_v(path, _G):
    #图_G 路径path的瓶颈容量
    return min([_G.edges[path[i], path[i+1]]['capacity'] 
               for i in range(len(path)-1)])
    
# Ford-Fulkerson
def max_flow_fordfulkerson(G):
    '''返回有向图的最大流
    
    todo: 处理本方法不会终止的情况'''
    FlowG = nx.DiGraph()
    FlowG.add_nodes_from(G.nodes)
    FlowG.add_edges_from(G.edges)
    for e in G.edges:
        FlowG.edges[e]['flow'] = 0
        if e[::-1] not in FlowG.edges:
            FlowG.add_edge(*e[::-1])
        FlowG.edges[e[::-1]]['flow'] = 0
    
    R = initialize_residual_g(G, FlowG)
    while True:
        aug_path = AnAugmentedPath(R, 's', 't')
        if len(aug_path) == 0:
            break
        bottleneck_v = bottle_neck_v(aug_path, R)
        
        for i in range(len(aug_path) - 1):
            FlowG.edges[aug_path[i], aug_path[i+1]]['flow'] += bottleneck_v
        
        update_residual_g(R, aug_path, bottleneck_v)
    return FlowG

if __name__ == '__main__':
	# 算法书图16.3
	G = nx.DiGraph()
	G.add_edge('s', 'a', capacity=16)
	G.add_edge('s', 'b', capacity=13)
	G.add_edge('a', 'b', capacity=4)
	G.add_edge('b', 'a', capacity=10)
	G.add_edge('a', 'c', capacity=12)
	# G.add_edge('b', 'c', capacity=9)
	G.add_edge('b', 'd', capacity=14)
	G.add_edge('c', 'b', capacity=9)
	G.add_edge('d', 'c', capacity=7)
	G.add_edge('c', 't', capacity=20)
	G.add_edge('d', 't', capacity=4)
	nx.draw(G, with_labels=True)
	plt.show()

	f = (max_flow_fordfulkerson(G))
	print_graph(f)
