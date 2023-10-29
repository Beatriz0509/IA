
#STUDENT NAME:BEATRIZ FILIPA DA SILVA FERREIRA
#STUDENT NUMBER: 107214

#DISCUSSED TPI-1 WITH: (names and numbers): 

import math
from tree_search import *

class OrderDelivery(SearchDomain):

    def __init__(self, connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates

    def actions(self, state):
        city = state[0]
        actlist = []
        for (C1, C2, D) in self.connections:
            if C1 == city:
                actlist.append((C1, C2))
            elif C2 == city:
                actlist.append((C2, C1))
        return actlist

    def result(self, state, action):
        current_city = state[0]
        (C1, C2) = action
        if C1 == current_city:
            return (C2,)
        elif C2 == current_city:
            return (C1,)

    def satisfies(self, state, goal):
        city, destinations = state[0], state[1:]
        return city in destinations

    def cost(self, state, action):
        C1, C2 = action
        current_city = state[0]
        for (x1, x2, d) in self.connections:
            if (x1, x2) == action or (x2, x1) == action:
                return d

    def heuristic(self, state, goal):
        current_city, remaining_destinations = state[0], state[1:]

        if not remaining_destinations:
            return 0

        min_distance = float('inf')
        for dest in remaining_destinations:
            distance = self.cost(state, (current_city, dest))
            if distance < min_distance:
                min_distance = distance

        estimated_cost = min_distance
        for dest in remaining_destinations:
            if dest != goal:
                estimated_cost += self.cost((dest, *remaining_destinations), (goal,))

        return estimated_cost

 
class MyNode(SearchNode):
    def __init__(self, state, parent, depth=0, cost=0, heuristic=0):
        super().__init__(state, parent)
        self.depth = depth
        self.cost = cost
        self.heuristic = heuristic
        self.eval = cost + heuristic

class MyTree(SearchTree):
    def __init__(self, problem, strategy='breadth', maxsize=None):
        super().__init__(problem, strategy)
        self.maxsize = maxsize
        self.terminals = 0

    def astar_add_to_open(self, lnewnodes):
        nodes_with_eval = [node for node in lnewnodes if node.eval is not None]
        nodes_with_eval.sort(key=lambda node: (node.eval, node.state))
        self.open_nodes.extend(nodes_with_eval)
        nodes_without_eval = [node for node in lnewnodes if node.eval is None]
        self.open_nodes.extend(nodes_without_eval)

    def search2(self):
        while self.open_nodes:
            node = self.open_nodes.pop(0)

            if node.parent is None:
                node.depth = 0
                node.cost = 0
                node.heuristic = 0
                node.eval = node.cost + node.heuristic

            if self.problem.goal_test(node.state):
                self.terminals = len(self.open_nodes) + 1
                self.solution = node
                return self.get_path(node)

            self.non_terminals += 1
            lnewnodes = []

            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state, a)

                if newstate not in self.get_path(node):
                    newnode = MyNode(newstate, node)
                    newnode.depth = node.depth + 1
                    newnode.cost = node.cost + self.problem.domain.cost(node.state, a)
                    newnode.heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    newnode.eval = newnode.cost + newnode.heuristic
                    lnewnodes.append(newnode)

            if not lnewnodes:
                continue  
            if self.strategy == 'A*':
                self.astar_add_to_open(lnewnodes)
            else:
                self.add_to_open(lnewnodes)

            tree_size = len(self.open_nodes) + self.non_terminals

            if self.strategy == 'A*' and self.maxsize is not None and tree_size > self.maxsize:
                self.manage_memory()

        return None

    def manage_memory(self):
        to_remove = set()
        nodes_by_parent = {}
        self.open_nodes.sort(key=lambda node: (node.eval, node.state))

        for node in self.open_nodes:
            if node.parent and node.parent.eval:  
                parent = node.parent
                if parent not in nodes_by_parent:
                    nodes_by_parent[parent] = [node]
                else:
                    nodes_by_parent[parent].append(node)
                to_remove.add(node)

        for parent, children in nodes_by_parent.items():
            parent_evals = [n.eval for n in children if n.eval is not None]
            if parent_evals:
                parent.eval = min(parent_evals)
            else:
                parent.eval = None

def orderdelivery_search(domain, city, targetcities, strat='breadth', maxsize=None):
    problem = SearchProblem(domain, (city, *targetcities), city)
    tree = MyTree(problem, strategy=strat, maxsize=maxsize)
    path = tree.search2()

    return tree, path


def distance_between_cities(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# If needed, auxiliary functions can be added here