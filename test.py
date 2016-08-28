import grid
def test_initialise():
    grid=grid_life([[1,1],[1,0]])
    assert grid.result==([[0,0],[0,0]])
