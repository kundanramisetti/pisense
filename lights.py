#!/usr/bin/env python

import RPi.GPIO as GPIO, time, json, requests
# Custom modules
import config

GPIO.setmode(GPIO.BCM)
GPIO.setup(config.PORT, GPIO.IN)

def switchOn() :
    response = requests.put(
        config.LIGHTS_ENDPOINT + "groups/" + str(config.LIGHTS_GROUP_ID) + "/action",
        data=json.dumps({"scene": config.LIGHTS_SCENE_ID})
    )

def switchOff() :
    response = requests.put(
        config.LIGHTS_ENDPOINT + "groups/" + str(config.LIGHTS_GROUP_ID) + "/action",
        data=json.dumps({"on": False})
    )

def lightUp(*args) :
    switchOn()
    time.sleep(config.LIGHTS_ON_TIME)
    switchOff()

GPIO.add_event_detect(config.PORT, GPIO.RISING, callback=lightUp, bouncetime=config.BOUNCE_TIME)

while True:
    pass
