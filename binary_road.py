def binary_road(img):
	gray = cv2.cvtColor(img, cv2.CV_BGR2GRAY)
	gary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
	erode = cv2.erode(gray, cv2.Mat(), 7)
	dilate = cv2.dilate(gray, cv2.Mat(), 7)
	path_trace = erode+dialte
	cv2.imshow('image', img)

