#NumPy_Example2.py


#COMMENT: Imports.

import math;

import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;


#COMMENT: Define a Gaussian() function using NumPy operations.

def Gaussian(x, a, mu, sigma):
    return (a / (sigma * math.sqrt(2 * math.pi))) * np.exp(-1 * ((x - mu) ** 2 / (2 * sigma ** 2)));


#COMMENT: Set defaults for the font, font size and line width.

mpl.rc('font', **{ 'family' : 'serif', 'size' : 8, 'serif' : 'Times New Roman' });
mpl.rc('lines', **{ 'linewidth' : 0.5 });

#COMMENT: Create a new figure 8.6 x 7.0 cm in size.

plt.figure(figsize = (8.6 / 2.54, 7.0 / 2.54));

#COMMENT: Generate a set of x values to draw the Gaussian curves with using np.linspace().

x = np.linspace(-6.0, 6.0, 1000);

#COMMENT: Use a for loop to plot  curves for four different sigma values and a = 1, mu = 0.

for sigma in [0.25, 0.5, 1.0, 2.5]:
    #COMMENT: Use the label = ... keyword to have Matplotlib prepare a set of legend entries.

    plt.plot(x, Gaussian(x, 1, 0, sigma), label = "$\sigma$ = {0:.2f}".format(sigma));

#COMMENT: Add a legend in the upper-right corner of the plot.

plt.legend(loc = 'upper right', frameon = False);

#COMMENT: Add x and y labels.

plt.xlabel("$x$");
plt.ylabel("$G(x)$");

#COMMENT: Set the axis border width.

for spine in plt.gca().spines.values():
    spine.set_linewidth(0.5);

#COMMENT: "Magic" function.

plt.tight_layout();

#COMMENT: Export the figure to a PNG file.

plt.savefig("Gaussians.png", format = 'png', dpi = 300);
plt.close();
