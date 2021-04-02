from prioritizator import Task

WIN = 1
DRAW = 0.5
LOSS = 0

def test_rating():
    task = Task()
    obtained_rating = round(task.rating)
    expected_rating = 1500
    assert expected_rating == obtained_rating

def test_match_win():
    task_1 = Task()
    task_2 = Task()
    task_1.match(task_2,WIN)
    assert task_1.rating > task_2.rating
    assert round(task_1.rating) == 1662
    assert round(task_2.rating) == 1338

def test_match_draw():
    task_1 = Task()
    task_2 = Task()
    task_1.match(task_2,DRAW)
    assert task_1.rating == task_2.rating
    assert round(task_1.rating) == 1500
    assert round(task_2.rating) == 1500

def test_match_loss():
    task_1 = Task()
    task_2 = Task()
    task_1.match(task_2,LOSS)
    assert task_1.rating < task_2.rating
    assert round(task_1.rating) == 1338
    assert round(task_2.rating) == 1662
