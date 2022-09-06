# importing cv2 pakage
import cv2
# declaring global variables (are used later on)
b = g =r = 0
#reading image
img = cv2.imread('C:/Users/kiran/Desktop/POGAKULA K/ddd.jpg')
# function to get x,y coordinates of mouse double click
def draw_function(event, x,y, glags,params):
    global b
    global g
    global r
    global img
    if event == cv2.EVENT_RBUTTONDBLCLK:
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        cv2.imshow('image', img)
        #Drawing rectangle on a image
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        #putting text on image
        cv2.putText(img, "Red ="+str(r)+''+'  Green='+str(g)+''+'  Blue='+str(b), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        

cv2.namedWindow('image')      
#Calling function   
cv2.setMouseCallback('image', draw_function)
cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()