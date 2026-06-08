import cv2
#load and convert the image to gray scale
img=cv2.imread("image.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#create a window
cv2.namedWindow("Controls")
#slider controls
cv2.createTrackbar("Gaussian Blur","Controls",1,20,lambda x:None)
cv2.createTrackbar("Median Kernel","Controls",1,20, lambda x:None)
cv2.createTrackbar("Canny Min","Controls",50,255, lambda x:None)
cv2.createTrackbar("Canny Max","Controls",150,255,lambda x:None)
while True:
    #get the slider valuse
    gk=cv2.getTrackbarPos("Gaussian Blur","Controls")
    mk = cv2.getTrackbarPos("Median Kernel","Controls")
    cmin = cv2.getTrackbarPos("Canny Min","Controls")
    cmax = cv2.getTrackbarPos("Canny Max","Controls")
    #kernel size-must be odd
    gk=gk*2+1
    mk=mk*2+1
    #apply the filters
    gaussian=cv2.GaussianBlur(gray,(gk,gk),0)
    median=cv2.medianBlur(gray,mk)
    #edge detection
    sobelx=cv2.Sobel(gaussian,cv2.CV_64F,1,0,ksize=3)
    sobely = cv2.Sobel(gaussian, cv2.CV_64F, 0, 1,ksize=3)
    laplacian=cv2.Laplacian(gaussian,cv2.CV_64F)
    canny = cv2.Canny(gaussian, cmin, cmax)
    #convet into displayable format
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    laplacian = cv2.convertScaleAbs(laplacian)
    #show the results
    cv2.imshow("original image",img)
    cv2.imshow("Gaussian Blur",gaussian)
    cv2.imshow("Median Blur",median)
    cv2.imshow("Sobel X",sobelx)
    cv2.imshow("Sobel Y",sobely)
    cv2.imshow("Laplacian",laplacian)
    cv2.imshow("Canny",canny)
    #q-quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()