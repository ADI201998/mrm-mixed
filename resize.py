import cv2
i=1
for i in range(1,131):
    s = str(i) + '.jpg'
    img = cv2.imread(s,1)
    re = cv2.resize(img,(640,480))
    cv2.imwrite(s,re)
    #cv2.waitKey(0)
cv2.destroyAllWindows()
