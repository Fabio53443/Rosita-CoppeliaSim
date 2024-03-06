from time import *
import datetime
from qreader import QReader
from coppeliasim_zmqremoteapi_client import *
import sys
from cv2 import COLOR_BGR2RGB, imread, cvtColor


def setup():
    client = RemoteAPIClient()
    sim = client.require('sim')
    motorHandles = [ ]
    motorPath = ['./front_left_wheel', './front_right_wheel', './back_right_wheel', './back_left_wheel']
    for i in range(0, 4):
        motorHandles.append(sim.getObject(motorPath[i]))
    return motorHandles, sim

def getImage():
    print("-- br br mars delay br br")
    m, sim = setup()
    cam = sim.getObject('./kinect/rgb')
    data, res = sim.getVisionSensorImg(cam)
    path = f'{sys.argv[0].split("src/main.py")[0]}/images/{datetime.datetime.now().replace(microsecond=0).isoformat()}.png'
    sim.saveImage(data, res, 0, path, 10)
    return path

def scanTag(path):
    print("trying to decode qrcode")
    qreader = QReader()
    image = cvtColor(imread(path), COLOR_BGR2RGB) # use https://genqrcode.com/generator/3d to create 3d tags
    decoded_text = qreader.detect_and_decode(image=image)
    return decoded_text

def moveJoint(rad, obj):
    if rad < -1 or rad > 1:
        print('value must be between 1 and -1')
        return 0
    m, sim = setup()
    joint = sim.getObject(obj)
    new = sim.getJointPosition(joint) - rad
    sim.setJointPosition(joint, new)
    return new

def pan(rad):
    moveJoint(rad, './panJoint')

def tilt(rad):
    moveJoint(rad, './tiltJoint')

def stop():
    setSpeed4W(0, 0, 0, 0, 0)

def setSpeed4W(fl, fr, bl, br, time):
    vel = [fl*10, -fr*10, -br*10, -bl*10]
    m, sim = setup()
    for i in range(0, 4):
        sim.setJointTargetVelocity(m[i], vel[i])

    sleep(time)

    for i in range(0, 4): 
        sim.setJointTargetVelocity(m[i], 0)



def avanti(speed, time):
    setSpeed4W(speed, speed, speed, speed, time)


def indietro(rawSpeed, time):
    speed = -1 * rawSpeed
    setSpeed4W(speed, speed, speed, speed, time)


def destra(speed, time):
    dxSpeed = -1 * speed
    setSpeed4W(speed, dxSpeed, speed, dxSpeed, time)


def sinistra(speed, time):
    sxSpeed = -1 * speed
    setSpeed4W(sxSpeed, speed, sxSpeed, speed, time)

