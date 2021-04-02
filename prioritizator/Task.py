import glicko2


class Task:
    def __init__(self, rating=1500, rd=350, id=None):
        self._player = glicko2.Player(rating, rd)
        self._id = id

    @property
    def rating(self):
        return self._player.rating

    @property
    def _rd(self):
        return self._player.rd

    def match(self, opponent_task, outcome):
        self_rating = self.rating
        opponent_rating = opponent_task.rating
        self_rd = self._player.rd
        opponent_rd = opponent_task._player.rd
        self._player.update_player([opponent_rating], [opponent_rd], [outcome])
        opponent_task._player.update_player([self_rating], [self_rd], [1 - outcome])
        return self, opponent_task
