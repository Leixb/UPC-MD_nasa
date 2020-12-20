# %run 00-common
# %matplotlib inline

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import plotting
from pylab import rcParams

fig_width_pt = 455  # Get this from LaTeX using \message{\the\columnwidth}

inches_per_pt = 1.0 / 72.27  # Convert pt to inch
golden_mean = (sqrt(5) - 1.0) / 2.0  # Aesthetic ratio
fig_width = fig_width_pt * inches_per_pt  # width in inches
fig_height = fig_width * golden_mean  # height in inches
fig_size = [fig_width, fig_height]
params = {
    "backend": "ps",
    "axes.labelsize": 10,
    "font.size": 10,
    "legend.fontsize": 10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "text.usetex": True,
    "figure.figsize": fig_size,
    "savefig.bbox": "tight",
}
rcParams.update(params)

pd.options.display.max_columns = 4000
sns.set_theme()
