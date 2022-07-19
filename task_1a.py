'''
*****************************************************************************************
*
*        		===============================================
*           		Berryminator (BM) Theme (eYRC 2021-22)
*        		===============================================
*
*  This script is to implement Task 1A of Berryminator(BM) Theme (eYRC 2021-22).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_1a.py
# Functions:		detect_shapes
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def detect_shapes(img):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list
	containing details of colored (non-white) shapes in that image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	Returns:
	---
	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image
	
	Example call:
	---
	shapes = detect_shapes(img)
	"""    
	detected_shapes = []

	##############	ADD YOUR CODE HERE	##############

	
	 
	mask= np.zeros(img.shape[:2], np.uint8)
	bgdModel = np.zeros((1,65), np.float64)
	fgdModel = np.zeros((1,65), np.float64)
	rect = (5, 5, 850, 550)
	cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
	mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
	img1= img*mask2[:,:,np.newaxis]
	background= img- img1
	background[np.where((background>[0,0,0]).all(axis=2))]= [255,255,255]
	final= background + img1

	imgGrey= cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
	_, thrash = cv2.threshold(imgGrey, 245,255, cv2.THRESH_BINARY_INV)
	contours, _ = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for contour in contours:
		approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
		cv2.drawContours(final, [approx], 0, (0,0,0), 2)
		if len(approx)>2 and len(approx)<=3:
			t= []
			M = cv2.moments(contour)
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])
			B,G,R = (final[cY,cX])
			if B>240 and G==0 and R==0:
				t.append("Blue")
				t.append("Triangle")
				cc = (cX,cY)
				t.append(cc)
				detected_shapes.append(t)
			elif G>240 and B==0 and R==0:
				t.append("Green")
				t.append("Triangle")
				cc = (cX,cY)
				t.append(cc)
				detected_shapes.append(t)
			elif R>240 and G==0 and B==0:
				t.append("Red")
				t.append("Triangle")
				cc = (cX,cY)
				t.append(cc)
				detected_shapes.append(t)
			elif R>240 and G>130 and B==0:
				t.append("Orange")
				t.append("Triangle")
				cc = (cX,cY)
				t.append(cc)
				detected_shapes.append(t)
		elif len(approx)==4:
			s= []
			x,y,w,h = cv2.boundingRect(approx)
			aspectRatio= float(w)/float(h)
			if aspectRatio >= 0.95 and aspectRatio <= 1.05:
				M = cv2.moments(contour)
				cX = int(M["m10"] / M["m00"])
				cY = int(M["m01"] / M["m00"])
				B,G,R = (final[cY,cX])
				if B>240 and G==0 and R==0:
					s.append("Blue")
					s.append("Square")
					cc = (cX,cY)
					s.append(cc)
					detected_shapes.append(s)
				elif G>240 and R==0 and B==0:
					s.append("Green")
					s.append("Square")
					cc = (cX,cY)
					s.append(cc)
					detected_shapes.append(s)
				elif R>240 and G==0 and B==0:
					s.append("Red")
					s.append("Square")
					cc = (cX,cY)
					s.append(cc)
					detected_shapes.append(s)
				elif R>240 and G>130 and B==0:
					s.append("Orange")
					s.append("Square")
					cc = (cX,cY)
					s.append(cc)
					detected_shapes.append(s)
			else:
				r= []
				M = cv2.moments(contour)
				cX = int(M["m10"] / M["m00"])
				cY = int(M["m01"] / M["m00"])
				B,G,R = (final[cY,cX])
				if B>240 and G==0 and R==0:
					r.append("Blue")
					r.append("Rectangle")
					cc = (cX,cY)
					r.append(cc)
					detected_shapes.append(r)
				elif G>240 and R==0 and B==0:
					r.append("Green")
					r.append("Rectangle")
					cc = (cX,cY)
					r.append(cc)
					detected_shapes.append(r)
				elif R>240 and G==0 and B==0:
					r.append("Red")
					r.append("Rectangle")
					cc = (cX,cY)
					r.append(cc)
					detected_shapes.append(r)
				elif R>240 and G>130 and B==0:
					r.append("Orange")
					r.append("Rectangle")
					cc = (cX,cY)
					r.append(cc)
					detected_shapes.append(r)
		elif len(approx)<= 5 and len(approx)>4:
			p= []
			M = cv2.moments(contour)
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])
			B,G,R = (final[cY,cX])
			if B>240 and G==0 and R==0:
				p.append("Blue")
				p.append("Pentagon")
				cc = (cX,cY)
				p.append(cc)
				detected_shapes.append(p)
			elif G>240 and B==0 and R==0:
				p.append("Green")
				p.append("Pentagon")
				cc = (cX,cY)
				p.append(cc)
				detected_shapes.append(p)
			elif R>240 and G==0 and B==0:
				p.append("Red")
				p.append("Pentagon")
				cc = (cX,cY)
				p.append(cc)
				detected_shapes.append(p)
			elif R>240 and G>130 and B==0:
				p.append("Orange")
				p.append("Pentagon")
				cc = (cX,cY)
				p.append(cc)
				detected_shapes.append(p)
		elif len(approx)>7:
			c= []
			M = cv2.moments(contour)
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])
			B,G,R = (final[cY,cX])
			if B>240 and G==0 and R==0:
				c.append("Blue")
				c.append("Circle")
				cc = (cX,cY)
				c.append(cc)
				detected_shapes.append(c)
			elif G>240 and B==0 and R==0:
				c.append("Green")
				c.append("Circle")
				cc = (cX,cY)
				c.append(cc)
				detected_shapes.append(c)
			elif R>240 and G==0 and B==0:
				c.append("Red")
				c.append("Circle")
				cc = (cX,cY)
				c.append(cc)
				detected_shapes.append(c)
			elif R>240 and G>130 and B==0:
				c.append("Orange")
				c.append("Circle")
				cc = (cX,cY)
				c.append(cc)
				detected_shapes.append(c)


	##################################################
	
	return detected_shapes

def get_labeled_image(img, detected_shapes):
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########
	"""
	Purpose:
	---
	This function takes the image and the detected shapes list as an argument
	and returns a labelled image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image

	Returns:
	---
	`img` :	[ numpy array ]
			labelled image
	
	Example call:
	---
	img = get_labeled_image(img, detected_shapes)
	"""
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########    

	for detected in detected_shapes:
		colour = detected[0]
		shape = detected[1]
		coordinates = detected[2]
		cv2.putText(img, str((colour, shape)),coordinates, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	return img

if __name__ == '__main__':
	
	# path directory of images in 'test_images' folder
	img_dir_path = 'test_images/'

	# path to 'test_image_1.png' image file
	file_num = 1
	img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
	
	# read image using opencv
	img = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor test_image_' + str(file_num) + '.png')
	
	# detect shape properties from image
	detected_shapes = detect_shapes(img)
	print(detected_shapes)
	
	# display image with labeled shapes
	img = get_labeled_image(img, detected_shapes)
	cv2.imshow("labeled_image", img)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()
	
	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 16):
			
			# path to test image file
			img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
			
			# read image using opencv
			img = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor test_image_' + str(file_num) + '.png')
			
			# detect shape properties from image
			detected_shapes = detect_shapes(img)
			print(detected_shapes)
			
			# display image with labeled shapes
			img = get_labeled_image(img, detected_shapes)
			cv2.imshow("labeled_image", img)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()


