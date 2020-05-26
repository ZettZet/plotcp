__version__ = '0.2.3'

from enum import Flag, auto
from typing import Callable, Tuple, Iterator, Optional

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


class Faxis(Flag):
    ORIG = auto()
    TRANSF = auto()
    BOTH = ORIG | TRANSF


class Reim(Flag):
    RE = auto()
    IM = auto()
    BOTH = RE | IM


class Inits(Flag):
    ORIG = auto()
    TRANSF = auto()
    BOTH = ORIG | TRANSF


def plotcp(
        fun: Callable[[complex], complex],
        xbound: Tuple[int, int],
        ybound: Tuple[int, int],
        nsteps: int = 100,
        gridstep: int = 10,
        inits_point: Optional[Iterator] = None,
        faxis: Faxis = Faxis.BOTH,
        reim: Reim = Reim.BOTH,
        inits: Inits = Inits.BOTH,
        inits_only: bool = False,
):
    if inits_only and inits_point is None:
        raise ValueError("'inits_point' is None")

    fig, ax = plt.subplots()

    plt.xlim(xbound)
    plt.ylim(ybound)

    if inits_point is not None:
        if inits == Inits.TRANSF or inits == Inits.BOTH:
            for init in inits_point:
                fun_init = [fun(item) for item in init]
                fun_init_re = np.real(fun_init)
                fun_init_im = np.imag(fun_init)
                ax.plot(fun_init_re, fun_init_im, color='g')

        if inits == Inits.ORIG or inits == Inits.BOTH:
            for init in inits_point:
                init_re = np.real(init)
                init_im = np.imag(init)
                ax.plot(init_re, init_im, color='g')
        
        if inits_only:
            return plt

    x_step = (xbound[1] - xbound[0]) / gridstep
    y_step = (ybound[1] - ybound[0]) / gridstep

    if faxis == Faxis.ORIG or faxis == Faxis.BOTH:
        if reim == Reim.RE or reim == Reim.BOTH:
            ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
            ax.grid(which='major', axis='y', color='b')
        
        if reim == Reim.IM or reim == Reim.BOTH:
            ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step))
            ax.grid(which='major', axis='x', color='tab:orange')
        
        if faxis != Faxis.BOTH:
            return plt

    u_re = []
    u_im = []
    v_re = []
    v_im = []

    if faxis == Faxis.TRANSF or faxis == Faxis.BOTH:
        x = np.linspace(xbound[0], xbound[1], 2 * gridstep)
        y = np.linspace(ybound[0], ybound[1], 2 * gridstep)

        if reim == Reim.RE or reim == Reim.BOTH:
            x_parallels = [[item_x + item_y * 1j for item_x in np.linspace(xbound[0], xbound[1], nsteps)] for item_y
                            in y]
            u = [[fun(item) for item in xs] for xs in x_parallels]
            u_re = [np.real(us) for us in u]
            u_im = [np.imag(us) for us in u]

            for r, i in zip(u_re, u_im):
                ax.plot(r, i, color='b')


        if reim == Reim.IM or reim == Reim.BOTH:
            y_parallels = [[item_x + item_y * 1j for item_y in np.linspace(ybound[0], ybound[1], nsteps)] for item_x
                            in x]
            v = [[fun(item) for item in ys] for ys in y_parallels]
            v_re = [np.real(vs) for vs in v]
            v_im = [np.imag(vs) for vs in v]

            for r, i in zip(v_re, v_im):
                ax.plot(r, i, color='tab:orange')

    return plt
