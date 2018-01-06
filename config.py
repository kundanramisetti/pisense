# Manage your app specific defaults/config in this file
# This will be imported in the script
PORT = 21 # Input port of your PIR sensor
WEBHOOK_URL = 'https://hooks.slack.com/services/XXXX/XXXXX' # Slack web hook URL
SLACK_DATA = {'text': ":loud_sound: :loud_sound: :loud_sound: *Someone home* :loud_sound: :loud_sound: :loud_sound:"}
LOG_FILE_NAME = 'app.log'
LIGHTS_ENDPOINT = 'http://host/api/username/' # Philips hue web hook URL
LIGHTS_ON_TIME = 60 # Time in seconds to keep the lights on
LIGHTS_SCENE_ID = 'XXXXXXXX' # Philips hue light scene id
LIGHTS_GROUP_ID = 1 # Philips hue lights group id
BOUNCE_TIME = 300 # Default bounce time on the GPIO pin