from prioritizator import Task


def test_set_and_get_title():
    task = Task(id=1)
    expected_title = "Hola Mundo"
    obtained_title = task._set_title(expected_title)
    obtained_title = task._get_title()
    assert expected_title == obtained_title
    expected_title = "Figura circular Objetivos Desarrollo Sostenible ONU"
    obtained_title = task._set_title(expected_title)
    obtained_title = task._get_title()
    assert expected_title == obtained_title
