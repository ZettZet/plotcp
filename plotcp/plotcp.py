from typing import Callable, Tuple, Optional

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.axes import Axes

from plotcp.enums import Faxis, Reim


def plotcp(
        fun: Callable[[complex], complex],
        x_bound: Tuple[int, int],
        y_bound: Tuple[int, int],
        *,
        n_steps: int = 100,
        grid_step: Tuple[int, int] = (10, 10),
        faxis: Faxis = Faxis.BOTH,
        reim: Reim = Reim.BOTH,
        polar: bool = False,
        ax: Optional[Axes] = None
) -> Axes:
    """
    :param fun: your predefined function f(z)
    :param x_bound: real plot bounds
    :param y_bound: imaginary plot bounds
    :param n_steps: how many nodes will be on each line
    :param grid_step: spaces between lines parallel to axis
    :param faxis: what to display: 'origin', 'transform' or 'both' (named constants, correspondingly: Faxis.ORIG,
    Faxis.TRANSFORM, Faxis.BOTH)
    :param reim: which part to display: 'real', 'imag' or 'both' (named constants, correspondingly: Reim.RE, Reim.IM,
    Reim.BOTH) (only works with grid lines, and not areas)
    Inits.TRANSFORM, Inits.BOTH)
    :param polar: use polar grid parametrization instead of cartesian
    :param ax: Axes object to plot on
    :return: matplotlib Axes object
    """
    if ax is None:
        fig, ax = plt.subplots()

    plt.xlim(x_bound)
    plt.ylim(y_bound)

    if polar:
        x_step = 2 * np.pi / grid_step[0]
        y_step = (max(x_bound[1], y_bound[1]) - min(x_bound[0], y_bound[0])) / grid_step[1]
    else:
        x_step = (x_bound[1] - x_bound[0]) / grid_step[0]
        y_step = (y_bound[1] - y_bound[0]) / grid_step[1]

    if faxis & Faxis.ORIG:
        if polar:
            if reim & Reim.RE:
                rays = [np.array([ro * (np.cos(x_step * k) + 1j * np.sin(x_step * k)) for ro in
                                  np.linspace(0, max(x_bound[1], y_bound[1]) * 1.5, n_steps)]) for k in
                        range(grid_step[0])]
                rays_re = [np.real(ray) for ray in rays]
                rays_im = [np.imag(ray) for ray in rays]
                for r, i in zip(rays_re, rays_im):
                    ax.plot(r, i, color='b')

            if reim & Reim.IM:
                circles = [np.array(
                    [y_step * k * (np.cos(theta) + 1j * np.sin(theta)) for theta in np.linspace(0, 2 * np.pi, n_steps)])
                    for k in range(max(x_bound[0], y_bound[0], x_bound[1], y_bound[1]) * 2)]
                circles_re = [np.real(circe) for circe in circles]
                circles_im = [np.imag(circe) for circe in circles]
                for r, i in zip(circles_re, circles_im):
                    ax.plot(r, i, color='tab:orange')

        else:
            if reim & Reim.RE:
                ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
                ax.grid(which='major', axis='y', color='b')

            if reim & Reim.IM:
                ax.xaxis.set_major_locator(ticker.MultipleLocator(x_step))
                ax.grid(which='major', axis='x', color='tab:orange')

        if faxis != Faxis.BOTH:
            return ax

    if faxis & Faxis.TRANSFORM:
        if polar:
            if reim & Reim.RE:
                rays = [np.array([ro * (np.cos(y_step * k) + 1j * np.sin(y_step * k)) for ro in
                                  np.linspace(0, max(x_bound[1], y_bound[1]) * 1.5, n_steps)]) for k in
                        range(grid_step[0])]
                u = [[fun(item) for item in xs] for xs in rays]
                u_re = [np.real(us) for us in u]
                u_im = [np.imag(us) for us in u]

                for r, i in zip(u_re, u_im):
                    ax.plot(r, i, color='b')

            if reim & Reim.IM:
                circles = [np.array([grid_step[1] * k * (np.cos(theta) + 1j * np.sin(theta)) for theta in
                                     np.linspace(0, 2 * np.pi, n_steps)]) for k in range(max(x_bound[1], y_bound[1]))]
                v = [[fun(item) for item in vs] for vs in circles]
                v_re = [np.real(vs) for vs in v]
                v_im = [np.imag(vs) for vs in v]

                for r, i in zip(v_re, v_im):
                    ax.plot(r, i, color='tab:orange')

        else:
            x = np.linspace(x_bound[0], x_bound[1], 2 * grid_step[0])
            y = np.linspace(y_bound[0], y_bound[1], 2 * grid_step[1])

            if reim & Reim.RE:
                x_parallels = [[item_x + item_y * 1j for item_x in np.linspace(x_bound[0], x_bound[1], n_steps)] for
                               item_y
                               in y]
                u = [[fun(item) for item in xs] for xs in x_parallels]
                u_re = [np.real(us) for us in u]
                u_im = [np.imag(us) for us in u]

                for r, i in zip(u_re, u_im):
                    ax.plot(r, i, color='b')

            if reim & Reim.IM:
                y_parallels = [[item_x + item_y * 1j for item_y in np.linspace(y_bound[0], y_bound[1], n_steps)] for
                               item_x
                               in x]
                v = [[fun(item) for item in ys] for ys in y_parallels]
                v_re = [np.real(vs) for vs in v]
                v_im = [np.imag(vs) for vs in v]

                for r, i in zip(v_re, v_im):
                    ax.plot(r, i, color='tab:orange')

    return ax
