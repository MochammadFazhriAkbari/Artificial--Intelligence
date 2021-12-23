class Capture:
    def __init__(self, 
    model="", 
    type="", 
    source="", output="", total_data = 100, start_sec= 1):
        self.model = model
        self.type = type
        self.source = source
        self.output = output
        self.total_data = total_data
        self.start_sec = start_sec
    def CaptureImage(self):
        import cv2
        import os
        detector_wajah = cv2.CascadeClassifier(self.model)
        image = cv2.VideoCapture(self.source)
        if self.type == "video_2":
            image.set(cv2.CAP_PROP_POS_MSEC, self.start_sec)
        counter = 0
        nama = input("Masukkan nama yang dimodelkan: ")
        try:
            os.mkdir(self.output+"/"+nama)
        except:
            pass
        while counter < self.total_data:
            ret, frame = image.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor = 1.01, minNeighbors= 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in bounding_box:
                counter+=1
                gambar_wajah = frame[y:(y+h), x:(x+w)]
                cv2.imwrite(self.output+"/{}/{}.jpg".format(nama,counter), gambar_wajah)
                wajah_blur = cv2.blur(gambar_wajah, (40, 40))
                frame[y:(y+h), x:(x+w)] = wajah_blur
            cv2.imshow("Vid", frame)
            if cv2.waitKey(1) and 0xFF == ord('q'):
                break
        image.release()
        cv2.destroyAllWindows()
    
    def DetectFaceFrontImage(self):
        import cv2
        import os
        import glob

        folder_gambar =input("Masukkan target folder image: ")
        data_path = os.path.join(self.source+"/"+folder_gambar,'*g')
        files = glob.glob(data_path)
        number = 1
        detector_wajah = cv2.CascadeClassifier(self.model)
        try:
            os.mkdir(self.output+"/"+folder_gambar)
        except:
            pass
        for file in files:
            gambar = cv2.imread(file)
            bounding_box = detector_wajah.detectMultiScale(gambar, scaleFactor = 1.01,
            minNeighbors= 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in bounding_box:
                gambar_wajah = gambar[y:(y+h), x:(x+w)]
                cv2.imwrite(self.output+"/"+folder_gambar+"/{}.jpg".format(number),gambar_wajah)
                number+=1


