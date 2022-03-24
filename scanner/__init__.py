import cv2
data = cv2.QRCodeDetector()
value, points, straigh_qrcode=data.detectAndDecode(cv2.imread("frame.png"))
print("value:"+value)
# da=cv2.imread("fas.png")
# print(da)