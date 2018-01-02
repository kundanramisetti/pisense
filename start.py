#!/usr/bin/env python

import RPi.GPIO as GPIO, time, json, requests, logging, os
# Custom modules
import config

logging.basicConfig(filename=config.LOG_FILE_NAME, level=logging.DEBUG)
GPIO.setmode(GPIO.BCM)
GPIO.setup(config.PORT, GPIO.IN)
GPIO.add_event_detect(config.PORT, GPIO.RISING)

def sendNotification() :
    response = requests.post(
        config.WEBHOOK_URL, data=json.dumps(config.SLACK_DATA),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        logging.error('Request to slack returned an error')

while True:
    i=GPIO.event_detected(config.PORT)
    if i==False:
        time.sleep(config.POLL_TIME)
    elif i==True:
        logging.info('Detected someone. Sending notification')
        sendNotification()
        time.sleep(config.POLL_TIME)
