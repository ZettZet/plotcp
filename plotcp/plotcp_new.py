from typing import Callable, Optional

import plotly.graph_objs as go
import numpy as np
from numpy.typing import ArrayLike

from plotcp import Reim


def plotcp_plotly(
        fun: Callable[[ArrayLike], ArrayLike],
        x_bound: tuple[int, int],
        y_bound: tuple[int, int],
        *,
        n_steps: int = 100,
        reim: Reim = Reim.BOTH,
        fig: Optional[go.Figure] = None
) -> go.Figure:
    """
    :param fun: your predefined function f(z)
    :param x_bound: real plot bounds
    :param y_bound: imaginary plot bounds
    :param n_steps: how many nodes will be on each line
    :param reim: which part to display: 'real', 'imag' or 'both' (named constants, correspondingly: Reim.RE, Reim.IM,
    Reim.BOTH) (only works with grid lines, and not areas)
    Inits.TRANSFORM, Inits.BOTH)
    :param fig: Figure object to plot on
    :return: plotly Figure object
    """
    if fig is None:
        fig = go.Figure()

    fig.update_xaxes(range=x_bound, showgrid=True, gridwidth=1, gridcolor='orange', zeroline=True, zerolinewidth=2,
                     zerolinecolor='orange')
    fig.update_yaxes(range=y_bound, showgrid=True, gridwidth=1, gridcolor='blue', zeroline=True, zerolinewidth=2,
                     zerolinecolor='blue')

    match reim:
        case Reim.IM:
            fig = __add_imag(fig, fun, x_bound, y_bound, n_steps)
        case Reim.RE:
            fig = __add_real(fig, fun, x_bound, y_bound, n_steps)
        case Reim.BOTH:
            fig = __add_imag(fig, fun, x_bound, y_bound, n_steps)
            fig = __add_real(fig, fun, x_bound, y_bound, n_steps)

    return fig


def __add_imag(fig: go.Figure, fun: Callable[[ArrayLike], ArrayLike], x_bound: tuple[int, int],
               y_bound: tuple[int, int], n_steps: int) -> go.Figure:
    x_l, x_r = x_bound
    y_l, y_r = y_bound
    real_fixed = np.arange(x_l, x_r + 1)
    imag = np.linspace(y_l, y_r, n_steps)
    parallel_to_imag = np.array([re + 1j * imag for re in real_fixed])

    for line in parallel_to_imag:
        f_parallel_imag = fun(line)
        fig.add_trace(
            go.Scatter(x=np.real(f_parallel_imag), y=np.imag(f_parallel_imag), name=f'{np.real(line[0])}',
                       line={'color': 'orange'}))

    return fig


def __add_real(fig: go.Figure, fun: Callable[[ArrayLike], ArrayLike], x_bound: tuple[int, int],
               y_bound: tuple[int, int], n_steps: int) -> go.Figure:
    x_l, x_r = x_bound
    y_l, y_r = y_bound
    imag_fixed = np.arange(y_l, y_r + 1)
    real = np.linspace(x_l, x_r, n_steps)
    parallel_to_real = np.array([real + 1j * im for im in imag_fixed])

    for line in parallel_to_real:
        f_parallel_real = fun(line)

        fig.add_trace(
            go.Scatter(x=np.real(f_parallel_real), y=np.imag(f_parallel_real), name=f'{1j * np.imag(line[0])}',
                       line={'color': 'blue'}))

    return fig
