
from time import sleep
import numpy as np
import qreader
from coppeliasim_zmqremoteapi_client import *
def setup():
    client = RemoteAPIClient()
    sim = client.require('sim')
    motorHandles = [-1, -1, -1, -1]
    motorHandles[0] = sim.getObject('./front_left_wheel')
    motorHandles[1] = sim.getObject('./front_right_wheel')
    motorHandles[2] = sim.getObject('./back_right_wheel')
    motorHandles[3] = sim.getObject('./back_left_wheel')
    return motorHandles, sim

def getImage():
    mH, sim = setup()
    cam = sim.getObject('./kinect/rgb')
    img, [resX, resY] = sim.getVisionSensorImg(cam)
    img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)

def stop():
    setSpeed4W(0, 0, 0, 0, 0)




def setSpeed4W(fl, fr, bl, br, time):
    fl, fr, bl, br = fl*10, fr*10, bl*10, br*10
    m, sim = setup()
    sim.setJointTargetVelocity(m[0], fl)
    sim.setJointTargetVelocity(m[1], -fr)
    sim.setJointTargetVelocity(m[2], -br)
    sim.setJointTargetVelocity(m[3], bl)
    sleep(time)
    sim.setJointTargetVelocity(m[0], 0)
    sim.setJointTargetVelocity(m[1], 0)
    sim.setJointTargetVelocity(m[2], 0)
    sim.setJointTargetVelocity(m[3], 0)



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


setup()