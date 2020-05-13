#!/usr/bin/python

from pathlib import Path

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# set plot properties
sns.set(context='paper', style='ticks', palette='colorblind')

# load data
fn = Path('./gradient_correction_data.csv')
df = pd.read_csv(fn)

# linear fit on data
x = df.max_gradient.values
y = df.correction_delta.values
x = x[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(x, y, rcond=None)
a = a[0]

obs = [2.55, 36]

fig, ax = plt.subplots()
ax.plot(df.max_gradient, df.correction_delta, 'o', label='$\\tanh(z)$ model',zorder=2)
# ax.plot(obs[0], obs[1], 'o', label='Observed')

ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

xlim = ax.get_xlim()
ax.plot(xlim, a*np.array(xlim), label='$\Delta$O$_2 = %.1f\\frac{\partial \mathrm{O}_2}{\partial z}$' % a, zorder=1)

ax.set_xlim(xlim)

ax.set_title('$\\tau = 75$s', loc='left')
ax.set_xlabel('Gradient Magnitude (mmol m$^{-3}$ dbar$^{-1}$)')
ax.set_ylabel('Correction Magnitude (mmol m$^{-3}$)')
ax.legend(loc=2)

fig.savefig('grad_corr_analysis.png', bbox_inches='tight', dpi=350)
plt.close(fig)