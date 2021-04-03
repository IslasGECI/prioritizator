from os import remove
from prioritizator import Matcher
from prioritizator import Task
from shutil import copyfile

WHITE_WINS = 1
DRAW = 0.5
WHITE_LOSES = 0


def test_match_existing_tasks():
    data_path = "tests/test_data/test_save_task_list.csv"
    copyfile("tests/test_data/test_load_task_list.csv", data_path)
    matcher = Matcher()
    matcher.match(white=1, black=2, outcome=WHITE_WINS, data_path=data_path)
