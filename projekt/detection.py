import cv2
import time

hogcv = cv2.HOGDescriptor()
hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detection(image):
    start = time.time()

    (regions, _) = hogcv.detectMultiScale(image, winStride=(10, 10), padding=(32, 32), scale=1.1)

    end = time.time()

    return len(regions), end - start
