from os import name

from face_recognition.api import face_encodings

from modules.tts import TextSpeech


class Testing :
    def __init__(self, models="", trained_models="", input=""):
        self.models = models
        self.trained_models = trained_models
        self.input = input

    def Test(self):
        import face_recognition
        import imutils
        import pickle
        import time
        import cv2
        import os
        faceCascade = cv2.CascadeClassifier(self.models)
        data = pickle.loads(open(self.trained_models, "rb").read())
        print("Streaming Started")
        video_capture = cv2.VideoCapture(self.input)
        current_name = ""
        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60), flags=cv2.CASCADE_SCALE_IMAGE)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            encodings = face_recognition.face_encodings(rgb)
            names = []

            for encoding in encodings:
                matches = face_encodings.compare_faces(data["encodings"], encoding)
                name = "Unknown"
                if True in matches:
                    matchedidxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    for i in matchedidxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)
                if name != "Unknown" and name != current_name:
                    current_name = name
                    tts_speech = TextSpeech(text=name, output="attachment", voice_type=voice_type)
                    tts_speech.PPTIKSpeech()
                        
                names.append(name)
                for ((x, y, w, h), name) in zip(faces, names):
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) and 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()
        