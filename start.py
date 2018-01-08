#!/usr/bin/env python

import RPi.GPIO as GPIO, json, requests, logging, time
# Custom modules
import config

# Overrides
config.BOUNCE_TIME = 16000

logging.basicConfig(filename=config.LOG_FILE_NAME, level=logging.DEBUG)
GPIO.setmode(GPIO.BCM)
GPIO.setup(config.PORT, GPIO.IN)

def notify() :
    logging.info('Detected someone. Sending notification')

    slackResponse = requests.post(
        config.WEBHOOK_URL, data=json.dumps(config.SLACK_DATA),
        headers={'Content-Type': 'application/json'}
    )

    if slackResponse.status_code != 200 :
        logging.error('Request to slack returned an error')

    hueResponse = requests.put(
        config.LIGHTS_ENDPOINT + 'groups/' + str(config.LIGHTS_GROUP_ID) + '/action',
        data=json.dumps({"on": True, "alert": "lselect"})
    )

    if hueResponse.status_code != 200 :
        logging.error('Request to lights returned an error')

def lightsOff() :
    lightsResponse = requests.put(
        config.LIGHTS_ENDPOINT + 'groups/' + str(config.LIGHTS_GROUP_ID) + '/action',
        data=json.dumps({"on": False})
    )

    if lightsResponse.status_code != 200 :
        logging.error('Request to lights returned an error')

def init(*args) :
    notify()
    time.sleep(18)
    lightsOff()

GPIO.add_event_detect(config.PORT, GPIO.RISING, callback=init, bouncetime=config.BOUNCE_TIME)

while True :
    pass
