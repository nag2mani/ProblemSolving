# Adjacency list of the above graph.
adjacency_list = {'Karlsruhe': ['Augsburg', 'Mannheim'],'Mannheim':['Karlsruhe', 'Frankfurt'],'Augsburg': ['Karlsruhe'], 'Würzburg': ['Nümberg', 'Erfurt', 'Frankfurt'], 'Kassel': ['München', 'Frankfurt'], 'München': ['Kassel'], 'Nümberg':['Stuttgart', 'Würzburg'], 'Erfurt':['Würzburg'],'Stuttgart':['Nümberg'], 'Frankfurt':['Mannheim', 'Würzburg', 'Kassel']}
visited_list = []
def dfs(node):
    if node not in visited_list:
        visited_list.append(node)
        for i in adjacency_list[node]:
            dfs(i)