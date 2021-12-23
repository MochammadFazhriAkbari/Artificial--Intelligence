import modules.capturing as capturing
import modules.training as training
import modules.testing as testing
Running = True

while Running:
    print("1. Capturing")
    print("2. Training")
    print("3. Testing")
    print("4. Exit")
    pilihan = input("Masukkan pilihan yang diinginkan :")
    if pilihan == "1":
        print("1. Dari Gambar")
        print("2. Dari Video")
        pilihan_take = input('pilih sumber dari pengambilan model')
        if pilihan_take == "1":
            capture = capturing.Capture(
                model="models/haarcascade_frontalface_alt.xml",
                source="input",
                output="output",
            )
            capture.DetectFaceFrontImage()
        elif pilihan_take == "2":
            print("1. Webcam")
            print("2. Video")
        input_type = input("Masukkan tipe pengambilan video: ")
        source = input("Masukkan sumber video: ")
        second = 0
        if input_type == "1":
            source = int(input_type)
        elif input_type == "2":
            second = int(input("Masukkan waktu dimulai video (ms):"))
            source = "input/"+source

         #running sistem capture   
        capture = capturing.Capture(
            model="models/haarcascade_frontalface_alt.xml",
            source=source,
            output="output",
            total_data=200,
            start_sec=second
        )
        capture.CaptureImage()
    train = training.Training(
        model_path = "output",
        model_output = "models/dataset_image"
        )
    if pilihan == "2":
      train.Cleaning("models/haarcascade_frontalface_alt_tree.xml")
    if pilihan == "3":
        train.Train()
    if pilihan == "4":
        test = testing.Testing(
            models="models/haarcascade_frontalface_default.xml",
            trained_models="models/dataset_image",
            input = "input/videoplayback.mp4"
        )
        test.Test()
    if pilihan.lower() == "X".lower():
        Running = False
        print("Program dihentikan")
    print(pilihan)