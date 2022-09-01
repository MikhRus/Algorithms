# Dictionary/hash-tab of graph
graph = {}
graph['start'] = {'a' : 6, 'b' : 2}
graph['a'] = {'fin' : 1}
graph['b'] = {'a' : 3}
graph['b'] = {'fin' : 5}
graph['fin'] = {}

# Dictionary/hash-tab of costs
# Infinity var
infinity = float('inf')
costs = {'a' : 6, 'b' : 2, 'fin' : infinity}

# Dictionary/hash-tab of parents
parents = {'a' : 'start', 'b' : 'start', 'fin' : None}

# List of process
processed = []

# Function for find cheaper cost node
def findLowestCostNode(costs):
    lowestCost = float('inf')
    lowestCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

def main(costs):
    node = findLowestCostNode(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            newCost = cost + neighbors[n]
            if costs[n] > newCost:
                costs[n] = newCost
                parents[n] = node
        processed.append(node)
        node = findLowestCostNode(costs)

main(costs)