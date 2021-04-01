from prioritizator import Task


def test_Task():
    task = Task()
    obtained_rating = round(task.rating)
    expected_rating = 1500
    assert expected_rating == obtained_rating
