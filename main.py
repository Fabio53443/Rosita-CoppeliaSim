
from time import *
from datetime import datetime
import numpy as np
from coppeliasim_zmqremoteapi_client import *
import sys, os 
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
    m, sim = setup()
    cam = sim.getObject('./kinect/rgb')
    data, res = sim.getVisionSensorImg(cam, 1)
    sim.saveImage(data, res, 1, f'{sys.argv[0].split("main.py")[0]}{str(time()).split(".")[0]}.png', 20)
    print("hello")

def pan(rad):
    if rad < -1 or rad > 1:
        raise ValueError('value must be between 1 and -1')
    m, sim = setup()
    joint = sim.getObject('./Revolute_joint')
    sim.setJointPosition(joint, rad)


def tilt(rad):
    m, sim = setup()
    joint = sim.getObject('./joint')
    sim.setJointPosition(joint, rad)



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

print(sys.argv[0].split("main.py")[0])

