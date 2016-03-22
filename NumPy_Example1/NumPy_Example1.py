#NumPy_Example1.py


#COMMENT: Imports.

import math;

import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;


#COMMENT: Set defaults for the font, font size and line width.

mpl.rc('font', **{ 'family' : 'serif', 'size' : 8, 'serif' : 'Times New Roman' });
mpl.rc('lines', **{ 'linewidth' : 0.5 });

#COMMENT: Create a new figure 8.6 x 7.0 cm in size.

plt.figure(figsize = (8.6 / 2.54, 7.0 / 2.54));

#COMMENT: Generate 1000 points between [0, 2Pi] to draw the trig functions with using np.linspace().

x = np.linspace(0, 2 * math.pi, 1000);

#COMMENT: Plot y = sin(x), y = cos(x) and y = tan(x).

plt.plot(x, np.sin(x), color = 'b', label = "$F(x) = sin(x)$");
plt.plot(x, np.cos(x), color = 'r', label = "$F(x) = cos(x)$");
plt.plot(x, np.tan(x), color = 'g', label = "$F(x) = tan(x)$");

#COMMENT: Add a legend in the upper-right corner of the plot.

plt.legend(loc = 'upper right', frameon = False);

#COMMENT: Add x and y labels.

plt.xlabel("$x$");
plt.ylabel("$F(x)$");

#COMMENT: Manually set x intervals ("ticks") and labels.

plt.xticks([0.0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi], ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"]);

plt.xlim(0.0, 2 * math.pi);
plt.ylim(-1.5, 1.5);

#COMMENT: Set the axis border width.

for spine in plt.gca().spines.values():
    spine.set_linewidth(0.5);

#COMMENT: "Magic" function.

plt.tight_layout();

#COMMENT: Export the figure to a PNG file.

plt.savefig("TrigFunctions.png", format = 'png', dpi = 300);
plt.close();

#COMMENT: Same again, with a bit of a "hack" to fix the position of the x labels.

plt.figure(figsize = (8.6 / 2.54, 7.0 / 2.54));

x = np.linspace(0, 2 * math.pi, 1000);

plt.plot(x, np.sin(x), color = 'b', label = "$F(x) = sin(x)$");
plt.plot(x, np.cos(x), color = 'r', label = "$F(x) = cos(x)$");
plt.plot(x, np.tan(x), color = 'g', label = "$F(x) = tan(x)$");

plt.legend(loc = 'upper right', frameon = False);

plt.xlabel("$x$");
plt.ylabel("$F(x)$");

#COMMENT: This time, set the "verticalalignment" parameter to align the labels at the text baseline.

plt.xticks([0.0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi], ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"], verticalalignment = 'baseline');

#COMMENT: If we rendered the plot now, the labels would be in the middle of the axis.
#COMMENT: To fix this, we increase the padding between the labels and the axis.

axes = plt.gca();
axes.xaxis.set_tick_params(pad = 10);

plt.xlim(0.0, 2 * math.pi);
plt.ylim(-1.5, 1.5);

for spine in plt.gca().spines.values():
    spine.set_linewidth(0.5);

plt.tight_layout();

plt.savefig("TrigFunctions-2.png", format = 'png', dpi = 300);
plt.close();
