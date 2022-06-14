from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
from pprint import pprint
import json
import time
import glob

sleep_delay = 600
sensors=dict()

def handle_data(sensor_data):
    pprint(sensor_data)

#Import sensor configs
for sensor_config_name in glob.glob("monitor_sensor_*.json"):
    with open(sensor_config_name,"r") as sensor_file:
        sensor_config=json.load(sensor_file)
        sensor_config["type"]=="ruuvitag"

        if sensor_config["id"] not in sensors:
            sensors[sensor_config["id"]]=sensor_config
        else:
            print("ERROR same MAC address in two config files, skipping %s"%sensor_config_name)

# List of macs of sensors which will execute callback function
RuuviTagSensor.get_datas(handle_data,macs=sensors.keys())

