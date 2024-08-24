import numpy as np
import cv2
import easyocr
import re

class NIKExtractor:

    def __init__(self, uploaded_img):
        self.uploaded_img = uploaded_img
        self.reader = easyocr.Reader(["id"])

    def inputImage(self):
        """ Fungsi membaca image dan resize"""
        if self.uploaded_img is None:
            print(f"Image {self.uploaded_img} is not found")
            return None
        h, w, _ = self.uploaded_img.shape
        resized_img = self.uploaded_img
        if w > 1000 and h > 1000:
            #menentukan ukuran baru
            new_h = int(h*0.20)
            new_w = int(w*0.25)

            #resize
            resized_img = cv2.resize(self.uploaded_img, (new_w, new_h))

        return resized_img

    def cropping_img(self, resized_img):
        """Cropping gambar"""
        #need log, print will do for now
        if resized_img is None:
            print(f"bruh no {resized_img} detected")
            return None
        #converting to hsv
        hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
        #thresholding
        hue_upper = 250
        hue_lower = 30 
        saturation_upper = 250
        saturation_lower = 10  # rentang toleransi saturasi
        value_upper = 200
        value_lower = 71  # rentang toleransi value
        
        up_thresh = np.array([hue_upper, saturation_upper, value_upper], dtype=np.uint8)
        low_thresh = np.array([hue_lower, saturation_lower, value_lower], dtype=np.uint8)
        thresh = cv2.inRange(hsv_img, low_thresh, up_thresh)

        #finding countour
        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) == 0:
            print("No contours found")
            return None

        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        largest_contour = cnts[0]

        #menentukan apakah layak cropping
        area = cv2.contourArea(largest_contour)
        if area > 43000:
            x, y, w, h = cv2.boundingRect(largest_contour)
            ROI = resized_img[y:y+h, x:x+w]
            # cv2.drawContours(resized_img, largest_contour, -1, (0,255,0), 2)
        else:
            ROI = resized_img

        return ROI

    def binarization(self, cropped):
        grayed = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(grayed, (5,5), 0 )
        threshed_img = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21,10)
        return threshed_img

    def extraction(self, binarize):
        """Fungsi ekstraksi gambar KTP menjadi string"""
        if binarize is None:
            text = "Gambar tidak tersedia"
        else:
        # img_pil = Image.fromarray(binarize)
            text = self.reader.readtext(binarize, detail = 0)
            pattern = r"\b\d{16}\b"
            text = re.findall(pattern, ' '.join(text))
        return text