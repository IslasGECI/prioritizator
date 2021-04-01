from prioritizator import Task


def test_rating():
    task = Task()
    obtained_rating = round(task.rating)
    expected_rating = 1500
    assert expected_rating == obtained_rating

def test_match():
    task_1 = Task()
    task_2 = Task()
    task_1.match(task_2,1)
    assert task_1.rating > task_2.rating
