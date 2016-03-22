#Matplotlib_Example3.py


#COMMENT: Imports.

import numpy as np;
import matplotlib.image as img;
import matplotlib.pyplot as plt;


#COMMENT: Read in the image.

image = img.imread("TEM.png");

#COMMENT: Convert the (r, g, b, a) image data to a 2D "intensity map" (= grayscale colour).

intensityMap = np.average(image[:, :, :3], axis = 2);

#COMMENT: Create a new figure.
#COMMENT: Note that the canvas dimensions should match the aspect ratio of the image, otherwise you'll get a white border.

plt.figure(figsize = (12.8 / 2.54, 9.6 / 2.54));

#COMMENT: Plot the image data using the plt.imshow() function.
#COMMENT: The cmap = ... parameter sets the colour scheme to use.

plt.imshow(intensityMap, cmap = 'afmhot');

#COMMENT: Switch off the axes.

plt.axis('off');

#COMMENT: Resize the plot area to fill the canvas.

plt.subplots_adjust(left = 0.0, bottom = 0.0, right = 1.0, top = 1.0);

#COMMENT: Save the image and clean up.

plt.savefig("TEM-FalseColour.png", format = 'png', dpi = 300);
plt.close();
