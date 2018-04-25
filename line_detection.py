# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
import glob
import sys
import math


i = 0
for filename in sorted(glob.glob('Images/Testing/*.png')):
	# Reading the required image in 
	# which operations are to be done. 
	# Make sure that the image is in the same 
	# directory in which this python program is
	img = cv2.imread(filename)

	# Convert the img to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	# Apply edge detection method on the image
	edges = cv2.Canny(gray,110, 120)

	# This returns an array of r and theta values
	lines = cv2.HoughLines(edges,1,np.pi/180, 200)

	# draw_line =[]
	# draw_line.append(lines[0])
	# if len(lines) > 1:
	# 	draw_line.append(lines[len(lines)-int(0.5*len(lines))])

	columns, rows, channels = img.shape

	m2 = float("inf")

	min_pos_theta = sys.maxsize
	max_neg_theta = -(sys.maxsize-1)

	posx1 = 0
	posy1 = 0
	posx2 = 0
	posy2 = 0
	negx1 = 0
	negy1 = 0
	negx2 = 0
	negy2 = 0
	# The below for loop runs till r and theta values 
	# are in the range of the 2d array
	for line in lines:
		for r,theta in line:
			
			# Stores the value of cos(theta) in a
			a = np.cos(theta)

			# Stores the value of sin(theta) in b
			b = np.sin(theta)
			
			# x0 stores the value rcos(theta)
			x0 = a*r
			
			# y0 stores the value rsin(theta)
			y0 = b*r
			
			# x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
			x1 = int(x0 + 1000*(-b))
			
			# y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
			y1 = int(y0 + 1000*(a))

			# x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
			x2 = int(x0 - 1000*(-b))
			
			# y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
			y2 = int(y0 - 1000*(a))
			
			if x2 == x1:
				m1 = float("inf")
			else: 	
				m1 = (y2-y1)/(x2-x1)
			if m1<0:
				angle = math.atan2((m1 - m2),(1+m1*m2))
			if m1>0:
				angle = math.atan2((m2 - m1),(1+m1*m2))

			print(angle)

			if angle < 0 and angle > max_neg_theta:
				print('new neg')
				max_neg_theta = angle
				negx1 = x1
				negy1 = y1
				negx2 = x2
				negy2 = y2


			if angle > 0 and angle < min_pos_theta:
				print('new pos')
				min_pos_theta = angle
				posx1 = x1
				posy1 = y1
				posx2 = x2
				posy2 = y2

			print('\n')

			#cv2.line(img, (int(rows/2), 0), (int(rows/2),columns-1), (0,0,255),2)


			# cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
			# (0,0,255) denotes the colour of the line to be 
			#drawn. In this case, it is red. 
			
		# All the changes made in the input image are finally
		# written on a new image houghlines.jpg

	# print(posx1)
	# print(posy1)
	# print(posx2)
	# print(posy2)

	# print(negx1)
	# print(negy1)
	# print(negx2)
	# print(negy2)


	cv2.line(img,(posx1,posy1), (posx2,posy2), (0,0,255),2)
	cv2.line(img,(negx1,negy1), (negx2,negy2), (0,0,255),2)
	
	url = 'Result2/linesDetected.jpg' + str(i) + '.png'
	i = i+1
	cv2.imwrite(url, img)