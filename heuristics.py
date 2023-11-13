class Heuristic:
    def get_evaluation(self, state):
        pass


class ExampleHeuristic(Heuristic):
    def get_evaluation(self, state):
        return 0


class Hamming(Heuristic):
    def get_evaluation(self, state):
        hamming = 0
        final_state = []
        for i in range(1, len(state)):
            final_state.append(i)
        final_state.append(0)
        final_state = tuple(final_state)

        for i in range(len(state)):
            if state.index(i) != final_state.index(i):
                hamming = hamming + 1
        return hamming


class Manhattan(Heuristic):
    def get_evaluation(self, state):
        state = list(state)
        size = int(len(state) / 2)
        final_state = []
        manhattan_distance = 0

        for i in range(1, len(state)):
            final_state.append(i)
        final_state.append(0)

        for piece in state:
            goal_index = final_state.index(piece)
            current_index = state.index(piece)

            goal_position = divmod(goal_index, size)
            current_position = divmod(current_index, size)

            manhattan_distance += (abs(current_position[0] - goal_position[0])
                                   + abs(current_position[1] - goal_position[1]))

        return manhattan_distance
