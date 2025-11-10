import plotly.graph_objects as go
from bearish.database.crud import BearishDb

from mysec.figures import plot_sec_data, add_trace
from mysec.queries import exited_positions, total_increase, total_decrease


def test_exit(bearish_db: BearishDb) -> None:
    fig = go.Figure()
    data = exited_positions(bearish_db)
    fig = add_trace(fig, data)
    assert data.valid()
    assert fig
    fig.show()


def test_increase(bearish_db: BearishDb) -> None:
    fig = go.Figure()
    data = total_increase(bearish_db)
    fig = add_trace(fig, data)
    assert data.valid()
    assert fig
    fig.show()


def test_plot_sec_data(bearish_db: BearishDb) -> None:
    fig = go.Figure()
    decrease = total_decrease(bearish_db)
    increase = total_increase(bearish_db)
    fig = plot_sec_data(fig, [increase, decrease])
    assert fig
    assert decrease.valid()
    assert increase.valid()
    fig.show()
