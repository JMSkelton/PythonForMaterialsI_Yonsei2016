#Matplotlib_Example1.py


#COMMENT: Imports.

import csv;

import matplotlib as mpl;
import matplotlib.pyplot as plt;


#COMMENT: Read input data.

x, y = [], [];

#COMMENT: Open the input file, and create a csv.reader on it.

inputReader = open("PbTe-Kappa.csv", 'r');
inputReaderCSV = csv.reader(inputReader);

#COMMENT: Skip first (header) row.

next(inputReaderCSV);

#COMMENT: Read the remaining rows, convert the first two elements into floats, and store them in x and y.

for row in inputReaderCSV:
    x.append(float(row[0]));
    y.append(float(row[1]));

inputReader.close();

#COMMENT: Basic plot.

#COMMENT: Create a new figure object.

plt.figure();

#COMMENT: Line plot.

plt.plot(x, y);

#COMMENT: Set axis labels.

plt.xlabel("T [K]");
plt.ylabel("Thermal Conductivity [W m-1 K-1]");

#COMMENT: Save to a PNG file.

plt.savefig("PbTe-Kappa.png", format = 'png');

#COMMENT: Clean up.

plt.close();

#COMMENT: "Tidier" plot.

#COMMENT: Set some nicer defaults for the font, font size and line width.

mpl.rc('font', **{ 'family' : 'serif', 'size' : 8, 'serif' : 'Times New Roman' });
mpl.rc('lines', **{ 'linewidth' : 0.5 });

#COMMENT: Specify a size (in inches; to convert from cm divide by 2.54) when the figure is created.

plt.figure(figsize = (8.6 / 2.54, 7.0 / 2.54));

#COMMENT: Specify a line colour, marker style and marker face/edge colour to plt.plot().

plt.plot(x, y, color = 'b', marker = '^', markersize = 5.0, markerfacecolor = 'none', markeredgecolor = 'b');

#COMMENT: Axis labels can use TeX commands delimited by '$' symbols, and font properties can be specified by keyword arguments.

plt.xlabel("$T$ [K]");
plt.ylabel("$\kappa_{L}$ [W m$^{-1}$ K$^{-1}$]");

#COMMENT: Set the y-axis range.

plt.ylim(0.0, 14.0);

#COMMENT: Set the axis border width.

for spine in plt.gca().spines.values():
    spine.set_linewidth(0.5);

#COMMENT: "Magic" function for "tightening up" the plot layout.

plt.tight_layout();

#COMMENT: Specify an image resolution (in DPI) to plt.savefig().

plt.savefig("PbTe-Kappa-v2.png", format = 'png', dpi = 300);
plt.close();
