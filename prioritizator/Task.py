import csv
import glicko2
import pandas as pd


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

    def load_from_csv(self, data_path):
        self_id = self._id
        with open(data_path, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                file_id = int(row["id"])
                if file_id == self_id:
                    self._player.rating = float(row["rating"])
                    self._player.rd = float(row["rd"])
                    return self
            raise LookupError(f"Task {self_id} not found")

    def save_to_csv(self, data_path):
        task_list = pd.read_csv(data_path)
        task_list = task_list
        is_id = task_list.id == self._id
        task_list.loc[is_id, "rating"] = self.rating
        task_list.loc[is_id, "rd"] = self._rd
        task_list.to_csv(data_path, index=False)
