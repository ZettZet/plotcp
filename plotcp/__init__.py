__version__ = '0.2.4'

from enum import Flag, auto
from typing import Callable, Tuple, Iterator, Optional

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


# TODO Update new names to README.md
class Faxis(Flag):
    ORIG = auto()
    TRANSFORM = auto()
    BOTH = ORIG | TRANSFORM


class Reim(Flag):
    RE = auto()
    IM = auto()
    BOTH = RE | IM


class Inits(Flag):
    ORIG = auto()
    TRANSFORM = auto()
    BOTH = ORIG | TRANSFORM


# TODO Add docstring
def plotcp(
        fun: Callable[[complex], complex],
        x_bound: Tuple[int, int],
        y_bound: Tuple[int, int],
        n_steps: int = 100,
        grid_step: int = 10,
        init_points: Optional[Iterator] = None,
        faxis: Faxis = Faxis.BOTH,
        reim: Reim = Reim.BOTH,
        inits: Inits = Inits.BOTH,
        inits_only: bool = False,
):
    if inits_only and init_points is None:
        raise ValueError("'init_points' is None")

    fig, ax = plt.subplots()

    plt.xlim(x_bound)
    plt.ylim(y_bound)

    if init_points is not None:
        if inits & Inits.TRANSFORM:
            for init in init_points:
                fun_init = [fun(item) for item in init]
                fun_init_re = np.real(fun_init)
                fun_init_im = np.imag(fun_init)
                ax.plot(fun_init_re, fun_init_im, color='g')

        if inits & Inits.ORIG:
            for init in init_points:
                init_re = np.real(init)
                init_im = np.imag(init)
                ax.plot(init_re, init_im, color='g')

        if inits_only:
            return plt

    x_step = (x_bound[1] - x_bound[0]) / grid_step
    y_step = (y_bound[1] - y_bound[0]) / grid_step

    if faxis & Faxis.ORIG:
        if reim & Reim.RE:
            ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
            ax.grid(which='major', axis='y', color='b')

        if reim & Reim.IM:
            ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step))
            ax.grid(which='major', axis='x', color='tab:orange')

        if faxis != Faxis.BOTH:
            return plt

    if faxis & Faxis.TRANSFORM:
        x = np.linspace(x_bound[0], x_bound[1], 2 * grid_step)
        y = np.linspace(y_bound[0], y_bound[1], 2 * grid_step)

        if reim & Reim.RE:
            x_parallels = [[item_x + item_y * 1j for item_x in np.linspace(x_bound[0], x_bound[1], n_steps)] for item_y
                           in y]
            u = [[fun(item) for item in xs] for xs in x_parallels]
            u_re = [np.real(us) for us in u]
            u_im = [np.imag(us) for us in u]

            for r, i in zip(u_re, u_im):
                ax.plot(r, i, color='b')

        if reim & Reim.IM:
            y_parallels = [[item_x + item_y * 1j for item_y in np.linspace(y_bound[0], y_bound[1], n_steps)] for item_x
                           in x]
            v = [[fun(item) for item in ys] for ys in y_parallels]
            v_re = [np.real(vs) for vs in v]
            v_im = [np.imag(vs) for vs in v]

            for r, i in zip(v_re, v_im):
                ax.plot(r, i, color='tab:orange')

    return plt
