#Matplotlib_Example2.py


#COMMENT: Imports

import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;


#COMMENT: Function to read plain-text data from a two-column DAT-type file.

def ReadDATFile(filePath, skipLines = 0):
	x, y = [], [];
	
	inputReader = open(filePath, 'r');
	
	for i in range(0, skipLines):
		next(inputReader);
	
	for line in inputReader:
		elements = line.strip().split();
		
		x.append(float(elements[0]));
		y.append(float(elements[1]));
	
	inputReader.close();
	
	return (np.array(x), np.array(y));


#COMMENT: Read input data.

x, y = ReadDATFile("PbTe-DOS.dat", skipLines = 1);

#COMMENT: Plotting code.

#COMMENT: Set Matplotlib defaults.

mpl.rc('font', **{ 'family' : 'serif', 'size' : 8, 'serif' : 'Times New Roman' });
mpl.rc('lines', **{ 'linewidth' : 0.5 });

#COMMENT: Initialise a new figure (8.6 cm x 7.5 cm).

plt.figure(figsize = (8.6 / 2.54, 7.5 / 2.54));

#COMMENT: Fill the area under the curve.

plt.fill_between(x, y, color = 'b', linewidth = 0.0, alpha = 0.25);

#COMMENT: Draw the solid line around the boundary separately.

plt.plot(x, y, color = 'b');

#COMMENT: Label the axes.

plt.xlabel("Frequency [THz]");
plt.ylabel("DOS [States Per F.U.]");

#COMMENT: Set the x-axis range; a.max() is a property of NumPy arrays.

plt.xlim(0.0, x.max());

#COMMENT: Set the spine widths.

for spine in plt.gca().spines.values():
    spine.set_linewidth(0.5);

#COMMENT: "Magic" layout function.

plt.tight_layout();

#COMMENT: Save the figure and cleanup.

plt.savefig("PbTe-DOS.png", format = 'png', dpi = 300);
plt.close();
