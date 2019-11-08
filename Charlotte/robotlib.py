import RPi.GPIO as GPIO
from time import sleep, time
import signal
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
from pyzbar import pyzbar

in1 = 11
in2 = 12
en = 13
temp1=1

in3 = 15
in4 = 16
enb = 18

IRdevantdroit = 38
IRdevantgauche = 40
IRderrieredroit = 37
IRderrieregauche = 36


camera = PiCamera()

class image:

    def __init__(self):
        self.faces = []
        face_cascade = cv2.CascadeClassifier()
        face_cascade.load(cv2.samples.findFile('../haarcascade_frontalface_alt.xml'))

    def afficher(self, image):
        cv2.imshow("Image", image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

    def capture(self):
        rawCapture = PiRGBArray(camera)

#        sleep(0.05)

        camera.resolution = (683, 384)
        camera.capture(rawCapture, format="bgr")
        return rawCapture.array


    def trouvervisages(self, image):

        image = self.capture()

        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)
        self.faces = self.face_cascade.detectMultiScale(frame_gray)



        return self.faces

    def nombredevisage(self):
        return len(self.faces)


    def positioncode(self, id):

        image = self.capture()
        barcodes = pyzbar.decode(image)

        #self.afficher(image)
        imgw = image.shape[1]
        imgx = image.shape[0]

        #print("Pos", imgx, imgw, sep=" ")


        self.position = None

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            barcodeData = barcode.data.decode("utf-8")
            print("Code:", barcodeData)

            if barcodeData == id:
                imgw = image.shape[1]
                pos = (x+w//2)/imgw

                print("Pos", x, imgw, pos, sep=" ")

                if pos > 0.45 and pos < 0.55:
                    self.position = "milieu"

                if pos <= 0.45:
                    self.position = "gauche"

                if pos >= 0.55:
                    self.position = "droite"

        return self.position





    def positionvisage(self):

        if len(self.faces) == 0:
            return "aucun"

        x,y,w,h = self.faces[0]
        imgw = self.image.shape[1]
        pos = (x+w//2)/imgw

        print("Pos", x, imgw, pos, sep=" ")

        if pos > 0.40 and pos < 0.60:
            return "milieu"

        if pos <= 0.45:
            return "gauche"

        if pos >= 0.55:
            return "droite"







def fin():
    GPIO.cleanup()

def start():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IRdevantdroit, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(IRdevantgauche, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(IRderrieredroit, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(IRderrieregauche, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.setup(enb,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def objetdevant():
    if GPIO.input(IRdevantdroit) == 0 or GPIO.input(IRdevantgauche) == 0:
        return True
    else:
        return False

def objetderriere():
    if GPIO.input(IRderrieredroit) == 0 or GPIO.input(IRderrieregauche) == 0:
        return True
    else:
        return False

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def avance(nb):

    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    sleep(0.1 * nb)

    stop()

def recule(nb):

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    sleep(0.1 * nb)

    stop()

def droite(nb):

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    sleep(0.0085 * nb)

    stop()

def gauche(nb):

    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    sleep(0.0085 * nb)

    stop()

def handler(signum, frame):
    fin()

start()

p=GPIO.PWM(en,1000)
q=GPIO.PWM(enb,1000)
p.start(25)
q.start(25)

p.ChangeDutyCycle(100)
q.ChangeDutyCycle(100)


signal.signal(signal.SIGINT, handler)

img = image()
