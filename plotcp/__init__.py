__version__ = '0.2.0'

from typing import Callable

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

I = 1j

ORIG = 'origin'
TRANSF = 'transform'
RE = 'real'
IM = 'imag'
BOTH = 'both'


def re(z: complex) -> float:
    return z.real


def im(z: complex) -> float:
    return z.imag


def plotcp(
        fun: Callable[[complex], complex],
        xbound,
        ybound,
        nsteps: int = 100,
        gridstep: int = 10,
        inits_point=None,
        faxis: str = BOTH,
        reim: str = BOTH,
        inits_only: bool = False,
):
    if inits_only is True and inits_point is None:
        raise ValueError("'inits_point' is None")

    if faxis not in [ORIG, TRANSF, BOTH]:
        raise ValueError("'faxis' must be 'origin', 'transform' or 'both'")

    if reim not in [RE, IM, BOTH]:
        raise ValueError("'reim' must be 'real', 'imag' or 'both'")

    fig, ax = plt.subplots()

    x_step = (xbound[1] - xbound[0]) / gridstep
    y_step = (ybound[1] - ybound[0]) / gridstep

    u_re = []
    u_im = []
    v_re = []
    v_im = []

    if not inits_only:
        if faxis == TRANSF or faxis == BOTH:
            x = np.linspace(xbound[0], xbound[1], 2 * gridstep)
            y = np.linspace(ybound[0], ybound[1], 2 * gridstep)

            if reim == RE or reim == BOTH:
                x_parallels = [[item_x + item_y * I for item_x in np.linspace(xbound[0], xbound[1], nsteps)] for item_y
                               in y]
                u = [[fun(item) for item in xs] for xs in x_parallels]
                u_re = [np.array([re(item) for item in us]) for us in u]
                u_im = [np.array([im(item) for item in us]) for us in u]

            if reim == IM or reim == BOTH:
                y_parallels = [[item_x + item_y * I for item_y in np.linspace(ybound[0], ybound[1], nsteps)] for item_x
                               in x]
                v = [[fun(item) for item in ys] for ys in y_parallels]
                v_re = [np.array([re(item) for item in vs]) for vs in v]
                v_im = [np.array([im(item) for item in vs]) for vs in v]

        if reim == RE:
            if faxis == ORIG:
                ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
                ax.grid(which='major', axis='y', color='b')

            elif faxis == TRANSF:
                for r, i in zip(u_re, u_im):
                    ax.plot(r, i, color='b')

            else:
                ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
                ax.grid(which='major', axis='y', color='b')
                for r, i in zip(u_re, u_im):
                    ax.plot(r, i, color='b')

        elif reim == IM:
            if faxis == ORIG:
                ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step))
                ax.grid(which='major', axis='x', color='tab:orange')

            elif faxis == TRANSF:
                for r, i in zip(v_re, v_im):
                    ax.plot(r, i, color='tab:orange')

            else:
                ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step))
                ax.grid(which='major', axis='x', color='tab:orange')
                for r, i in zip(v_re, v_im):
                    ax.plot(r, i, color='tab:orange')

        else:
            if faxis == ORIG:
                ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step))
                ax.grid(which='major', axis='x', color='tab:orange')
                ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
                ax.grid(which='major', axis='y', color='b')

            elif faxis == TRANSF:
                for r, i in zip(u_re, u_im):
                    ax.plot(r, i, color='b')
                for r, i in zip(v_re, v_im):
                    ax.plot(r, i, color='tab:orange')

            else:
                ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step))
                ax.grid(which='major', axis='x', color='tab:orange')
                ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
                ax.grid(which='major', axis='y', color='b')
                for r, i in zip(u_re, u_im):
                    ax.plot(r, i, color='b')
                for r, i in zip(v_re, v_im):
                    ax.plot(r, i, color='tab:orange')

    if inits_point is not None:
        if faxis == TRANSF or faxis == BOTH:
            for init in inits_point:
                fun_init = [fun(item) for item in init]
                fun_init_re = np.array([re(item) for item in fun_init])
                fun_init_im = np.array([im(item) for item in fun_init])
                ax.plot(fun_init_re, fun_init_im, color='g')

        if faxis == ORIG or faxis == BOTH:
            for init in inits_point:
                init_re = np.array([re(item) for item in init])
                init_im = np.array([im(item) for item in init])
                ax.plot(init_re, init_im, color='g')

    plt.xlim(xbound)
    plt.ylim(ybound)
    return plt
