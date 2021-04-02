from prioritizator import Task

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
