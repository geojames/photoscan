#-------------------------------------------------------------------------------
# Name:         PS_110_exportORTHO.py
# Purpose:      Batch export DEMs for all chunks in a project. Especially useful
#                   for time series analysis.
#
# Compatibility: Agisoft PhotoScan Professional 1.1.x
#
# Author:       James Dietrich, Dartmouth College
#               james.t.dietrich@dartmouth.edu
# Created:      18/06/2015
# Copyright:    (c) James Dietrich 2015
# Licence:      MIT
#
# Useage:       Open the script file in Photoscan (from the Console or Tools
#                   menu. In the Arguments box enter the file path and output
#                   resolution for the orthos (all will have the same res)
#                   Example: D:\SfM\dems 0.5
#                   * the file name does not need a trailing slash
#                   * the args should be separated by a single space
#-------------------------------------------------------------------------------

import os
import sys
import PhotoScan

# blending mode
blend = PhotoScan.BlendingMode.MosaicBlending

folder = str(sys.argv[1])      # Path to the folder
res = float(sys.argv[2])       # Resolution of the output DEM

# If the output folder does not exist create it
if not os.path.exists(folder):
    os.mkdir(folder)

# For each cunck in a project export the Ortho to the specified folder
#   using the chunk name as the file name
for chnk in PhotoScan.app.document.chunks:
	filename = folder + '/' + chnk.label + '.tif'
	chnk.exportOrthophoto(filename, format="tif",blending=blend,
        color_correction=False, dx=res, dy=res, projection=chnk.crs)

	print(filename)

PhotoScan.app.messageBox("Export Complete")     # display msgbox when done