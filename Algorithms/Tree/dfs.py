# Adjacency list of the above graph.
adjacency_list = {'Karlsruhe': ['Augsburg', 'Mannheim'],'Mannheim':['Karlsruhe', 'Frankfurt'],'Augsburg': ['Karlsruhe'], 'Würzburg': ['Nümberg', 'Erfurt', 'Frankfurt'], 'Kassel': ['München', 'Frankfurt'], 'München': ['Kassel'], 'Nümberg':['Stuttgart', 'Würzburg'], 'Erfurt':['Würzburg'],'Stuttgart':['Nümberg'], 'Frankfurt':['Mannheim', 'Würzburg', 'Kassel']}
adjacency_list = {3:[9, 20], 20:[15, 7, 3], 9:[3], 15:[20], 7:[20]}
graph=[["node1", "node2", "weight"]]

#for storing visited path.
visited_list = []

def dfs(node):
    if node not in visited_list:
        visited_list.append(node)
        for i in adjacency_list[node]:
            dfs(i)

dfs(3)
print(visited_list)