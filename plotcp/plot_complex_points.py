from typing import Iterator, Optional

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go


def plot_complex_points(init_points: Iterator[complex], *, ax: Optional[Axes] = None) -> Axes:
    """
    Plot complex points
    :param init_points: values to be plotted
    :param ax: Axes object to plot on
    :return: matplotlib Axes object
    """
    if ax is None:
        fig, ax = plt.subplots()
    ax.plot(np.real(init_points), np.imag(init_points), color='g')
    return ax


def plot_complex_points_plotly(init_points: Iterator[complex], *, name: str, color: str = 'green',
                        fig: Optional[go.Figure] = None) -> go.Figure:
    """
    Plot complex points
    :param color:
    :param name: name of a line
    :param init_points: values to be plotted
    :param fig: Figure object to plot on
    :return: plotly Figure object
    """
    if fig is None:
        fig = go.Figure()

    fig.add_trace(go.Scatter(x=np.real(init_points), y=np.imag(init_points), name=name, line={'color': color}))

    return fig
