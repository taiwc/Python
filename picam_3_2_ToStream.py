from io import BytesIO
from time import sleep
from picamera import PiCamera

# Create an in-memory stream
my_stream = BytesIO()
camera = PiCamera()
camera.resolution = (320, 240)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture(my_stream, 'jpeg',resize=(320, 240))
camera.stop_preview()
