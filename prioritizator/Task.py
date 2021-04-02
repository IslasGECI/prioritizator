import glicko2


class Task:
    def __init__(self):
        self._player = glicko2.Player()

    @property
    def rating(self):
        return self._player.rating

    def match(self, opponent_task, outcome):
        self_rating = self.rating
        opponent_rating = opponent_task.rating
        self_rd = self._player.rd
        opponent_rd = opponent_task._player.rd
        self._player.update_player([opponent_rating], [opponent_rd], [outcome])
        opponent_task._player.update_player([self_rating], [self_rd], [1 - outcome])
        return self, opponent_task
