import glicko2


def test_glicko2():
    player = glicko2.Player()
    assert isinstance(player, glicko2.glicko2.Player)
