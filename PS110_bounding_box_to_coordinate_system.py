#-------------------------------------------------------------------------------
# Name:         PS110_bounding_box_to_coordinate_system.py
# Purpose:      Rotates model bounding box in accordance of coordiante system
#                   for the active chunk, bounding box size is kept. The orig.
#                   version of this script (for Phtoscan v.0.9.x) was provided
#                   by the AgiSoft support staff. Updated for version 1.1.x.
#
# Compatibility: Agisoft PhotoScan Professional 1.1.x
#
# Author:       James Dietrich, Dartmouth College
#               james.t.dietrich@dartmouth.edu
# Created:      18/01/2015
# Copyright:    (c) James Dietrich 2015
# Licence:      MIT
#
# Useage:       Open the script file in Photoscan (from the Console or Tools
#                   menu. No arguments are needed.
#               *** The coodinate system of the project needs to be set to
#               *** something other than 'Local Coordinates'
#-------------------------------------------------------------------------------

import PhotoScan
import math

doc = PhotoScan.app.document

chnk = doc.chunk

T = chnk.transform

v = PhotoScan.Vector( [0,0,0,1] )

v_t = T.matrix * v

v_t.size = 3

m = chnk.crs.localframe(v_t)

m = m * T.matrix

s = math.sqrt(m[0,0]*m[0,0] + m[0,1]*m[0,1] + m[0,2]*m[0,2]) #scale factor
# S = PhotoScan.Matrix( [[s, 0, 0], [0, s, 0], [0, 0, s]] ) #scale matrix

R = PhotoScan.Matrix( [[m[0,0],m[0,1],m[0,2]], [m[1,0],m[1,1],m[1,2]], [m[2,0],m[2,1],m[2,2]]])

R = R * (1. / s)

reg = chnk.region
reg.rot = R.t()
chnk.region = reg

