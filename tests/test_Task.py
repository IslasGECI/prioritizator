from os import remove
from prioritizator import Task
from shutil import copyfile

WIN = 1
DRAW = 0.5
LOSS = 0


def test_constructor_0_arguments():
    task = Task()
    obtained_rating = round(task.rating)
    expected_rating = 1500
    assert expected_rating == obtained_rating
    obtained_rd = round(task._rd)
    expected_rd = 350
    assert expected_rd == obtained_rd
    obtained_id = task._id
    expected_id = None
    assert expected_id == obtained_id


def test_match_win():
    task_1 = Task()
    task_2 = Task()
    task_1.match(task_2, WIN)
    assert task_1.rating > task_2.rating
    assert round(task_1.rating) == 1662
    assert round(task_2.rating) == 1338


def test_match_draw():
    task_1 = Task()
    task_2 = Task()
    task_1.match(task_2, DRAW)
    assert task_1.rating == task_2.rating
    assert round(task_1.rating) == 1500
    assert round(task_2.rating) == 1500


def test_match_loss():
    task_1 = Task()
    task_2 = Task()
    task_1.match(task_2, LOSS)
    assert task_1.rating < task_2.rating
    assert round(task_1.rating) == 1338
    assert round(task_2.rating) == 1662


def test_rd_decrease():
    task_1 = Task()
    task_2 = Task()
    rd_before = task_1._rd
    task_1.match(task_2, DRAW)
    rd_after = task_1._rd
    assert rd_before > rd_after
    assert round(rd_before) == 350
    assert round(rd_after) == 290


def test_constructor_1_argument():
    expected_rating = 2000
    task = Task(expected_rating)
    obtained_rating = round(task.rating)
    assert expected_rating == obtained_rating
    obtained_rd = task._rd
    expected_rd = 350
    assert expected_rd == obtained_rd


def test_constructor_2_arguments():
    expected_rating = 1000
    expected_rd = 100
    task = Task(expected_rating, expected_rd)
    obtained_rating = round(task.rating)
    assert expected_rating == obtained_rating
    obtained_rd = round(task._rd)
    assert expected_rd == obtained_rd


def test_constructor_3_arguments():
    expected_rating = 1750
    expected_rd = 50
    expected_id = 2
    task = Task(expected_rating, expected_rd, expected_id)
    obtained_rating = round(task.rating)
    assert expected_rating == obtained_rating
    obtained_rd = round(task._rd)
    assert expected_rd == obtained_rd
    obtained_id = task._id
    assert expected_id == obtained_id


def test_constructor_arguments_out_of_order():
    expected_rating = 1750
    expected_rd = 50
    expected_id = 2
    task = Task(id=expected_id, rating=expected_rating, rd=expected_rd)
    obtained_rating = round(task.rating)
    assert expected_rating == obtained_rating
    obtained_rd = round(task._rd)
    assert expected_rd == obtained_rd
    obtained_id = task._id
    assert expected_id == obtained_id


def test_constructor_only_id():
    expected_id = 2
    task = Task(id=expected_id)
    obtained_rating = round(task.rating)
    expected_rating = 1500
    assert expected_rating == obtained_rating
    obtained_rd = round(task._rd)
    expected_rd = 350
    assert expected_rd == obtained_rd
    obtained_id = task._id
    assert expected_id == obtained_id


def test_load_task():
    expected_id = 2
    task = Task(id=expected_id)
    task.load_from_csv("tests/test_data/test_load_task_list.csv")
    obtained_id = task._id
    assert expected_id == obtained_id
    obtained_rating = round(task.rating)
    expected_rating = 2000
    assert expected_rating == obtained_rating
    obtained_rd = round(task._rd)
    expected_rd = 200
    assert expected_rd == obtained_rd


def test_save_existing_task():
    data_path = "tests/test_data/test_save_task_list.csv"
    copyfile("tests/test_data/test_load_task_list.csv", data_path)
    with open(data_path) as data_file:
        header_before = data_file.readline()
    expected_id = 2
    expected_rating = 1250
    expected_rd = 25
    task_1 = Task(id=expected_id, rating=expected_rating, rd=expected_rd)
    task_1.save_to_csv(data_path)
    task_2 = Task(id=expected_id)
    obtained_initial_rating = round(task_2.rating)
    expected_initial_rating = 1500
    assert expected_initial_rating == obtained_initial_rating
    task_2.load_from_csv(data_path)
    obtained_id = task_2._id
    assert expected_id == obtained_id
    obtained_rating = round(task_2.rating)
    assert expected_rating == obtained_rating
    obtained_rd = round(task_2._rd)
    assert expected_rd == obtained_rd
    with open(data_path) as data_file:
        header_after = data_file.readline()
    assert header_after == header_before
    remove(data_path)


def test_save_new_task():
    data_path = "tests/test_data/test_save_task_list.csv"
    copyfile("tests/test_data/test_load_task_list.csv", data_path)
    with open(data_path) as data_file:
        header_before = data_file.readline()
    expected_id = 4
    expected_rating = 1234
    expected_rd = 123
    task_1 = Task(id=expected_id, rating=expected_rating, rd=expected_rd)
    task_1.save_to_csv(data_path)
    task_2 = Task(id=expected_id)
    obtained_initial_rating = round(task_2.rating)
    expected_initial_rating = 1500
    assert expected_initial_rating == obtained_initial_rating
    task_2.load_from_csv(data_path)
    obtained_id = task_2._id
    assert expected_id == obtained_id
    obtained_rating = round(task_2.rating)
    assert expected_rating == obtained_rating
    obtained_rd = round(task_2._rd)
    assert expected_rd == obtained_rd
    with open(data_path) as data_file:
        header_after = data_file.readline()
    assert header_after == header_before
    remove(data_path)


def test_add_rating_to_string():
    original_string = "Hola Mundo"
    task = Task()
    obtained_string = task.add_rating_to_string(original_string)
    expected_string = "[1500] Hola Mundo"
    assert expected_string == obtained_string


def test_update_rating_in_string():
    original_string = "[123] Hola Mundo"
    task = Task()
    obtained_string = task.update_rating_in_string(original_string)
    expected_string = "[1500] Hola Mundo"
    assert expected_string == obtained_string


def test_add_or_update_rating_in_string_without_rating():
    original_string = "Hola Mundo"
    task = Task()
    obtained_string = task.add_or_update_rating_in_string(original_string)
    expected_string = "[1500] Hola Mundo"
    assert expected_string == obtained_string


def test_add_or_update_rating_in_string_with_rating():
    original_string = "[123] Hola Mundo"
    task = Task()
    obtained_string = task.add_or_update_rating_in_string(original_string)
    expected_string = "[1500] Hola Mundo"
    assert expected_string == obtained_string
