import paho.mqtt.client as mqttClient
import struct
import json
import time
import configparser
from xml.etree import ElementTree
import syslog
import logging, sys
import urllib3

Connected = 0

def my_logging(msg):
    if DEBUG :
        logging.debug(msg)
    syslog.syslog(syslog.LOG_INFO, msg)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        my_logging('Connected to broker with the result code: ' + str(rc))
        global Connected                #Use global variable
        Connected = 1                   #Signal connection 
    else:
        my_logging('Connected to broker failed with the result code: ' + str(rc))

def on_disconnect(client, userdata, rc):
   global Connected
   Connected = 0

def on_publish(client, userdata, result):             #create function for callback
    if DEBUG :
        my_logging('Data published result: ' + str(result))
    pass

def getpage(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    if DEBUG :
        logging.debug(response.data)

    return response.data

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)

config = configparser.ConfigParser()
config.read('wibeee2mqtt.conf')

# for debugging only
DEBUG = int(config['global']['debug'])

WIBEEE_URL = config['wibeee']['wibeee_url']

broker_address = config['mqtt']['address']
broker_port = int(config['mqtt']['port'])
broker_username = config['mqtt']['username']
broker_password = config['mqtt']['password']

my_logging('Starting wibeee2mqtt... ')

client = mqttClient.Client("wibeee2mqtt client")
client.username_pw_set(broker_username, password=broker_password)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect(broker_address, port=broker_port)

while True:
    time.sleep(10)
    client.loop()
    my_logging('Connected: ' + str(Connected))
    
    if Connected == 1:
        # Collect the XML  message from a url
        xml = getpage(WIBEEE_URL)
        # Parse the XML string
        root = ElementTree.fromstring(xml)

        for child in root:
            #print ("CHILD: " + child.tag + ": " + child.text)

            if child.tag == 'time': 
                my_logging('reading info, timestamp: ' + str(child.text))

            client.publish("wibeee/"+child.tag, child.text)
    else:
        client.connect(broker_address, port=broker_port)
        time.sleep(5)
