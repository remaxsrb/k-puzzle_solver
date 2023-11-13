import random
import time

import config
from collections import deque
from queue import PriorityQueue


class Algorithm:
    def __init__(self, heuristic=None):
        self.heuristic = heuristic
        self.nodes_evaluated = 0
        self.nodes_generated = 0

    def get_legal_actions(self, state):
        self.nodes_evaluated += 1
        max_index = len(state)
        zero_tile_ind = state.index(0)
        legal_actions = []
        if 0 <= (up_ind := (zero_tile_ind - config.N)) < max_index:
            legal_actions.append(up_ind)
        if 0 <= (right_ind := (zero_tile_ind + 1)) < max_index and right_ind % config.N:
            legal_actions.append(right_ind)
        if 0 <= (down_ind := (zero_tile_ind + config.N)) < max_index:
            legal_actions.append(down_ind)
        if 0 <= (left_ind := (zero_tile_ind - 1)) < max_index and (left_ind + 1) % config.N:
            legal_actions.append(left_ind)
        return legal_actions

    def apply_action(self, state, action):
        self.nodes_generated += 1
        copy_state = list(state)
        zero_tile_ind = state.index(0)
        copy_state[action], copy_state[zero_tile_ind] = copy_state[zero_tile_ind], copy_state[action]
        return tuple(copy_state)

    def get_steps(self, initial_state, goal_state):
        pass

    def get_solution_steps(self, initial_state, goal_state):
        begin_time = time.time()
        solution_actions = self.get_steps(initial_state, goal_state)
        print(f'Execution time in seconds: {(time.time() - begin_time):.2f} | '
              f'Nodes generated: {self.nodes_generated} | '
              f'Nodes evaluated: {self.nodes_evaluated}')
        return solution_actions


class ExampleAlgorithm(Algorithm):
    def get_steps(self, initial_state, goal_state):
        state = initial_state
        solution_actions = []
        while state != goal_state:
            legal_actions = self.get_legal_actions(state)
            action = legal_actions[random.randint(0, len(legal_actions) - 1)]
            solution_actions.append(action)
            state = self.apply_action(state, action)
        return solution_actions


class Node:
    def __init__(self, state, actions, path_length=0, parent_node=None):
        self.state = state
        self.actions = actions
        self.path_length = path_length
        self.parent_node = parent_node

    def get_state(self):
        return self.state

    def get_actions(self):
        return self.actions

    def get_path_length(self):
        return self.path_length

    def get_parent_node(self):
        return self.parent_node

    def __lt__(self, other):
        return self.state < other.state


class BFS(Algorithm):
    def get_steps(self, initial_state, goal_state):

        queue = deque()
        visited = set()
        solution_actions = []
        node = Node(initial_state, solution_actions)
        queue.appendleft(node)

        while queue:
            popped = queue.popleft()
            popped_state = popped.get_state()
            popped_actions = popped.get_actions()

            legal_actions = self.get_legal_actions(popped_state)
            for legal_action in legal_actions:
                new_state = self.apply_action(popped_state, legal_action)

                if new_state == goal_state:
                    popped_actions.append(legal_action)
                    return popped_actions

                if new_state in visited:
                    pass
                else:
                    visited.add(new_state)
                    updated_actions = popped_actions.copy()  # Due to python's mechanics this can not be simple
                    # assignment, we want a deep not a shallow copy
                    updated_actions.append(legal_action)
                    new_node = Node(new_state, updated_actions)
                    queue.append(new_node)


class BestFirstSearch(Algorithm):
    def get_steps(self, initial_state, goal_state):

        queue = PriorityQueue()
        visited = set()
        solution_actions = []
        node = Node(initial_state, solution_actions)
        queue.put((self.heuristic.get_evaluation(initial_state), node))
        while queue:
            popped = queue.get()
            popped_node = popped[1]

            popped_state = popped_node.get_state()
            popped_actions = popped_node.get_actions()

            legal_actions = self.get_legal_actions(popped_state)
            for legal_action in legal_actions:
                new_state = self.apply_action(popped_state, legal_action)

                if new_state == goal_state:
                    popped_actions.append(legal_action)
                    return popped_actions

                if new_state in visited:
                    pass
                else:
                    visited.add(new_state)
                    updated_actions = popped_actions.copy()
                    updated_actions.append(legal_action)
                    new_node = Node(new_state, updated_actions)
                    queue.put((self.heuristic.get_evaluation(new_state), new_node))



