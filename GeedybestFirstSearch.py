import heapq

h = {'A':7,'B':6,'C':5,'D':2,'G':0}
graph = {'A':['B','C'], 'B':['D'], 'D':['G'], 'C':['G'], 'G':[]}

pq = [(h['A'], 'A')]
visited = set()

while pq:
    _, n = heapq.heappop(pq)
    if n in visited: continue
    print(n)
    visited.add(n)
    if n == 'G': break
    for nxt in graph[n]:
        heapq.heappush(pq, (h[nxt], nxt))
