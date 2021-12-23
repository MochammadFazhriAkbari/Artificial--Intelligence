from gtts import tts


class TextSpeech:
    def __init__(self, text="", output=""):
        self.text = text
        self.output = output
        self.voice_type = voice_type
    def PPTIKSpeech(self):
        import requests
        import os
        if self.voice_type == "1":
            from gtts import gTTS
            tts = gTTS("halo "+self.text)
            tts.save(self.output+"/"+self.text+".mp3")
        elif self.voice_type == "2":
            data = requests.post("http://lisanx.pptik.id", data= "Hei Bro!"+self.text)

            with open(self.output+"/"+self.text+".mp3", "wb") as f:
                  f.write(data.content)
        
        from playsound import playsound
        playsound(self.output+'/'+self.text+'.mp3')