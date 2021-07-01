from prioritizator import Task


def test_set_and_get_title():
    task = Task(id=1)
    expected_title = "Hola Mundo"
    task._set_title(expected_title)
    obtained_title = task._get_title()
    assert expected_title == obtained_title
    expected_title = "Figura circular Objetivos Desarrollo Sostenible ONU"
    task._set_title(expected_title)
    obtained_title = task._get_title()
    assert expected_title == obtained_title


def test_update_rating_on_github():
    task = Task(id=1)
    task.update_rating_on_github()
    obtained_title = task._get_title()
    expected_title = "[1500] Figura circular Objetivos Desarrollo Sostenible ONU"
    assert expected_title == obtained_title
