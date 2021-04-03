from prioritizator import Task


class Matcher:
    def __init__(self, data_path=None):
        self.data_path = data_path

    def match(self, white_id, black_id, outcome):
        white_task = Task(id=white_id).load_from_csv(self.data_path)
        black_task = Task(id=black_id).load_from_csv(self.data_path)
        white_task.match(black_task, outcome)
        white_task.save_to_csv(self.data_path)
        black_task.save_to_csv(self.data_path)
