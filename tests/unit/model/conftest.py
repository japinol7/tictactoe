import pytest


class CellSpriteMock:
    def __int__(self):
        self.frame_index = None


@pytest.fixture
def cell_sprite_mock():
    class CellSpriteFake:
        def __init__(self):
            self.frame_index = 1
    yield CellSpriteFake()


@pytest.fixture
def random_choice_board_cell(mocker):
    mocker.patch("random.choice",
                 side_effect=(1, 2),
                 )
