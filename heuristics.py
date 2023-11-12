class Heuristic:
    def get_evaluation(self, state):
        pass


class ExampleHeuristic(Heuristic):
    def get_evaluation(self, state):
        return 0


class Hamming(Heuristic):
    def get_evaluation(self, state):
        hamming = 0
        final_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        for i in 8:
            if state[i] == final_state[i]:
                hamming = hamming + 1


class Manhattan(Heuristic):
    def get_evaluation(self, state):
        manhattan = 0
        final_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
