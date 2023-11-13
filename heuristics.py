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
        manhattan = 0
