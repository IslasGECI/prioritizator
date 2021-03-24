import glicko2


def test_glicko2():
    player1 = glicko2.Player()
    assert isinstance(player1, glicko2.glicko2.Player)
