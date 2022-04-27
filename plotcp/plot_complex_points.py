from typing import Iterator, Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


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
