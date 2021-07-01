from os import remove
from prioritizator import Matcher
from prioritizator import Task
from shutil import copyfile

WHITE_WINS = 1
DRAW = 0.5
WHITE_LOSES = 0


def assert_data_path(matcher, data_path):
    obtained_data_path = matcher.data_path
    expected_data_path = data_path
    assert obtained_data_path == expected_data_path


def test_constructor_0_arguments():
    matcher = Matcher()
    assert_data_path(matcher, None)


def test_setting_data_path():
    data_path = "tests/test_data/test_load_task_list.csv"
    matcher = Matcher()
    matcher.data_path = data_path
    assert_data_path(matcher, data_path)


def test_constructor_1_argument():
    data_path = "tests/test_data/test_load_task_list.csv"
    matcher = Matcher(data_path)
    assert_data_path(matcher, data_path)


def test_match_existing_tasks():
    data_path = "tests/test_data/test_save_task_list.csv"
    copyfile("tests/test_data/test_load_task_list.csv", data_path)
    white_id = 1
    white_task = Task(id=white_id).load_from_csv(data_path)
    obtained_white_rating_before = white_task.rating
    expected_white_rating_before = 1000
    assert expected_white_rating_before == obtained_white_rating_before
    black_id = 2
    black_task = Task(id=black_id).load_from_csv(data_path)
    obtained_black_rating_before = black_task.rating
    expected_black_rating_before = 2000
    assert expected_black_rating_before == obtained_black_rating_before
    matcher = Matcher(data_path)
    matcher.match(white_id=white_id, black_id=black_id, outcome=WHITE_WINS)
    white_task.load_from_csv(data_path)
    obtained_white_rating_after = white_task.rating
    assert obtained_white_rating_after > obtained_white_rating_before
    black_task.load_from_csv(data_path)
    obtained_black_rating_after = black_task.rating
    assert obtained_black_rating_after < obtained_black_rating_before
    remove(data_path)


def test_match_new_tasks():
    data_path = "tests/test_data/test_save_task_list.csv"
    copyfile("tests/test_data/test_load_task_list.csv", data_path)
    white_id = 5
    white_task = Task(id=white_id)
    obtained_white_rating_before = white_task.rating
    expected_white_rating_before = 1500
    assert expected_white_rating_before == obtained_white_rating_before
    black_id = 6
    black_task = Task(id=black_id)
    obtained_black_rating_before = black_task.rating
    expected_black_rating_before = 1500
    assert expected_black_rating_before == obtained_black_rating_before
    matcher = Matcher(data_path)
    matcher.match(white_id=white_id, black_id=black_id, outcome=WHITE_LOSES)
    white_task.load_from_csv(data_path)
    obtained_white_rating_after = white_task.rating
    assert obtained_white_rating_after < obtained_white_rating_before
    black_task.load_from_csv(data_path)
    obtained_black_rating_after = black_task.rating
    assert obtained_black_rating_after > obtained_black_rating_before
    remove(data_path)
