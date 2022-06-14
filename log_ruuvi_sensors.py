from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
from pprint import pprint
import json
import time
import glob
import datetime

sleep_delay = 600
sensors=dict()
run_flag = RunFlag()


def handle_data(sensor_data):
    pprint(sensor_data)
    data=dict()
    data["time"]=datetime.datetime.now().isoformat()
    data["id"]=sensor_data[0]
    data["name"]=sensors[data["id"]]["name"]
    data["humidity"]=sensor_data[1]["humidity"]
    data["temperature"] = sensor_data[1]["temperature"]

    with open("ruuvi_sensor_data.log","a") as output:
        json.dump(data,output)
        output.write("\n")
    run_flag.running = False

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
while True:
    for sensor_mac in sensors:
        run_flag.running = True
        RuuviTagSensor.get_datas(handle_data,[sensor_mac],run_flag)
    time.sleep(600)

