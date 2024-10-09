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
HA_DISCOVERY_PUBLISHED = False  # to ensure that we only publish one time to autodiscovery

def my_logging(msg):
    if DEBUG:
        logging.debug(msg)
    syslog.syslog(syslog.LOG_INFO, msg)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        my_logging('Connected to broker with the result code: ' + str(rc))
        global Connected
        Connected = 1  # Signal connection
    else:
        my_logging('Connected to broker failed with the result code: ' + str(rc))

def on_disconnect(client, userdata, rc):
    global Connected
    Connected = 0

def on_publish(client, userdata, result):
    if DEBUG:
        my_logging('Data published result: ' + str(result))
    pass

def getpage(url):
    timeout = urllib3.Timeout(connect=2.0, read=7.0)
    http = urllib3.PoolManager(timeout=timeout)
    
    if DEBUG:
        my_logging('Getting page...')
    response = http.request('GET', url)

    if DEBUG:
        logging.debug(response.data)
        my_logging('Returning page...')

    return response.data

def publish_ha_discovery(client):
    global HA_DISCOVERY_PUBLISHED

    if not HA_DISCOVERY_PUBLISHED:
        my_logging('Publishing Home Assistant discovery messages...')

        # sensor list configured
        sensors = [
            {"name": "Model", "state_topic": "wibeee/model", "device_class": "none", "unit": None},
            {"name": "Timestamp", "state_topic": "wibeee/time", "device_class": "timestamp", "unit": None},
            # l1
            {"name": "L1 Voltage", "state_topic": "wibeee/fase1_vrms", "device_class": "voltage", "unit": "V"},
            {"name": "L1 Current", "state_topic": "wibeee/fase1_irms", "device_class": "current", "unit": "A"},
            {"name": "L1 Apparent Power", "state_topic": "wibeee/fase1_p_aparent", "device_class": "power", "unit": "VA"},
            {"name": "L1 Active Power", "state_topic": "wibeee/fase1_p_activa", "device_class": "power", "unit": "W"},
            {"name": "L1 Reactive Inductive Power", "state_topic": "wibeee/fase1_p_reactiva_ind", "device_class": "power", "unit": "var"},
            {"name": "L1 Reactive Capacitive Power", "state_topic": "wibeee/fase1_p_reactiva_cap", "device_class": "power", "unit": "var"},
            {"name": "L1 Frequency", "state_topic": "wibeee/fase1_frecuencia", "device_class": "frequency", "unit": "Hz"},
            {"name": "L1 Power Factor", "state_topic": "wibeee/fase1_factor_potencia", "device_class": "power_factor", "unit": None},
            {"name": "L1 Active Energy", "state_topic": "wibeee/fase1_energia_activa", "device_class": "energy", "unit": "Wh", "state_class": "total_increasing"},
            {"name": "L1 Reactive Inductive Energy", "state_topic": "wibeee/fase1_energia_reactiva_ind", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
            {"name": "L1 Reactive Capacitive Energy", "state_topic": "wibeee/fase1_energia_reactiva_cap", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
            # l2
            {"name": "L2 Voltage", "state_topic": "wibeee/fase2_vrms", "device_class": "voltage", "unit": "V"},
            {"name": "L2 Current", "state_topic": "wibeee/fase2_irms", "device_class": "current", "unit": "A"},
            {"name": "L2 Apparent Power", "state_topic": "wibeee/fase2_p_aparent", "device_class": "power", "unit": "VA"},
            {"name": "L2 Active Power", "state_topic": "wibeee/fase2_p_activa", "device_class": "power", "unit": "W"},
            {"name": "L2 Reactive Inductive Power", "state_topic": "wibeee/fase2_p_reactiva_ind", "device_class": "power", "unit": "var"},
            {"name": "L2 Reactive Capacitive Power", "state_topic": "wibeee/fase2_p_reactiva_cap", "device_class": "power", "unit": "var"},
            {"name": "L2 Frequency", "state_topic": "wibeee/fase2_frecuencia", "device_class": "frequency", "unit": "Hz"},
            {"name": "L2 Power Factor", "state_topic": "wibeee/fase2_factor_potencia", "device_class": "power_factor", "unit": None},
            {"name": "L2 Active Energy", "state_topic": "wibeee/fase2_energia_activa", "device_class": "energy", "unit": "Wh", "state_class": "total_increasing"},
            {"name": "L2 Reactive Inductive Energy", "state_topic": "wibeee/fase2_energia_reactiva_ind", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
            {"name": "L2 Reactive Capacitive Energy", "state_topic": "wibeee/fase2_energia_reactiva_cap", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
            # l3
            {"name": "L3 Voltage", "state_topic": "wibeee/fase3_vrms", "device_class": "voltage", "unit": "V"},
            {"name": "L3 Current", "state_topic": "wibeee/fase3_irms", "device_class": "current", "unit": "A"},
            {"name": "L3 Apparent Power", "state_topic": "wibeee/fase3_p_aparent", "device_class": "power", "unit": "VA"},
            {"name": "L3 Active Power", "state_topic": "wibeee/fase3_p_activa", "device_class": "power", "unit": "W"},
            {"name": "L3 Reactive Inductive Power", "state_topic": "wibeee/fase3_p_reactiva_ind", "device_class": "power", "unit": "var"},
            {"name": "L3 Reactive Capacitive Power", "state_topic": "wibeee/fase3_p_reactiva_cap", "device_class": "power", "unit": "var"},
            {"name": "L3 Frequency", "state_topic": "wibeee/fase3_frecuencia", "device_class": "frequency", "unit": "Hz"},
            {"name": "L3 Power Factor", "state_topic": "wibeee/fase3_factor_potencia", "device_class": "power_factor", "unit": None},
            {"name": "L3 Active Energy", "state_topic": "wibeee/fase3_energia_activa", "device_class": "energy", "unit": "Wh", "state_class": "total_increasing"},
            {"name": "L3 Reactive Inductive Energy", "state_topic": "wibeee/fase3_energia_reactiva_ind", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
            {"name": "L3 Reactive Capacitive Energy", "state_topic": "wibeee/fase3_energia_reactiva_cap", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
            # l4 / total
            {"name": "Total Voltage", "state_topic": "wibeee/fase4_vrms", "device_class": "voltage", "unit": "V"},
            {"name": "Total Current", "state_topic": "wibeee/fase4_irms", "device_class": "current", "unit": "A"},
            {"name": "Total Apparent Power", "state_topic": "wibeee/fase4_p_aparent", "device_class": "power", "unit": "VA"},
            {"name": "Total Active Power", "state_topic": "wibeee/fase4_p_activa", "device_class": "power", "unit": "W"},
            {"name": "Total Reactive Inductive Power", "state_topic": "wibeee/fase4_p_reactiva_ind", "device_class": "power", "unit": "var"},
            {"name": "Total Reactive Capacitive Power", "state_topic": "wibeee/fase4_p_reactiva_cap", "device_class": "power", "unit": "var"},
            {"name": "Total Frequency", "state_topic": "wibeee/fase4_frecuencia", "device_class": "frequency", "unit": "Hz"},
            {"name": "Total Power Factor", "state_topic": "wibeee/fase4_factor_potencia", "device_class": "power_factor", "unit": None},
            {"name": "Total Active Energy", "state_topic": "wibeee/fase4_energia_activa", "state_class": "total_increasing", "device_class": "energy", "unit": "Wh"},
            {"name": "Total Reactive Inductive Energy", "state_topic": "wibeee/fase4_energia_reactiva_ind", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
            {"name": "Total Reactive Capacitive Energy", "state_topic": "wibeee/fase4_energia_reactiva_cap", "state_class": "total_increasing", "device_class": "energy", "unit": "varh"},
        ]

        for sensor in sensors:
            sensor_config = {
                "name": sensor["name"],
                "state_topic": sensor["state_topic"],
                "state_class": sensor.get("state_class"),  # if exists add this sensor
                "unit_of_measurement": sensor["unit"],
                "device_class": sensor["device_class"],
                "unique_id": f"wibeee_{sensor['name'].lower().replace(' ', '_')}",
                "device": {
                    "identifiers": ["wibeee"],
                    "name": "Wibeee Energy Monitor",
                    "model": "Wibeee",
                    "manufacturer": "Wibeee Manufacturer"
                }
            }

            # Serializando the dictionary in JSON
            payload = json.dumps(sensor_config)

            ha_topic = f"{HA_DISCOVER_TOPIC}/sensor/wibeee_{sensor['name'].lower().replace(' ', '_')}/config"
            #client.publish(ha_topic, json.dumps(sensor_config), retain=True)
            #my_logging(f"Published HA discovery for {sensor['name']} to topic {ha_topic}")
            result = client.publish(ha_topic, payload, retain=True)

            if DEBUG:
                my_logging(f"Published HA discovery to topic {ha_topic}, payload: {payload}")


        HA_DISCOVERY_PUBLISHED = True  # marked as published

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)

config = configparser.ConfigParser()
config.read('wibeee2mqtt.conf')

DEBUG = int(config['global']['debug'])
WIBEEE_URL = config['wibeee']['wibeee_url']
HA = int(config['global'].get('ha', 0))  # returns 0 as default
HA_DISCOVER_TOPIC = config['global'].get('ha_discover_prefix', 'homeassistant')

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

# var to ensure the last value readed in fase4_energia_activa, because sometimes is less that the actual value
last_fase4_energia_activa_value = None

while True:
    time.sleep(10)
    client.loop()
    if DEBUG:
        my_logging('HA enabled: ' + str(HA))
        my_logging('Connected: ' + str(Connected))

    if Connected == 1:
        if HA == 1 and not HA_DISCOVERY_PUBLISHED:
            # publish autodiscover message to Home Assistant
            publish_ha_discovery(client)

        # gets the XML message from wibeee URL
        xml = getpage(WIBEEE_URL)
        # Parseia a string XML
        root = ElementTree.fromstring(xml)

        for child in root:
            # Se for a tag 'time', loga o timestamp
            if child.tag == 'time':
                try:
                    unix_timestamp = int(child.text)  # Converte para inteiro
                    iso_timestamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(unix_timestamp))
                    my_logging('reading info, timestamp: ' + iso_timestamp)
                    client.publish("wibeee/" + child.tag, iso_timestamp)
                except ValueError:
                    my_logging('Error: Invalid timestamp value in child.text')
            # if the tag is 'fase4_energia_activa', verify if the valor is incrementing
            elif child.tag == 'fase4_energia_activa':
                try:
                    # value to float
                    new_fase4_energia_activa_value = float(child.text)

                    # if is the first time it will be None, only gets the value
                    if last_fase4_energia_activa_value is None:
                        last_fase4_energia_activa_value = new_fase4_energia_activa_value

                    # verify is the new value is bigger that the last value
                    elif new_fase4_energia_activa_value >= last_fase4_energia_activa_value:
                        # Atualiza o último valor e publica no MQTT
                        client.publish("wibeee/" + child.tag, child.text)
                        last_fase4_energia_activa_value = new_fase4_energia_activa_value
                        my_logging(f'Published new value for fase4_energia_activa: {new_fase4_energia_activa_value}')
                    else:
                        # if the value is lower, skip the post
                        my_logging(f'Ignored lower value for fase4_energia_activa: {new_fase4_energia_activa_value}')
                except ValueError:
                    my_logging('Error: Invalid energy value in child.text')
            else:
                # Publica os dados lidos no tópico MQTT
                client.publish("wibeee/" + child.tag, child.text)
    else:
        client.connect(broker_address, port=broker_port)
        time.sleep(5)
