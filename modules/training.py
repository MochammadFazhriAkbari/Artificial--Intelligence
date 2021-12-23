from os import name

from cv2 import data, imread


class Training:
    def __init__(self, model_path="", model_output=""):
        self.model_path = model_path
        self.model_output = model_output
    def Train(self):
        from imutils import paths
        import face_recognition
        import pickle
        import cv2
        import os
        imagePaths = list(paths.list_images(self.model_path))
        knownEncodings = []
        knownNames = []
        for (i, imagePaths) in enumerate(imagePaths):
            name = imagePaths.split(os.path.sep)[-2]
            print(name)
            print(imagePaths)
            image = cv2.imread(imagePaths)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb, model='haar')
            encodings = face_recognition.face_encodings(rgb, boxes)
            for encoding in encodings:
                knownEncodings.append(encoding)
                knownNames.append(name)
            data = {"encodings": knownEncodings, "names": knownNames}
            f = open(self.model_output, "wb")
            f.write(pickle.dumps(data))
            f.close()
    def Cleaning(self, models=""):
        import cv2
        import os
        import glob
        folder_target = input("Masukkan folder model yang ingin dibersihkan: ")
        detector_wajah = cv2.CascadeClassifier(models)
        data_path = os.path.join(self.model_path+'/'+folder_target,'*g')
        files = glob.glob(data_path)
        output = 1
        try:
            os.mkdir(self.model_path+'/cleaned_'+folder_target)
        except:
            pass
        for file in files:
            print(file)
            image = cv2.imread(file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

            for(x, y, w, h) in bounding_box:
                output += 1
                gambar_wajah = image[y:(y+h), x:(x+w)]
                cv2.imwrite(self.model_path+"/cleaned_"+folder_target+"/{}.jpg".format(output))
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.waitKey(1)
