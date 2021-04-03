from os import remove
from prioritizator import Matcher
from prioritizator import Task
from shutil import copyfile

WHITE_WINS = 1
DRAW = 0.5
WHITE_LOSES = 0


def test_constructor_0_arguments():
    matcher = Matcher()
    obtained_data_path = matcher.data_path
    expected_data_path = None
    assert obtained_data_path == expected_data_path


def test_setting_data_path():
    data_path = "tests/test_data/test_load_task_list.csv"
    matcher = Matcher()
    matcher.data_path = data_path
    obtained_data_path = matcher.data_path
    expected_data_path = data_path
    assert obtained_data_path == expected_data_path


def test_constructor_1_argument():
    data_path = "tests/test_data/test_load_task_list.csv"
    matcher = Matcher(data_path)
    obtained_data_path = matcher.data_path
    expected_data_path = data_path
    assert obtained_data_path == expected_data_path


def test_match_existing_tasks():
    data_path = "tests/test_data/test_save_task_list.csv"
    copyfile("tests/test_data/test_load_task_list.csv", data_path)
    matcher = Matcher(data_path)
    matcher.match(white=1, black=2, outcome=WHITE_WINS)
    remove(data_path)
