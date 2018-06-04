# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node

        stack, visited = [node], {}
        new_nodes = {}

        while stack:
            cur = stack.pop(0)
            if cur.label in new_nodes:
                new_node = new_nodes[cur.label]
            else:
                new_node = UndirectedGraphNode(cur.label)
                new_nodes[cur.label] = new_node

            for neigh in cur.neighbors:
                if neigh.label == cur.label:
                    new_node.neighbors.append(new_node)
                else:
                    if neigh.label in new_nodes:
                        next_node = new_nodes[neigh.label]
                    else:
                        next_node = UndirectedGraphNode(neigh.label)
                        new_nodes[neigh.label] = next_node
                        stack.append(neigh)
                    new_node.neighbors.append(next_node)
            visited[cur.label] = 1
        return new_nodes[node.label]

    def cloneGraph2(self, node):
        clones = {}

        def clone(node):
            if not node:
                return node
            if node.label in clones:
                return clones[node.label]

            new = UndirectedGraphNode(node.label)
            clones[node.label] = new

            for cur in node.neighbors:
                new.neighbors.append(clone(cur))
            return new

        return clone(node)
