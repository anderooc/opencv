import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
for i in range(0, 310, 10):
    if i % 4 == 0:
        for j in range(10, 330, 20):
            cv2.rectangle(canvas, (j, i), (j + 10, i + 10), (0, 0, 255), -1)
    else:
        for j in range(0, 310, 20):
            cv2.rectangle(canvas, (j, i), (j + 10, i + 10), (0, 0, 255), -1)

cv2.circle(canvas, (canvas.shape[1] // 2, canvas.shape[0] // 2), 50, (0, 255, 0), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)