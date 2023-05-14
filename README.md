# Person detection project

## About the project:
Function 'detection' uses OpenCV to perform human detection in an input image using the Histogram of Oriented Gradients descriptor and SVM classifier. 
detectMultiScale() method returns a list of rectanges that represent the regions of the input image where humans were detected.
Final function returns the number of detected regions and the detection time.

You can get these informations by doing requests via HTTP POST method on http://localhost:5000/obrazki 
